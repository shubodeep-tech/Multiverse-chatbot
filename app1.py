import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

st.set_page_config(page_title="Multiverse of Chatbots", page_icon="🌀")
st.title(" MULTIVERSE OF CHATBOTS")


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("No GEMINI_API_KEY found. Add it to a .env file as GEMINI_API_KEY=your_key_here")
    st.stop()

client = genai.Client(api_key=api_key)

PERSONALITIES = [
    "An Expert Hacker",
    "The Gentleman Industrialist Ratan Tata",
    "The Selfish Rohit Sharma",
    "A Fast and Furious Messi",
    "The Steel Empire Builder Andrew Carnegie",
    "The AI Visionary Jensen Huang",
    "The Visionary Builder Elon Musk",
]


with st.sidebar:
    personality = st.selectbox("Who do you want to talk with?", PERSONALITIES)
    model_name = st.selectbox("Model", "gemini-2.5-flash-lite",
        model="gemini-2.5-flash")
    if st.button(" Clear chat"):
        st.session_state.messages = []
        st.rerun()



if "chats" not in st.session_state:
    st.session_state.chats = {}
if personality not in st.session_state.chats:
    st.session_state.chats[personality] = []

history = st.session_state.chats[personality]


for msg in history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


user_message = st.chat_input("Say something...")

if user_message:
    history.append({"role": "user", "content": user_message})
    with st.chat_message("user"):
        st.write(user_message)

    system_instruction = (
        f"You are acting as {personality}. Stay completely in character "
        f"in every response: tone, vocabulary, attitude, everything. "
        f"Keep replies conversational, not overly long."
    )


    contents = [system_instruction]
    for m in history:
        prefix = "User" if m["role"] == "user" else "You"
        contents.append(f"{prefix}: {m['content']}")

    with st.chat_message("assistant"):
        with st.spinner("Connecting to the multiverse..."):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents="\n".join(contents),
                )
                reply = response.text
            except Exception as e:
                reply = f" Something went wrong talking to Gemini: {e}"

        st.write(reply)

    history.append({"role": "assistant", "content": reply})