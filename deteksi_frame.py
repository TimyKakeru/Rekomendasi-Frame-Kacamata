import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

image = cv2.imread("Wajah2.jpg")
if image is None:
    print("Gambar tidak ditemukan!")
    exit()

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

results = face_mesh.process(rgb_image)

if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        h, w, _ = image.shape

        pelipis_kiri = face_landmarks.landmark[127]
        pelipis_kanan = face_landmarks.landmark[356]
        dagu = face_landmarks.landmark[152]
        dahi = face_landmarks.landmark[10]

        lebar = ((pelipis_kanan.x - pelipis_kiri.x) * w)
        panjang = ((dagu.y - dahi.y) * h)

        print(f"Lebar wajah: {abs(lebar):.2f} px")
        print(f"Panjang wajah: {abs(panjang):.2f} px")

        rasio = abs(panjang) / abs(lebar)
        print(f"Rasio Panjang/Lebar: {rasio:.2f}")

        if rasio >= 1.3:
            bentuk = "Oval"
        elif 0.9 < rasio < 1.3:
            bentuk = "Round"
        else:
            bentuk = "Square"

        print(f"Bentuk wajah terdeteksi: {bentuk}")

        if bentuk == "Oval":
            print("Rekomendasi: Cocok dengan semua frame, terutama frame bulat atau persegi panjang.")
        elif bentuk == "Round":
            print("Rekomendasi: Gunakan frame kotak atau persegi panjang untuk menyeimbangkan.")
        elif bentuk == "Square":
            print("Rekomendasi: Gunakan frame bulat atau oval untuk melembutkan sudut wajah.")
else:
    print("Tidak ada wajah terdeteksi.")
