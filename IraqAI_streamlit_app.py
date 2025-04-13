
import streamlit as st
import requests

st.set_page_config(page_title="Iraq AI - دردش مع شخصية عراقية 🇮🇶")

st.title("🇮🇶 Iraq AI - دردش مع شخصية عراقية")

characters = ["الحجية أم فوزي", "العسكري أبو سيف", "اليوتيوبر حسون تيك", "الشاب منتظر", "الطالبة زينب"]
selected_character = st.selectbox("🧕🏽 اختار شخصية", characters)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if st.button("🧹 مسح المحادثة"):
    st.session_state.chat_history = []

question = st.text_input("✍️ اكتب سؤالك هنا")

headers = {
    'Authorization': f'Bearer {st.secrets["OPENROUTER_API_KEY"]}',
    'Content-Type': 'application/json',
}

if st.button("🚀 أرسل"):
    with st.spinner('جارٍ الحصول على الرد...'):
        data = {
            'model': 'deepseek/deepseek-r1:free',
            'messages': [
                {"role": "system", "content": f"تحدث بأسلوب عراقي شعبي كشخصية {selected_character}"},
                {"role": "user", "content": question}
            ]
        }

        response = requests.post('https://openrouter.ai/api/v1/chat/completions', json=data, headers=headers)

        if response.status_code == 200:
            answer = response.json()['choices'][0]['message']['content']
            st.session_state.chat_history.append((selected_character, question, answer))
        else:
            st.error("❌ هناك خطأ في استجابة النموذج")

for char, q, a in reversed(st.session_state.chat_history):
    st.markdown(f"**{char}:** {q}")
    st.markdown(f"🔸 {a}")

st.markdown("[📸 تابعنا على إنستغرام](https://www.instagram.com/husseinsaad.iq/)")
