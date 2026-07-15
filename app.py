import streamlit as st

from bedrock import ask_bedrock


st.set_page_config(
    page_title="AWS GenAI Support Copilot",
    page_icon="☁️",
    layout="wide"
)


with st.sidebar:
    st.header("AWS GenAI Copilot")

    st.write("Powered by:")
    st.write("- Amazon Bedrock")
    st.write("- Amazon Nova Lite")
    st.write("- Python")
    st.write("- Streamlit")

    st.divider()

    st.write("Version: MVP v1.0")
    st.write("Developed by")
    st.write("Swarali Chine")


st.title("AWS GenAI Support Engineer Copilot")

st.write(
    "☁️ AI-powered cloud troubleshooting assistant using Amazon Bedrock + Nova Lite"
)


st.write(
    """
    Analyze AWS errors, identify probable root causes,
    and generate troubleshooting workflows with AWS CLI guidance.
    """
)


user_input = st.text_area(
    "Paste your AWS error or question:",
    height=180,
    placeholder="""
Example:

My EC2 instance is unreachable.
System status check failed.

How do I troubleshoot?
"""
)


if st.button("🚀 Analyze Issue"):

    if user_input.strip():

        with st.spinner("Analyzing with Amazon Nova Lite..."):

            response = ask_bedrock(
                f"""
You are a Senior AWS Support Engineer.

Analyze this AWS issue:

{user_input}

Provide your response using this format:

## Summary

## Root Cause

## Troubleshooting Steps

## AWS CLI Commands

## Recommended Fix
"""
            )

        st.subheader("AI Analysis")

        st.markdown(response)

    else:
        st.warning(
            "Please enter an AWS issue before analyzing."
        )