import streamlit as st
import os
from dotenv import load_dotenv
from google import genai


st.set_page_config(page_title="Multiverse of Chatbots", page_icon="🌀")
st.title("🌀 MULTIVERSE OF CHATBOTS")


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error(" GEMINI_API_KEY not found.")
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


MODELS = [
    "models/gemini-2.5-flash-lite",
    "models/gemini-flash-lite-latest",
    "models/gemini-2.0-flash",
]


with st.sidebar:

    personality = st.selectbox(
        "Who do you want to talk with?",
        PERSONALITIES
    )

    model_name = st.selectbox(
        "Choose Gemini Model",
        MODELS,
        index=0
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.chats = {}
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

    history.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.chat_message("user"):
        st.write(user_message)

    system_instruction = f"""
You are acting as {personality}.

Stay completely in character.

Never mention that you are an AI.

Reply naturally and conversationally.
"""

    conversation = system_instruction + "\n\n"

    for m in history:
        if m["role"] == "user":
            conversation += f"User: {m['content']}\n"
        else:
            conversation += f"Assistant: {m['content']}\n"

    with st.chat_message("assistant"):

        with st.spinner("Connecting to the Multiverse..."):

            try:

                response = client.models.generate_content(
                    model=model_name,
                    contents=conversation
                )

                reply = response.text

            except Exception as e:

                reply = f"Error:\n\n{e}"

        st.write(reply)

    history.append(
        {
            "role": "assistant",
            "content": reply
        }
    )