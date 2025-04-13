
import streamlit as st
import requests
import random
import os

st.set_page_config(page_title="دردشة مع الحجّية العراقية", layout="centered")

st.markdown("""
# 🇮🇶 دردشة مع الحجّية العراقية
👵 أهلاً بكم ويّا الحجّية أم فوزي! اسألها عن يومك، الحظ، أو اختار من خدماتها الأخرى.

[تابعنا على إنستغرام](https://www.instagram.com/hajiya.iraq) | [تابعنا على تيليجرام](https://t.me/HajiyaIraq)
""", unsafe_allow_html=True)

# Chat box UI like WhatsApp
if 'messages' not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("اكتب سؤالك هنا للحجّية")

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


with st.container():
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"<div style='text-align:right;background-color:#dcf8c6;padding:10px;border-radius:10px;margin:5px;'>{msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align:left;background-color:#fff;padding:10px;border-radius:10px;margin:5px;border:1px solid #ccc'>{msg['content']}</div>", unsafe_allow_html=True)

# Fun side features
st.divider()
st.markdown("## 🍲 وصفات أكلات عراقية")
if st.button("أظهر 10 وصفات مشهورة"):
    recipes = {
        "دولمة": "المكونات: ورق عنب، رز، لحم مفروم، بهارات.
الخطوات:
1. نخلط الحشو.
2. نلف الورق.
3. نطبخ على نار هادئة لمدة ساعة.
4. نقدّم مع ليمون.",
        "تشريب": "المكونات: خبز عراقي، لحم، طماطم.
الخطوات:
1. نحمّر اللحم.
2. نطبخ الصلصة.
3. نغمس الخبز بالمرق.
4. يُقدّم ساخنًا.",
        "قيمة": "المكونات: حمص مجروش، لحم، بصل.
الخطوات:
1. نطبخ الحمص.
2. نضيف اللحم.
3. نهرس المزيج.
4. يُقدّم مع خبز.",
        "برياني": "المكونات: رز، دجاج، بهارات برياني.
الخطوات:
1. نطبخ الدجاج.
2. نغلي الرز نصف سلقة.
3. ندمجهم بالبهارات ونُكمل الطهي.",
        "كبة حلب": "المكونات: برغل، لحم، بصل.
الخطوات:
1. نحضر عجينة الكبة.
2. نُشكّلها ونحشيها.
3. نقلي حتى تتحمّر.",
        "كباب": "المكونات: لحم مفروم، بهارات، بصل.
الخطوات:
1. نخلط المكونات.
2. نشكّل على أعواد.
3. نشوي على الفحم.",
        "مرقة باميا": "المكونات: باميا، لحم، طماطم.
الخطوات:
1. نحمّر اللحم.
2. نضيف الباميا والطماطم.
3. نطبخ على نار هادئة.",
        "تمن أحمر": "المكونات: رز، معجون طماطم، مرق.
الخطوات:
1. نقلي الرز.
2. نضيف المعجون والمرق.
3. نغطي ونتركه حتى ينضج.",
        "قوزي": "المكونات: لحم غنم، رز، بهارات.
الخطوات:
1. نطبخ اللحم.
2. نعدّ الرز بالبهارات.
3. نُقدّمهم معًا.",
        "شوربة عدس": "المكونات: عدس، جزر، بصل.
الخطوات:
1. نغلي العدس.
2. نضيف الخضار.
3. نهرس الخليط ونقدّمه ساخن."
    }
    for title, steps in recipes.items():
        st.markdown(f"**{title}**

{steps}")

st.divider()
st.markdown("## 🎯 حظّك اليوم")
if st.button("اضغط لتعرف حظك اليوم!"):
    luck_messages = [
        "اليوم عندج حظ قوي جدًا! 🍀",
        "الحجّية تكول ديري بالك، خليك حذرة شوي!",
        "فرصة حلوة بالطريق، لا تضيعينها!",
        "انتبهي من شخص يحاول يزعلك.",
        "الحظ متوسط اليوم، بس مزاجج حلو راح يساعدك."
    ]
    st.success(random.choice(luck_messages))

st.divider()
st.markdown("## ❓ سؤال نعم أو لا")
yes_no_q = st.text_input("اكتبي سؤال تنين عليه جواب نعم أو لا:")
if st.button("اسألي الحجّية"):
    if yes_no_q:
        st.info(f"🔮 الحجّية تكول: {'نعم' if random.choice([True, False]) else 'لا'}")
