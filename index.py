import streamlit as st
import os

def homepage():
    st.title("Selamat datang di halaman utama!")

def camera_scan_page():
    st.title("Halaman Pemindaian Kamera")
    # Tambahkan logika halaman pemindaian kamera di sini

def gallery_and_details_page():
    st.title("Galeri Foto & Rincian")
    image_dir = "path/to/your/image_directory"  # Sesuaikan dengan direktori gambar Anda

    images = os.listdir(image_dir)
    cols = st.columns(4)  # Menggunakan 4 kolom untuk tata letak galeri

    for idx, image in enumerate(images):
        if image.endswith(('.jpg', '.jpeg', '.png')):
            with cols[idx % 4]:
                image_path = os.path.join(image_dir, image)
                st.image(image_path, caption=image, use_column_width=True, classes="square-image")
                st.button("Detail gambar", key=f"detail_{image}")
                if st.button("Hapus gambar", key=f"hapus_{image}"):
                    os.remove(image_path)
                    st.experimental_rerun()  # Reload halaman untuk memperbarui galeri

# Jalankan fungsi utama jika file ini dijalankan langsung
if __name__ == "__main__":
    gallery_and_details_page()
