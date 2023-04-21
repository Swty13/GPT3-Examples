import openai
import time
import streamlit as st
from streamlit_pills import pills
openai.api_type = "XXXXXXXXXXX"
openai.api_base = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
openai.api_version = "XXXXXXXXXXXXXX"
openai.api_key = "XXXXXXXXXXXXXXXXXXXXX"


st.subheader("OpenAI `stream` *argument*")
selected = pills("", ["NO Streaming", "Streaming"], ["🎈", "🌈"])
start_time = time.time()
user_input = st.text_input("You: ",placeholder = "Ask me anything ...", key="input")

if st.button("Submit", type="primary"):
    st.markdown("----")
    res_box = st.empty()
    if selected == "Streaming":
        report = []
        for resp in openai.Completion.create( engine="text-davinci-003",
                                            prompt=user_input,
                                            max_tokens=1000, 
                                            temperature = 0.5,
                                            stream = True):
            # join method to concatenate the elements of the list 
            # into a single string, 
            # then strip out any empty strings
            report.append(resp.choices[0].text)
            result = "".join(report).strip()
            result = result.replace("\n", "")        
            res_box.markdown(f'*{result}*') 
            
    else:
        completions = openai.Completion.create(engine="text-davinci-003",
                                            prompt=user_input,
                                            max_tokens=1000, 
                                            temperature = 0.5,
                                            stream = False)
        result = completions.choices[0].text
        
        res_box.write(result)
        
end_time = time.time()
execution_time = end_time - start_time
st.write(f"Total execution time: {execution_time:.2f} seconds")
st.markdown("----")

##to run this file excute this command:streamlit run stream_run.py