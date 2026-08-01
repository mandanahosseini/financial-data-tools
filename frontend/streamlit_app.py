import streamlit as st
import requests


st.set_page_config(
    page_title="Financial AI Assistant",
    page_icon="💰"
)


st.title(
    "💰 Financial AI Assistant"
)


st.write(
    """
    Ask questions about financial documents
    using an AI-powered RAG assistant.
    """
)


question = st.text_input(
    "Enter your financial question:"
)


if st.button("Ask"):

    if question:

        response = requests.post(
            "http://localhost:8000/ask",
            json={
                "question": question
            }
        )


        if response.status_code == 200:

            answer = response.json()["answer"]

            st.success(answer)

        else:

            st.error(
                "API Error"
            )