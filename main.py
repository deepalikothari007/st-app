import streamlit as st

def main():
    st.title('RAG System')
    
    user_input = st.text_input("Please enter your query", "")
    num_chunks = st.number_input("Enter the number of chunks", min_value=1, value=1, step=1)
    
    if st.button('Submit'):
        if user_input:
            st.write(f'You asked: {user_input}')
            st.write(f'Number of chunks: {num_chunks}')
            st.write('Here is your response: ...')  # Add your response logic here
        else:
            st.write('Please enter a query.')

if __name__ == "__main__":
    main()