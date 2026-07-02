!pip install -q streamlit pyngrok google-generativeai
%%writefile app.py

import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["AQ.Ab8RN6IUrSXVxgTWa96UZNSKdLSNA68pl1sth_9W3StPIDwjeA"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="AI Learning Buddy Sindhu", page_icon="🎓")

st.title("🎓 AI Learning Buddy Sindhu")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if topic == "":
        st.warning("Please enter a topic.")
    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic} with answers."

        else:
            prompt = topic

        response = model.generate_content(prompt)

        st.write(response.text)
!nohup streamlit run app.py --server.port 8501 &
import time
time.sleep(10)
!cat nohup.out
!pip install -q pyngrok
from pyngrok import ngrok
ngrok.set_auth_token(st.secrets["3FrBNzcGLHxCu0wO0kROA0R9dtY_FC6MLcZBgz8gdHsCvLuk"])
public_url = ngrok.connect(8501)

print(public_url)
