# HR Employee Attrition Problem

## Business Understanding
Perusahaan multinasional Jaya Jaya Maju, yang telah beroperasi sejak tahun 2000 dan memiliki lebih dari 1000 karyawan, tengah menghadapi tantangan serius dalam mengelola retensi karyawan. Tingkat attrition (rasio karyawan yang keluar dibanding total karyawan) telah menembus angka 13%, yang berdampak pada stabilitas operasional dan potensi kerugian sumber daya. Tingginya angka attrition ini menimbulkan kekhawatiran di kalangan manajemen, khususnya di divisi Human Resources (HR). Oleh karena itu, tim HR memerlukan analisis mendalam dan visualisasi interaktif guna:
- Mengidentifikasi faktor-faktor yang berkontribusi terhadap keputusan karyawan untuk keluar.
- Mengembangkan strategi pencegahan berbasis data.
- Memonitor tren dan pola attrition secara real-time melalui dashboard.

## Business Problem
Manajemen HR ingin menjawab pertanyaan-pertanyaan berikut:
- Apa karakteristik umum karyawan yang keluar (usia, jenis kelamin, pendapatan, jabatan, dll)?
- Bagaimana pengaruh faktor internal perusahaan seperti overtime, salary hike, dan work-life balance terhadap attrition?
- Departemen atau job role mana yang paling terdampak oleh attrition?
- Adakah ketimpangan pendapatan atau jenjang karir yang berkaitan dengan keputusan keluar?

## Project Goals
- Menganalisis pola dan tren employee attrition berdasarkan karakteristik demografis, peran, dan faktor internal.
- Mengidentifikasi faktor-faktor utama yang paling berkorelasi terhadap attrition.
- Membuat dashboard bisnis interaktif yang dapat digunakan oleh tim HR untuk memantau dan mengantisipasi risiko attrition.
- Memberikan insight dan rekomendasi berbasis data yang dapat ditindaklanjuti untuk menurunkan attrition rate.

## Project Scope
- Dataset yang dianalisis mencakup informasi demografi, job role, kompensasi, dan faktor kepuasan kerja dari 1470 karyawan.
- Fokus utama analisis adalah membedakan antara karyawan yang keluar (Attrition = Yes) dan yang bertahan (Attrition = No).
- Pembuatan dashboard mencakup metrik utama seperti:
1. Total Attrition Rate
2. Rata-rata Pendapatan
3. Distribusi berdasarkan usia, pendapatan, job role, overtime, dan lainnya

## Preparation
Sumber data: [Data Employee Attrition](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)
Setup environment:
1. Clone Repository
```bash
git clone https://github.com/hildanida/HR-Problem-Employee-Attrition.git
```
2. Creat Virtual Environment
```bash
# Windows
python -m venv env
env\Scripts\activate

# Mac/Linux
python3 -m venv env
source env/bin/activate
```
3. Install Library
```bash
pip install -r requirements.txt
```
4. Library Used
```bash
# Untuk analisis data
import pandas as pd
import numpy as np

# Untuk visualisasi
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Untuk dashboard interaktif
import streamlit as st
```
5. Run Streamlit
```bash
streamlit run streamlit_app.py
```

## Business Dashboard
