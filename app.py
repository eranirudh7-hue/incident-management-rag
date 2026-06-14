import streamlit as st
from fetching import fetch
from Generator import generate

st.title("Incident Management Assistant")

query=st.text_input("What you are looking for Today?")

if  st.button("Search") and query:  #clicking button and type qry

    docs=fetch(query)
    context = "\n\n".join([
        f"Page Content: {doc.page_content}\n"
        f"Page Number: {doc.metadata['page_label']}"
        for doc in docs
    ])
    ans=generate(context,query)
    st.subheader("Answer")
    st.json(ans.model_dump())
    
