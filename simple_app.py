import streamlit as st
import base64
from pathlib import Path

# Настройка страницы
st.set_page_config(
    page_title="",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Скрываем все элементы Streamlit и делаем видео на весь экран
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    .reportview-container .main .block-container {padding: 0; margin: 0;}
    .reportview-container .main {padding: 0; margin: 0;}
    .stApp {padding: 0; margin: 0;}
    .main .block-container {padding: 0; margin: 0;}
    body {margin: 0; padding: 0;}
</style>
""", unsafe_allow_html=True)

# Функция для создания HTML с видео на весь экран
def get_video_html(video_path):
    with open(video_path, "rb") as f:
        video_bytes = f.read()
    
    video_base64 = base64.b64encode(video_bytes).decode()
    
    html_code = f"""
    <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; background: black;">
        <div style="position: absolute; top: 20px; left: 0; width: 100%; text-align: center; z-index: 10000;">
            <h1 style="color: white; font-size: 24px; text-shadow: 2px 2px 4px #000000;">НАЖМИТЕ НА ЧЕРНЫЙ ЭКРАН</h1>
        </div>
        <video 
            width="100%" 
            height="100%" 
            autoplay 
            muted 
            loop
            style="object-fit: cover;"
            onloadeddata="this.muted=false; this.play();"
            oncanplay="this.muted=false; this.play();"
            onclick="this.muted=false; this.play();"
        >
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const video = document.querySelector('video');
            if (video) {{
                video.muted = false;
                video.play();
                // Принудительно включаем звук через 1 секунду
                setTimeout(function() {{
                    video.muted = false;
                    video.play();
                }}, 1000);
            }}
        }});
        
        // Обработчик клика для включения звука
        document.addEventListener('click', function() {{
            const video = document.querySelector('video');
            if (video) {{
                video.muted = false;
                video.play();
            }}
        }});
    </script>
    """
    return html_code

# Проверяем наличие видео файла
video_path = "Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster).mp4"

if Path(video_path).exists():
    video_html = get_video_html(video_path)
    st.components.v1.html(video_html, height=1000)
else:
    st.error("Видео файл не найден!") 