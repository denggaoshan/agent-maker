"""Demo of the web interface of the chatbot."""
import os

import streamlit as st
from agent import Agent
from common import Message

st.set_page_config(
    page_title="Agent Maker 🎈",
    layout='wide'
)


selected = st.sidebar.selectbox(
    'Select a robot',
    options=[robot[:-5] for robot in os.listdir('./agents') if robot.endswith('.toml')]
)

# Reload the agent only if the user selects a different agent
if "agent" not in st.session_state or st.session_state.agent.config_path != f'./agents/{selected}.toml':
    st.session_state.clear()
    st.session_state.agent = Agent.build_from_toml(f'./agents/{selected}.toml')

st.title(f"💬 {st.session_state.agent.name}")

with open(st.session_state.agent.config_path, 'r', encoding='utf-8') as f:
    st.sidebar.code(f.read())

if "messages" not in st.session_state:
    msgs = []
    if st.session_state.agent.greeting:
        msgs.append(Message(speaker=st.session_state.agent.role_assistant, content=st.session_state.agent.greeting))
    st.session_state["messages"] = msgs

for msg in st.session_state.messages:
    role, content = msg.get_chat_message()
    st.chat_message(role).write(content)

if user_input := st.chat_input():
    st.session_state.messages.append(
        Message(speaker=st.session_state.agent.role_user, content=user_input, is_user=True)
    )
    st.chat_message("user").write(user_input)
    response = st.session_state.agent.chat(st.session_state.messages)
    msg = Message.from_str(response, is_user=False)
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
