import streamlit as st
import ollama

st.title('My Custom AI Interface')

if 'messages' not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m['role']):
        st.write(m['content'])

if p := st.chat_input('Say something...'):
    st.session_state.messages.append({'role': 'user', 'content': p})
    with st.chat_message('user'):
        st.write(p)
    with st.chat_message('assistant'):
        msg = st.empty()
        full = ''
        try:
            for chunk in ollama.chat(model='llama3', messages=st.session_state.messages, stream=True):
                full += chunk['message']['content']
                msg.markdown(full)
        except:
            st.error('Make sure Ollama is open and running!')
    st.session_state.messages.append({'role': 'assistant', 'content': full})