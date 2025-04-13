import streamlit as st
import requests
import random
import os

st.set_page_config(page_title="دردشة مع الحجّية العراقية", layout="centered")

st.markdown("""
# 🇮🇶 دردشة مع الحجّية العراقية
👵 أهلاً بكم ويّا الحجّية أم فوزي! اسألها عن يومك، الحب، الحظ، أو شوفي وصفات أكلات عراقية.

[تابعنا على إنستغرام](https://www.instagram.com/hajiya.iraq) | [تابعنا على تيليجرام](https://t.me/HajiyaIraq)
""", unsafe_allow_html=True)

# Chat state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Chat input box
user_input = st.chat_input("اكتبي سؤالك هنا للحجّية")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

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
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        else:
            st.session_state.messages.append({"role": "assistant", "content": "❌ الحجّية ما فهمت السؤال."})
    except Exception as e:
        st.session_state.messages.append({"role": "assistant", "content": f"❌ صار خطأ: {e}"})


# Display chat messages
with st.container():
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f"<div style='text-align:right;background-color:#dcf8c6;padding:10px;border-radius:10px;margin:5px;'>{msg['content']}</div>",
                unsafe_allow_html=True)
        else:
            st.markdown(
                f"<div style='text-align:left;background-color:#fff;padding:10px;border-radius:10px;margin:5px;border:1px solid #ccc'>{msg['content']}</div>",
                unsafe_allow_html=True)

# وصفات أكلات عراقية
st.divider()
st.markdown("## 🍲 وصفات أكلات عراقية")

if st.button("أظهر 10 وصفات مشهورة"):
    recipes = {
        "دولمة": """المكونات: ورق عنب، رز، لحم مفروم، بهارات، بصل، معجون طماطة، دبس رمان.
1. نغسل الرز ونخلطه مع اللحم والبصل المفروم والبهارات والمعجون.
2. نلف الورق بالحشوة ونرتبه في قدر.
3.
