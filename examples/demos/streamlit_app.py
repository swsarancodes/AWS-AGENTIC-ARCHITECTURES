import streamlit as st
from patterns.base.bedrock_client import BedrockClient

st.title("AWS Agentic Architectures Demo")

pattern = st.selectbox("Select Pattern", [
    "Reflection", "Tool Using", "ReAct", "Planning", "PEV",
    "Tree of Thoughts", "Multi-Agent", "Meta Controller", 
    "Blackboard", "Ensemble", "Memory", "Self-Improvement"
])

prompt = st.text_area("Enter your prompt:")

if st.button("Run"):
    with st.spinner("Processing..."):
        client = BedrockClient()
        result = client.invoke_model(prompt)
        st.write("**Result:**")
        st.write(result)
