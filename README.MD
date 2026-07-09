LIVE DEMO: https://app1py-vciqoyehjtklwzuapvqxux.streamlit.app/

# 🌀 Multiverse of Chatbots

A Streamlit app that lets you chat with different AI personalities powered by Google's Gemini API. Pick a character, type a message, and get a response fully in that character's voice — with conversation memory per personality.




## Features

- Chat-style UI (`st.chat_message` / `st.chat_input`)
- Separate conversation history per personality — switch characters without losing either chat
- Choice of Gemini model (`gemini-2.5-flash` or `gemini-2.5-pro`)
- Clear chat button
- Graceful error handling for missing API keys or failed requests

## Requirements

- Python 3.9+
- A Google Gemini API key ([get one here](https://aistudio.google.com/apikey))

## Setup

1. **Clone or download this project**, then move into the folder.

2. **Install dependencies:**

   ```bash
   pip install streamlit google-genai python-dotenv
   ```

3. **Create a `.env` file** in the same folder as the script, with your API key:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the app:**

   ```bash
   streamlit run multiverse_chatbot_v2.py
   ```

5. Streamlit will open the app in your browser (usually at `http://localhost:8501`).

## Usage

1. Pick a personality from the sidebar (e.g. "An expert Hacker").
2. Type a message in the chat box at the bottom and press Enter.
3. The AI responds in character. Keep chatting — it remembers earlier turns in the conversation.
4. Switch personalities anytime from the sidebar; each one keeps its own separate chat history.
5. Use **🗑️ Clear chat** in the sidebar to wipe the current personality's history.

## Project structure

```
.
├── multiverse_chatbot_v2.py   # Main Streamlit app
├── .env                       # Your API key (not committed to git)
└── README.md
```

## Adding a new personality

Open the script and add a new entry to the `PERSONALITIES` list:

```python
PERSONALITIES = [
    "An expert Hacker",
    "The Selfish Rohit Sharma",
    "A fast and Furious Messi",
    "Your New Character Here",
]
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `No GEMINI_API_KEY found` error | Make sure `.env` exists in the same folder and contains `GEMINI_API_KEY=...` |
| App won't start | Confirm `streamlit`, `google-genai`, and `python-dotenv` are installed |
| Slow or failed responses | Try switching to `gemini-2.5-flash` in the sidebar, or check your API quota |

## License

Personal / educational project — use freely.
