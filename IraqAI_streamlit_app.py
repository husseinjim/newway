
import streamlit as st
import requests
import os
import random

st.set_page_config(page_title="دردشة مع الحجية العراقية", layout="centered")

st.title("🇮🇶 دردشة مع الحجية العراقية")

menu = st.sidebar.radio("اختار القسم:", ["💬 دردشة", "🍽️ وصفات", "🔮 حظك اليوم", "🙋‍♀️ اسألي الحجية"])

# ------------------------
# 1. Chat Section
# ------------------------
if menu == "💬 دردشة":
    st.markdown("**يمّه، اكتبي سؤالك هنا والحجية ترد عليك:**")
    user_input = st.text_input("✍️ سؤالك:")
    if st.button("أرسل 💌"):
        if user_input.strip() != "":
            with st.spinner("الحجية قاعدة تفكر..."):
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
                        st.error("❌ ما قدرت أجاوب، جرّبي مرة ثانية.")
                except Exception as e:
                    st.error(f"❌ صار خطأ: {e}")

# ------------------------
# 2. Recipes Section
# ------------------------
elif menu == "🍽️ وصفات":
    st.markdown("**اختاري أكلة عراقية وتعلمي طريقة تحضيرها:**")
    recipes = {
        "دولمة": "المكونات: ورق عنب، رز، لحم مفروم، بهارات...
الخطوات: ...",
        "تشريب لحم": "المكونات: لحم، خبز عراقي، بصل، طماطم...
الخطوات: ...",
        "برياني": "المكونات: رز، دجاج، بهارات برياني، بطاطا...
الخطوات: ...",
        "كبة حلب": "المكونات: برغل، لحم، بصل...
الخطوات: ...",
        "بامية": "المكونات: بامية، لحم، طماطم...
الخطوات: ...",
        "قوزي": "المكونات: رز، لحم غنم، بهارات...
الخطوات: ...",
        "مقلوبة": "المكونات: رز، باذنجان، بطاطا...
الخطوات: ...",
        "مرق السبانغ": "المكونات: سبانغ، لحم، حمص...
الخطوات: ...",
        "تشريب دجاج": "المكونات: دجاج، خبز عراقي، طماطم...
الخطوات: ...",
        "كبة موصلية": "المكونات: برغل، لحم، توابل...
الخطوات: ..."
    }
    selected = st.selectbox("اختاري أكلة:", list(recipes.keys()))
    if st.button("شوفي الوصفة 🍴"):
        st.info(recipes[selected])

# ------------------------
# 3. Luck of the Day
# ------------------------
elif menu == "🔮 حظك اليوم":
    luck = [
        "اليوم حظج حلو، استغلي الفرص يمّه ✨",
        "نامي واصحي، باجر أحسن إن شاء الله 🌙",
        "كو رزق بالطريق... استعدي له 🙏",
        "الحظ متوسط اليوم، بس انتي قدها 💪",
        "راح تسمعين خبر يفرحج 💌"
    ]
    if st.button("احسبيلي حظي اليوم ✨"):
        st.success(random.choice(luck))

# ------------------------
# 4. Yes/No Oracle
# ------------------------
elif menu == "🙋‍♀️ اسألي الحجية":
    st.markdown("**اكتبي سؤال يكون جوابه نعم أو لا:**")
    yn_question = st.text_input("🔍 سؤالك:")
    if st.button("اسألي 🧿"):
        answer = random.choice(["اي والله", "لا حبيبة الحجية", "مبين عليه نعم", "مو وقته هسة", "الله أعلم، بس إن شاء الله خير"])
        st.markdown(f"**الحجية تقول:** {answer}")
