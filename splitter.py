import cv2
import os

# Buka video
mode = ''
video = 'pantry'
video_path = f'{mode}assets/{video}.mp4'
cap = cv2.VideoCapture(video_path)

# Periksa apakah video berhasil dibuka
if not cap.isOpened():
    print("Gagal membuka video")
    exit()

# Buat direktori penyimpanan
os.makedirs(f'{mode}data/{video}', exist_ok=True)

frame_count = 0

# Loop melalui setiap frame di video
while True:
    ret, frame = cap.read()
    
    # Periksa apakah berhasil membaca frame
    if not ret:
        break

    print(f'frame_{frame_count:04d}.jpg')
    # Simpan frame ke folder
    frame_filename = os.path.join('{mode}data', video, f'frame_{frame_count:04d}.jpg')  # Ubah format nama file sesuai kebutuhan
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

# Tutup video dan selesaikan program
cap.release()
cv2.destroyAllWindows()
