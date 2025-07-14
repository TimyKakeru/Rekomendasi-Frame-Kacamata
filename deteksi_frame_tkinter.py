import cv2
import mediapipe as mp
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Mediapipe face mesh setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

# Buat window tkinter
root = tk.Tk()
root.title("Deteksi Frame Kacamata")

# Label untuk hasil
result_label = tk.Label(root, text="Belum ada gambar diproses", font=("Arial", 12))
result_label.pack()

# Canvas untuk gambar
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Variabel global gambar
output_image = None

def pilih_gambar():
    global filepath
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if filepath:
        img = Image.open(filepath)
        img.thumbnail((500, 500))
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(250, 250, image=img_tk)
        canvas.image = img_tk

def deteksi():
    global output_image
    if not filepath:
        messagebox.showerror("Error", "Pilih gambar dulu!")
        return

    # Baca gambar
    image = cv2.imread(filepath)
    if image is None:
        messagebox.showerror("Error", "Gambar tidak valid!")
        return

    height, wide, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_image)

    if not results.multi_face_landmarks:
        result_label.config(text="Wajah tidak terdeteksi!")
        return

    face_landmarks = results.multi_face_landmarks[0]

    # Pakai landmark spesifik: pipi kiri (234), pipi kanan (454), dagu (152), dahi (10)
    left_cheek = face_landmarks.landmark[234]
    right_cheek = face_landmarks.landmark[454]
    chin = face_landmarks.landmark[152]
    forehead = face_landmarks.landmark[10]

    # Konversi ke koordinat piksel
    x_left = int(left_cheek.x * wide)
    y_left = int(left_cheek.y * height)
    x_right = int(right_cheek.x * wide)
    y_right = int(right_cheek.y * height)
    x_chin = int(chin.x * wide)
    y_chin = int(chin.y * height)
    x_forehead = int(forehead.x * wide)
    y_forehead = int(forehead.y * height)

    # Hitung panjang & lebar
    lebar = np.linalg.norm([x_right - x_left, y_right - y_left])
    panjang = np.linalg.norm([x_chin - x_forehead, y_chin - y_forehead])
    rasio = panjang / lebar
    print("Rasio",rasio)
    # Klasifikasi
    if rasio >= 1.3:
        bentuk = "Oval"
        rekomendasi = "Gunakan frame lebar & tipis"
    elif rasio >= 1.1 and rasio < 1.3:
        bentuk = "Square"
        rekomendasi = "Gunakan frame bulat"
    else:
        bentuk = "Round"
        rekomendasi = "Gunakan frame kotak atau persegi panjang"


    # Gambar kotak di gambar
    output = image.copy()
    cv2.circle(output, (x_left, y_left), 5, (0, 255, 0), -1)
    cv2.circle(output, (x_right, y_right), 5, (0, 255, 0), -1)
    cv2.circle(output, (x_chin, y_chin), 5, (255, 0, 0), -1)
    cv2.circle(output, (x_forehead, y_forehead), 5, (255, 0, 0), -1)
    cv2.line(output, (x_left, y_left), (x_right, y_right), (0, 255, 0), 2)
    cv2.line(output, (x_forehead, y_forehead), (x_chin, y_chin), (255, 0, 0), 2)

    # Update label hasil
    result_label.config(text=f"Bentuk: {bentuk} | Rekomendasi: {rekomendasi}")

    # Tampilkan di tkinter
    output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    output_pil = Image.fromarray(output_rgb)
    output_pil.thumbnail((500, 500))
    output_tk = ImageTk.PhotoImage(output_pil)
    canvas.create_image(250, 250, image=output_tk)
    canvas.image = output_tk

# Tombol pilih & deteksi
btn_pilih = tk.Button(root, text="Pilih Gambar", command=pilih_gambar)
btn_pilih.pack(pady=5)

btn_deteksi = tk.Button(root, text="Deteksi", command=deteksi)
btn_deteksi.pack(pady=5)

root.mainloop()
