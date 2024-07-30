import streamlit as st
from auth import verify_user
from captcha import generate_captcha, check_captcha

def login_page():
    st.title("Halaman Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Menghasilkan CAPTCHA jika belum ada
    if "generated_captcha" not in st.session_state:
        st.session_state["generated_captcha"] = generate_captcha()
    
    generated_captcha = st.session_state["generated_captcha"]

    st.markdown(f"<b>CAPTCHA:</b> {generated_captcha}", unsafe_allow_html=True)
    input_captcha = st.text_input("Masukkan CAPTCHA")

    if st.button("Login"):
        # Memeriksa CAPTCHA
        if not check_captcha(input_captcha, generated_captcha):
            st.error("CAPTCHA salah")
        # Memeriksa username dan password
        elif verify_user(username, password):
            st.success("Login berhasil!")
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            # Hapus CAPTCHA setelah berhasil login
            del st.session_state["generated_captcha"]
            try:
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error during rerun: {e}")
        else:
            st.error("Username atau password salah")

if __name__ == "__main__":
    login_page()
