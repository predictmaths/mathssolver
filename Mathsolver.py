#Complex Word Math Problem Solver App
import streamlit as st
import openai
from langchain import OpenAI, LLMMathChain
import os

openai.api_key = st.secrets['api_key']
llm = OpenAI(temperature=0)
llm_math = LLMMathChain.from_llm(llm, verbose=True)

def main():
    st.title("Complex Word Math Solver")
    #input form
    query = st.text_input("Enter your Math query:")
    execute_button = st.button("Execute")

    if execute_button:
        #Perform query and display results
        result = llm_math.run(query)
        st.write("Result:",result)

   

   

if __name__ == "__main__":
    main()
