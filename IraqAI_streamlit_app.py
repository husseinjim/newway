
import streamlit as st
import requests
import os

st.set_page_config(page_title="🇮🇶 Iraq AI - دردش مع شخصية عراقية", layout="centered")
st.markdown("<h1 style='text-align: center;'>🇮🇶 Iraq AI - دردش مع شخصية عراقية</h1>", unsafe_allow_html=True)

characters = {
    "الحجّية أم فوزي": "أنت حجّية عراقية، تحكين بحنية وبساطة، تستخدمين أمثال شعبية وتنصحين وكأنك أم للكل.",
    "العسكري أبو سيف": "أنت عسكري عراقي، صارم وجاد، تتحدث بكلمات مباشرة وأسلوب مختصر.",
    "اليوتيوبر حسون تيك": "أنت شاب عراقي عصري، تتحدث بسرعة وحماسة، وتستخدم مصطلحات التكنولوجيا والسوشيال ميديا.",
    "الشاب منتظر": "أنت شاب من بغداد، تحچي باللهجة الشعبية وبأسلوب عفوي ومضحك.",
    "الطالبة زينب": "أنت طالبة جامعية ذكية ومنظمة، تحبين التحليل المنطقي والنقاش الهادئ."
}

selected_character = st.selectbox("👤 اختر شخصية:", list(characters.keys()))
user_input = st.text_input("🗨️ اكتب سؤالك هنا:", placeholder="مثلاً: شنو رأيك بالحياة؟")

if st.button("🚀 أرسل"):
    if user_input:
        with st.spinner("✍️ جاري توليد الرد..."):
            api_key = os.getenv("OPENROUTER_API_KEY")
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            system_prompt = characters[selected_character]
            payload = {
                "model": "deepseek/deepseek-r1:free",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            }
            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
                result = response.json()
                if "choices" in result and result["choices"]:
                    reply = result["choices"][0]["message"]["content"]
                    st.success(f"👤 {selected_character}:\n\n{reply}")
                else:
                    st.error("❌ لم يتم العثور على رد من النموذج.")
            except Exception as e:
                st.error(f"❌ حدث خطأ: {e}")
    else:
        st.warning("الرجاء كتابة سؤال أولاً.")

# Clear session
if st.button("🧹 مسح المحادثة"):
    st.session_state.clear()
    st.experimental_rerun()

# Instagram follow
st.markdown("[📸 تابعنا على إنستغرام](https://www.instagram.com/husseinsaad.iq/)")
