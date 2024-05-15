import streamlit as st
from transformers import pipeline

# Nama model yang tepat
model_name = "ranggaaldosas/llama-8b"

# Mencoba memuat model dengan pipeline text-generation
try:
    model = pipeline("text-generation", model=model_name)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Membuat interface Streamlit
st.title("Generate Text with LLaMA-8B")
input_text = st.text_input("Enter your text:")

if st.button("Generate"):
    try:
        # Generate text menggunakan model
        output = model(
            input_text, max_length=50
        )  # Sesuaikan parameter sesuai kebutuhan
        st.write(output[0]["generated_text"])
    except Exception as e:
        st.error(f"Error generating text: {e}")
