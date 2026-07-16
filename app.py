import streamlit as st

from bedrock import ask_bedrock
from rag import retrieve_context


st.set_page_config(
    page_title="AWS GenAI Support Copilot",
    page_icon="☁️",
    layout="wide"
)


with st.sidebar:

    st.header("☁️ AWS GenAI Copilot")

    st.write(
        """
        Powered by:

        - Amazon Bedrock
        - Amazon Nova Lite
        - FAISS Vector Search
        - Python
        - Streamlit
        """
    )

    st.divider()

    st.write(
        "Version: MVP v2.0"
    )

    st.write(
        "Developed by"
    )

    st.write(
        "**Swarali Chine**"
    )



st.title(
    "☁️ AWS GenAI Support Engineer Copilot"
)


st.caption(
    "AI-powered cloud troubleshooting assistant using Amazon Bedrock + RAG"
)


st.write(
    """
    Analyze AWS errors, retrieve relevant AWS documentation,
    identify probable root causes, and generate troubleshooting workflows.
    """
)



user_input = st.text_area(
    "🔎 Paste your AWS error or question:",
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


        with st.spinner(
            "Searching AWS documentation and analyzing with Nova Lite..."
        ):


            context, sources = retrieve_context(
                user_input
            )


            response = ask_bedrock(
                user_input,
                context
            )



        st.subheader(
            "🤖 AI Analysis"
        )


        st.markdown(
            response
        )



        st.divider()



        st.subheader(
            "📚 AWS Documentation Used"
        )


        unique_sources = {}


        for source in sources:

            unique_sources[
                source["service"]
            ] = source["url"]



        for service, url in unique_sources.items():

            st.markdown(
                f"""
                ✅ **{service}**

                {url}
                """
            )



    else:

        st.warning(
            "Please enter an AWS issue before analyzing."
        )