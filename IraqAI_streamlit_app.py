import streamlit as st
import requests
import os
import random

st.set_page_config(page_title="دردشة مع الحجّية العراقية 🇮🇶", layout="centered")
st.title("🇮🇶 دردشة مع الحجّية العراقية – Hajiya AI")

# 💬 الشات
st.header("💬 دردش ويّا الحجّية")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("اكتب سؤالك هنا", key="user_input", placeholder="شلون حظي اليوم؟")

if st.button("✉️ أرسل"):
    if user_input:
        st.session_state.chat_history.append(("أنت", user_input))

        # إعداد الاتصال بـ OpenRouter
        api_key = os.getenv("OPENROUTER_API_KEY")
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek/deepseek-r1:free",
            "messages": [
                {"role": "system", "content": "أنت الحجّية العراقية، تجاوب بطريقة شعبية عراقية وبأسلوب لطيف."},
                {"role": "user", "content": user_input}
            ]
        }

        try:
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
            data = response.json()
            ai_reply = data['choices'][0]['message']['content']
            st.session_state.chat_history.append(("الحجّية", ai_reply))
        except Exception as e:
            st.session_state.chat_history.append(("الحجّية", f"صار خلل: {e}"))

# عرض المحادثة
for speaker, message in st.session_state.chat_history[::-1]:
    with st.chat_message(name=speaker):
        st.markdown(message)

# 🍲 وصفات أكلات عراقية
st.divider()
st.header("🍲 وصفات أكلات عراقية")
recipes = {
    "البرياني": "رز، لحم أو دجاج، خضار مشكلة، بهارات برياني.",
    "الدولمة": "ورق عنب، رز، لحم مفروم، بهارات، طماطم.",
    "القوزي": "لحم خروف، رز، مكسرات، بهارات مشكلة.",
    "التمن الأحمر": "رز، معجون طماطم، لحم، بهارات عراقية.",
    "كبة حلب": "برغل، لحم مفروم، بصل، بهارات.",
    "كباب عراقي": "لحم مفروم، دهن، بقدونس، بصل.",
    "مرقة باميا": "باميا، لحم، طماطم، بهارات.",
    "تشريب لحم": "لحم بالعظم، خبز عراقي، مرق.",
    "كباب طاوة": "دجاج أو لحم مفروم، صوص أحمر، بطاطا.",
    "قيمة نجفية": "لحم مفروم، حمص مجروش، بصل، بهارات."
}
selected_recipe = st.selectbox("اختار أكلة وشوف طريقتها:", list(recipes.keys()))
st.info(recipes[selected_recipe])

# 🌟 حظّك اليوم
st.divider()
st.header("🌟 حظّك اليوم ويّا الحجّية")
if st.button("شوف حظي"):
    fortune = random.choice([
        "اليوم يومك، شوية صبر وباچر أحلى!",
        "كوّن حذر من الناس اللي تضحك بوجهك واجد.",
        "عندك خبر حلو قريباً، تفائل ✨",
        "اليوم عادي، بس لا تخلي أحد يعكر مزاجك.",
        "حظك قوي إذا تتوكل على ربك وتشتغل."
    ])
    st.success(f"🔮 {fortune}")

# ❓ سؤال نعم أو لا
st.divider()
st.header("❓ اسأل الحجّية سؤال نعم أو لا")
yes_no_q = st.text_input("اكتب سؤالك هنا (نعم/لا)", key="yes_no")
if st.button("🔮 جاوبيني"):
    if yes_no_q:
        yn_answer = random.choice(["نعم", "لا", "يمكن", "مو أكيد", "رجع اسألني باچر 😄"])
        st.warning(f"💬 الحجّية: {yn_answer}")
        
