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
![Dashboard Attrition](employee-attrition-dashboard.png)
Dashboard ini [Employee Attrition Dashboard](https://public.tableau.com/views/employee-attrition/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) merupakan visualisasi menyeluruh untuk memahami pola dan faktor-faktor yang berkaitan dengan *attrition* (keluar dari perusahaan) di Jaya Jaya Maju. Dashboard ini mencakup total karyawan, tingkat attrition, perbandingan pendapatan, serta distribusi attrition berdasarkan usia, jenis kelamin, pendapatan, jabatan, departemen, keseimbangan kerja, hingga overtime.

Dari visualisasi ini, kita bisa melihat bahwa attrition lebih sering terjadi pada karyawan dengan pendapatan rendah, durasi kerja yang lebih singkat, dan beban kerja lebih tinggi (terlihat dari proporsi overtime). Role seperti *Sales Executive* dan *Laboratory Technician* juga menunjukkan angka keluar yang tinggi. Temuan-temuan ini dapat menjadi dasar bagi tim HR untuk mengambil langkah strategis dalam meningkatkan retensi karyawan.

Berdasarkan dashboard, terlihat bahwa attrition lebih banyak terjadi pada karyawan pria, khususnya yang berusia di bawah 30 tahun dan memiliki pendapatan di bawah 3.000 USD. Salah satu faktor paling mencolok adalah *overtime*—lebih dari separuh karyawan yang keluar ternyata bekerja lembur secara rutin. Selain itu, tingkat kepuasan terhadap work-life balance dan job satisfaction yang rendah juga tampak selaras dengan tingginya angka attrition. Dari sisi jabatan, posisi *Sales Executive* dan *Laboratory Technician* memiliki tingkat keluar yang cukup tinggi dibanding peran lainnya, yang bisa menjadi indikator beban kerja atau tekanan yang lebih besar pada posisi tersebut. Insight ini mengarah pada pentingnya perhatian lebih terhadap keseimbangan kerja, kebijakan kompensasi, dan lingkungan kerja di jabatan-jabatan tertentu untuk menekan angka attrition ke depan.

## Conclusion

## Recommendation
