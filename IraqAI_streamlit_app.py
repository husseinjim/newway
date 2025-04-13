# IraqAI_streamlit_app.py
import streamlit as st
import requests
import os

# إعداد الصفحة
st.set_page_config(page_title="🇶🇼 الحجية العراقية - Hajiya AI", layout="centered")
st.markdown("""
<h1 style='text-align: center;'>🇶🇼 دردشة مع الحجية العراقية</h1>
<p style='text-align: center; font-size: 15px;'>🌐 <a href='https://www.instagram.com/hajiya.iraq' target='_blank'>تابعنا على إنستغرام</a> | <a href='https://t.me/HajiyaIraq' target='_blank'>تيليجرام</a></p>
""", unsafe_allow_html=True)

# خيارات الحجية
st.divider()
purpose = st.radio(
    "🌺 شتريد من الحجية؟",
    [
        "معرفة موعد الزواج",
        "هل هذا/هذه الشخصية جيدة؟",
        "نعم أو لا"
    ],
    index=None,
    horizontal=True
)
st.divider()

# إدخال متغيرات السؤال
user_input = ""
if purpose == "معرفة موعد الزواج":
    age = st.text_input("العمر")
    education = st.text_input("الدراسة")
    location = st.text_input("من وين انتي/انته؟")
    routine = st.text_input("شو روتينك باليوم؟")
    user_input = f"عُمري {age}، دراستي {education}، ساكنة في {location}، روتيني اليومي: {routine}. متى أتزوج؟"

elif purpose == "هل هذا/هذه الشخصية جيدة؟":
    name = st.text_input("الاسم")
    height = st.text_input("الطول")
    other = st.text_input("معلومات ثانية")
    user_input = f"الاسم {name}، طوله {height}، ومعلومات إضافية: {other}. هل هو/هي جيد/ة؟"

elif purpose == "نعم أو لا":
    user_input = st.text_input("🔹 اكتب/ي سؤالك هنا:")

# أزرار
col1, col2 = st.columns([1, 5])
with col1:
    if st.button("🖊️ إرسال"):
        if user_input:
            # أرسل للنموذج
            api_key = os.getenv("OPENROUTER_API_KEY")
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "deepseek/deepseek-r1:free",
                "messages": [{"role": "user", "content": user_input}]
            }
            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
                data = response.json()
                if "choices" in data:
                    ai_reply = data["choices"][0]["message"]["content"]
                    st.success(ai_reply)
                else:
                    st.error("❌ ما كدرت ألكي رد!")
            except Exception as e:
                st.error(f"خطأ: {e}")
with col2:
    st.button("مسح المحادثة", on_click=lambda: st.experimental_rerun())
