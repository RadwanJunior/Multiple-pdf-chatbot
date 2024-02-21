import streamlit as st
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    #Header of page
    st.header("Chat with multiple PDFs :books:")
    #Text area for user to ask questions
    st.text_input("Ask a question about your documents:")

    #sidebar (use with to put things inside it)
    with st.sidebar:
        st.subheader("Your documents")
        #add a streamlit element
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            
            #get pdf text

            # get the text chunks

            #create vector store




if __name__ == "__main__":
    main()