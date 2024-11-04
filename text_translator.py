import streamlit as st
from transformers import pipeline

# Streamlit app title and description
st.title('**Language Translator**')
st.write('**Translate text from English to your desired language**')

# Text area for user input
user_text = st.text_area('**Enter text to translate:**', '')

# Define available language models with specific model names
language_models = {
    'French': 'Helsinki-NLP/opus-mt-en-fr',
    'Spanish': 'Helsinki-NLP/opus-mt-en-es',
    'German': 'Helsinki-NLP/opus-mt-en-de',
    'Italian': 'Helsinki-NLP/opus-mt-en-it',
    # 'Japanese': 'Helsinki-NLP/opus-mt-en-ja',
    'Chinese': 'Helsinki-NLP/opus-mt-en-zh',
}

# Language selection dropdown
target_language = st.selectbox('**Select target language**', list(language_models.keys()))

# Perform translation when the button is clicked
if st.button('**Translate**'):
    if user_text.strip() == '':
        st.write('**Please enter text to translate**')
    else:
        # Load the correct model for the selected language
        model_name = language_models[target_language]
        translator = pipeline(task="translation", model=model_name)
        
        # Perform translation
        translation = translator(user_text)[0]['translation_text']
        
        # Display the translated text
        st.write('**Translated Text:**')
        st.write(f'**{translation}**')
