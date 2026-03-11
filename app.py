import streamlit as st
import requests
import time

# Page config
st.set_page_config(
    page_title="Personal AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
<style>

.main {
    background: #020024;
    background: linear-gradient(90deg, rgba(2, 0, 36, 1) 2%, rgba(9, 9, 121, 1) 11%, rgba(0, 212, 255, 1) 61%);
}

.block-container {
    padding-top: 2rem;
}

.assistant-card {
    background: #4840C2;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
}

.chat-user {
    background-color: #2E44F0;
    padding: 12px;
    border-radius: 10px;
}

.chat-assistant {
    background-color: #F04E2E;
    padding: 12px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.title("🤖 Assistant Panel")

    st.markdown("---")

    st.subheader("Quick Actions")

    if st.button("📅 Schedule Meeting"):
        st.info("Type: Schedule meeting tomorrow at 10 AM")

    if st.button("📧 Summarize Emails"):
        st.info("Type: Summarize my emails")

    if st.button("📝 Add Task"):
        st.info("Type: Add task 'Finish report'")

    if st.button("💰 Track Expense"):
        st.info("Type: Add expense 500 for groceries")

    st.markdown("---")

    st.caption("Built with Streamlit + n8n")


# Title section
st.title("🤝 Your Personal Assistant")

st.markdown(
"""
<div class="assistant-card">

### What can your assistant do?

- Answer questions on various topics  
- Arrange calendar events and meetings  
- Read and summarize your emails  
- Manage tasks and to-do lists  
- Take quick notes  
- Track expenses and budgeting  

</div>
""",
unsafe_allow_html=True
)


st.subheader("💬 Chat with your assistant")


# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat history
for message in st.session_state.messages:

    if message["role"] == "user":
        with st.chat_message("user", avatar="🧑"):
            st.markdown(
                f'<div class="chat-user">{message["content"]}</div>',
                unsafe_allow_html=True
            )

    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(
                f'<div class="chat-assistant">{message["content"]}</div>',
                unsafe_allow_html=True
            )


# Chat input
user_message = st.chat_input("Ask your assistant anything...")


if user_message:

    # Display user message
    with st.chat_message("user", avatar="🧑"):
        st.markdown(
            f'<div class="chat-user">{user_message}</div>',
            unsafe_allow_html=True
        )

    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )


    # Loading spinner
    with st.spinner("Assistant is thinking..."):

        response = requests.post(
            "http://localhost:5678/webhook/", # Add production URL here
            json={"message": user_message}
        )

        time.sleep(1)

        ai_response = response.json()[0]["output"]


    # Display assistant response
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(
            f'<div class="chat-assistant">{ai_response}</div>',
            unsafe_allow_html=True
        )

    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )