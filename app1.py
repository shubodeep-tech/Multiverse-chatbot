import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

st.set_page_config(page_title="Multiverse of Chatbots", page_icon="🌀")
st.title("MULTIVERSE OF CHATBOTS")

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found.")
    st.stop()

client = Groq(api_key=api_key)

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
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "openai/gpt-oss-120b",
]

with st.sidebar:
    personality = st.selectbox(
        "Who do you want to talk with?",
        PERSONALITIES
    )
    model_name = st.selectbox(
        "Choose Model",
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
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {
                            "role": "system",
                            "content": system_instruction
                        },
                        {
                            "role": "user",
                            "content": conversation
                        }
                    ]
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"Error:\n\n{e}"

            st.write(reply)

    history.append(
        {
            "role": "assistant",
            "content": reply
        }
    )