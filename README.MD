# 🌀 Multiverse of Chatbots

**Live Demo:** 

A Streamlit app that lets you chat with different AI personalities powered by the **Groq API**. Pick a character, type a message, and get responses in that character's voice with separate conversation memory for each personality.

## Features

* Chat-style UI (`st.chat_message` / `st.chat_input`)
* Multiple AI personalities
* Separate conversation history for each personality
* Multiple Groq models
* Clear chat button
* Error handling for missing API keys

## Requirements

* Python 3.9+
* A Groq API Key

## Setup

1. Clone this repository.

2. Install dependencies:

```bash
pip install streamlit groq python-dotenv
```

3. Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

4. Run the app:

```bash
streamlit run app1.py
```

## Available Models

* `llama-3.3-70b-versatile`
* `llama-3.1-8b-instant`
* `openai/gpt-oss-120b`

## Project Structure

```text
.
├── app1.py
├── .env
└── README.md
```
