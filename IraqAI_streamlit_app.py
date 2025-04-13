import streamlit as st
import requests
import os

# إعداد الصفحة
st.set_page_config(page_title="Iraq AI – دردشة مع الحجية العراقية", layout="centered")
st.title("🇮🇶 Iraq AI – دردشة مع الحجية العراقية")

# رابط تابعنا
st.markdown("[📸 تابعنا على إنستغرام](https://www.instagram.com/hajiya.iraq) | [💬 تابعنا على تيليجرام](https://t.me/HajiyaIraq)", unsafe_allow_html=True)

# صندوق السؤال
user_input = st.text_input("✍️ اكتبي سؤالك هنا:", placeholder="مثلاً: شنو رأيك بهالشاب؟")

# خيارات "قراءة الفنجان"
mood = st.radio("🔮 قراءة الفنجان (اختياري):", ["لا أريد", "احجيلي عن حظي", "راح يرجع؟", "أكدر أثق بي؟", "نعم أو لا؟"])

# زر الإرسال
if st.button("🚀 أرسل"):
    if not user_input.strip():
        st.warning("يرجى كتابة سؤال.")
    else:
        # نص الطلب المُرسل
        full_prompt = f"""
أنت شخصية الحجية أم فوزي. امرأة عراقية كبيرة بالعمر، تحب تنصح، تنكت، وتتكلم باللهجة العراقية. تجاوب دائماً بطريقة شعبية طريفة، لكن بيها حكمة ودفء.

إذا المستخدم اختار قراءة فنجان، اضف لمستك كقارئة فنجان شعبية وتكلمي كأنك تشوفين الفنجان:

اختيار المستخدم لقراءة الفنجان: {mood}
سؤال المستخدم: {user_input}
"""

        # إرسال الطلب إلى OpenRouter
        api_key = os.getenv("OPENROUTER_API_KEY")
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek/deepseek-r1:free",
            "messages": [{"role": "user", "content": full_prompt}]
        }

        try:
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
            data = response.json()

            if "choices" in data:
                ai_reply = data["choices"][0]["message"]["content"]
                st.success(ai_reply)
            else:
                st.error("❌ لم يتم العثور على رد من النموذج.")
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
