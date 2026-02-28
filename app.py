import streamlit as st
from deep_translator import GoogleTranslator

st.title("Multi-Language Translator")

text = st.text_input("Enter a text")

languages = {
    "Uzbek 🇺🇿": "uz",
    "Russian 🇷🇺": "ru",
    "French 🇫🇷": "fr",
    "Spanish 🇪🇸": "es"
}

if text:
    st.subheader("Translations:")
    for language_name, lang_code in languages.items():
        try:
            translated = GoogleTranslator(source='auto', target=lang_code).translate(text)
            st.markdown(f"**{language_name}:** {translated}")
        except Exception as e:
            st.error(f"Error translating to {language_name}: {e}")