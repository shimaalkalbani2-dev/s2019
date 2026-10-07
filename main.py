import streamlit as st

st.title("🤖 مساعد الذكاء الاصطناعي")
st.write("مرحباً بك! هذه واجهة مستخدم بسيطة تم إنشاؤها باستخدام Streamlit.")

user_input = st.text_input("أدخل سؤالك أو نصك هنا:")

if st.button("إرسال"):
    if user_input:
        st.success(f"تم استقبال النص بنجاح: {user_input}")
    else:
        st.warning("يرجى كتابة نص قبل الضغط على زر الإرسال.")
