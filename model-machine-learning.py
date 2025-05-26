import warnings
import pickle

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import make_scorer, fbeta_score, classification_report
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, RobustScaler
from imblearn.combine import SMOTEENN
from imblearn.pipeline import Pipeline as ImbPipeline

warnings.filterwarnings('ignore')
warnings.filterwarnings("ignore", module="joblib.externals.loky")


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Map Attrition to binary
    df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})
    # Drop unused columns
    df.drop(columns=['EmployeeId'], inplace=True)
    return df


def encode_ordinals(df: pd.DataFrame) -> pd.DataFrame:
    # Define orders
    education_order = {'Below College': 1, 'College': 2, 'Bachelor': 3, 'Master': 4, 'Doctor': 5}
    sat_order = {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4}
    wb_order = {'Low': 1, 'Good': 2, 'Excellent': 3, 'Outstanding': 4}

    df['Education'] = df['Education'].map(education_order).astype(int)
    for col in ['EnvironmentSatisfaction', 'JobSatisfaction', 'JobInvolvement', 'RelationshipSatisfaction']:
        df[col] = df[col].map(sat_order).astype(int)
    df['WorkLifeBalance'] = df['WorkLifeBalance'].map(wb_order).astype(int)
    return df


def build_preprocessors(cat_features, ord_features, num_features):
    # For RFC & XGB
    preprocessing = ColumnTransformer([
        ('onehot', OneHotEncoder(drop='first'), cat_features),
        ('ordinal', OrdinalEncoder(), ord_features)
    ], remainder='passthrough')

    # For Logistic Regression
    robust_pre = ColumnTransformer([
        ('onehot', OneHotEncoder(drop='first'), cat_features),
        ('ordinal', OrdinalEncoder(), ord_features),
        ('scale', RobustScaler(), num_features)
    ], remainder='drop')
    return preprocessing, robust_pre


def resampling_scores(model, X, y, preprocessing, folds=5):
    """Returns DataFrame of cross-validated F2 scores for given model with SMOTEENN."""
    resampler = SMOTEENN(random_state=42)
    scorer = make_scorer(fbeta_score, beta=2)
    skf = StratifiedKFold(n_splits=folds, shuffle=True, random_state=42)

    pipeline = ImbPipeline([
        ('prep', preprocessing),
        ('resample', resampler),
        ('model', model)
    ])
    scores = cross_val_score(pipeline, X, y, cv=skf, scoring=scorer, n_jobs=-1)
    print(f"{model.__class__.__name__} CV Mean F2: {scores.mean():.4f}  Std: {scores.std():.4f}")


def tune_logistic(X_train, y_train, preprocessor):
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    f2_scorer = make_scorer(fbeta_score, beta=2)
    resampler = SMOTEENN(random_state=42)

    pipe = ImbPipeline([
        ('prep', preprocessor),
        ('resample', resampler),
        ('model', LogisticRegression(random_state=42))
    ])

    param_grid = {
        'model__penalty': ['l1', 'l2', 'elasticnet', None],
        'model__C': [0.01, 0.1, 1, 10],
        'model__solver': ['saga'],
        'model__l1_ratio': [0, 0.5, 1],
        'model__max_iter': [200]
    }
    grid = GridSearchCV(pipe, param_grid, cv=skf, scoring=f2_scorer, n_jobs=-1, error_score='raise')
    grid.fit(X_train, y_train)
    print(f"Best F2: {grid.best_score_:.4f}")
    print("Best Params:", grid.best_params_)
    return grid.best_estimator_


def evaluate_model(model, X_train, y_train, X_test, y_test):
    # Fit and predict
    model.fit(X_train, y_train)
    for split, (Xs, ys) in zip(['Train', 'Test'], [(X_train, y_train), (X_test, y_test)]):
        preds = model.predict(Xs)
        print(f"\n{split} Classification Report:\n", classification_report(ys, preds))


def save_model(model, filename: str):
    pickle.dump(model, open(filename, 'wb'))
    print(f"Model saved to {filename}")


def main():
    # Paths
    data_path = 'employee_data_cleaned.csv'
    model_path = 'employee_attrition_logreg.sav'

    # Load & prepare data
    df = load_data(data_path)
    df = encode_ordinals(df)

    # Feature lists
    cat_feats = ['BusinessTravel','Department','EducationField','Gender',
                 'JobRole','MaritalStatus','OverTime','PerformanceRating']
    ord_feats = ['Education','EnvironmentSatisfaction','JobInvolvement',
                 'JobSatisfaction','WorkLifeBalance','JobLevel',
                 'StockOptionLevel','RelationshipSatisfaction']
    num_feats = ['Age','DailyRate','DistanceFromHome','HourlyRate',
                 'MonthlyIncome','MonthlyRate','NumCompaniesWorked',
                 'PercentSalaryHike','TotalWorkingYears','TrainingTimesLastYear',
                 'YearsAtCompany','YearsInCurrentRole',
                 'YearsSinceLastPromotion','YearsWithCurrManager']

    # Build preprocessors
    pre, robust_pre = build_preprocessors(cat_feats, ord_feats, num_feats)

    # Split
    X = df.drop('Attrition', axis=1)
    y = df['Attrition']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Baseline resampling evaluation
    resampling_scores(LogisticRegression(random_state=42), X_train, y_train, robust_pre)

    # Hyperparameter tuning
    best_logreg = tune_logistic(X_train, y_train, robust_pre)

    # Final evaluation
    evaluate_model(best_logreg, X_train, y_train, X_test, y_test)

    # Save model
    save_model(best_logreg, model_path)


if __name__ == '__main__':
    main()