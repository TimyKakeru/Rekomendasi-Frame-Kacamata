# 👓 Rekomendasi Frame Kacamata

Project Python sederhana untuk mendeteksi **bentuk wajah** (Oval, Square, Round) dan merekomendasikan **frame kacamata** yang cocok.  
Menggunakan **OpenCV**, **Mediapipe**, **Pillow**, dan antarmuka **GUI Tkinter**.

---

## 🚀 Fitur

- Deteksi otomatis landmark wajah (dahi, dagu, pipi kiri & kanan)
- Hitung rasio panjang/lebar wajah
- Tentukan bentuk wajah: Oval, Square, atau Round
- Tampilkan hasil bentuk wajah & rasio di GUI
- Rekomendasi jenis frame kacamata sesuai bentuk wajah
- Tampilan gambar input + landmark di GUI (Tkinter)

---

## 📂 Struktur Folder

```
Rekomendasi-Frame-Kacamata/
 ├─ README.md
 ├─ .gitignore
 ├─ requirements.txt
 ├─ deteksi_frame_tkinter.py
 ├─ img/               # Folder contoh gambar wajah
 ├─ celeba_ratios.csv  # (Opsional) file hasil analisis dataset
```
---

⚙️ Persyaratan

- Python >= 3.10 (disarankan menggunakan Anaconda)
- OpenCV ==  4.12.0.88
- Mediapipe =  0.10.14
- Pillow == 11.3.0
- Tkinter (sudah bawaan Python, untuk Linux bisa install python3-tk jika perlu)

---
📥 Cara Instalasi

1️⃣ Clone repositori

```bash
git clone https://github.com/username/Rekomendasi-Frame-Kacamata.git
cd Rekomendasi-Frame-Kacamata
```
2️⃣ (Opsional) Buat virtual environment
```bash
conda create -n rekomendasi-frame python=3.10
conda activate rekomendasi-frame
```
---
▶️ Cara Menjalankan Program

- python deteksi_frame_tkinter.py
- Klik Pilih Gambar ➜ pilih foto wajah (*.png / .jpg)
- Klik Deteksi
- Hasil bentuk wajah, rasio, dan rekomendasi frame akan muncul di GUI
- Gambar wajah + landmark juga ditampilkan

---
🧮 Logika Penentuan Bentuk Wajah

Bentuk	Rasio Panjang / Lebar
- Oval	>= 1.3
- Square	>= 1.1 dan < 1.3
- Round	< 1.1
---
✨ Rekomendasi Frame

Bentuk	Rekomendasi
- Oval	Gunakan frame lebar & tipis
- Square	Gunakan frame bulat
- Round	Gunakan frame kotak / persegi panjang

---

📝 Lisensi
MIT — Bebas digunakan untuk keperluan pembelajaran, riset, dan pengembangan.
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
