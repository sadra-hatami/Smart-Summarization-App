import streamlit as st
from transformers import pipeline

# ۱. شخصی‌سازی ظاهر صفحه
st.set_page_config(page_title="خلاصه‌ساز هوشمند فارسی", page_icon="📝")

# ۲. تابع بارگذاری مدل با قابلیت Cache (برای سرعت بالاتر در اجراهای بعدی)
@st.cache_resource
def load_ai_model():
    model_name = "m3hrdadfi/t5-base-parsbert-summarization"
    return pipeline("summarization", model=model_name, tokenizer=model_name)

# ۳. طراحی رابط کاربری
st.title("🤖 خلاصه‌ساز متن با هوش مصنوعی")
st.markdown("متن طولانی‌تون رو در باکس زیر وارد کنید تا هوش مصنوعی کوتاه‌ترین و دقیق‌ترین نسخه اون رو بهتون تحویل بده.")

# ۴. باکس دریافت ورودی
user_input = st.text_area("متن فارسی را اینجا وارد کنید:", height=250)

# ۵. دکمه پردازش
if st.button("خلاصه‌سازی کن"):
    if user_input.strip():
        with st.spinner('در حال تحلیل و پردازش متن...'):
            try:
                summarizer = load_ai_model()
                # تنظیم پارامترهای خلاصه سازی
                result = summarizer(user_input, max_length=150, min_length=40, do_sample=False)
                
                st.success("✅ نتیجه نهایی:")
                st.info(result[0]['summary_text'])
            except Exception as e:
                st.error(f"خطایی رخ داد: {e}")
    else:
        st.warning("لطفاً ابتدا متنی را برای پردازش وارد کنید.")