import cv2
import mediapipe as mp

# Inisialisasi Face Detection & Drawing
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)
mp_drawing = mp.solutions.drawing_utils

# Baca gambar
image = cv2.imread("Wajah.jpg")
if image is None:
    print("Gambar tidak ditemukan!")
    exit()

# Convert ke RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Proses face mesh
results = face_mesh.process(rgb_image)

if not results.multi_face_landmarks:
    print("Wajah tidak terdeteksi!")
    exit()

# Ambil landmark wajah pertama
face_landmarks = results.multi_face_landmarks[0]

# Cari batas kiri, kanan, atas, bawah wajah
h, w, _ = image.shape
x_coords = [lm.x * w for lm in face_landmarks.landmark]
y_coords = [lm.y * h for lm in face_landmarks.landmark]

min_x, max_x = min(x_coords), max(x_coords)
min_y, max_y = min(y_coords), max(y_coords)

lebar_wajah = max_x - min_x
tinggi_wajah = max_y - min_y
rasio = tinggi_wajah / lebar_wajah

# Tentukan bentuk wajah
if rasio >= 1.3:
    bentuk = "Oval"
    rekomendasi = "Gunakan frame lebar & tidak terlalu tebal"
elif rasio <= 1.1:
    bentuk = "Round"
    rekomendasi = "Gunakan frame kotak atau persegi panjang"
else:
    bentuk = "Square"
    rekomendasi = "Gunakan frame bulat untuk melembutkan sudut"

print(f"Bentuk wajah: {bentuk}")
print(f"Rekomendasi: {rekomendasi}")

# Tulis teks ke gambar
output = image.copy()
cv2.rectangle(output, (int(min_x), int(min_y)), (int(max_x), int(max_y)), (0, 255, 0), 2)
cv2.putText(output, f'Bentuk: {bentuk}', (30, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.putText(output, f'{rekomendasi}', (30, 60),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

# Tampilkan gambar di jendela
cv2.imshow("Hasil Deteksi", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
