import os

import openai
import streamlit as st


# thesoothsayeria.com

def main():
    build_header()
    
    tech_name = ask_for_tech_input()

    if tech_name:
        with st.spinner(text=f'Asking GPT-3 about the future of {tech_name}...'):
            prediction = request_future(tech_name)
        print_prediction(prediction)


def build_header():
    st.header('SOOTHS-AI-R :crystal_ball:')
    st.markdown('You can now ask AI about the future!')
    st.markdown('There is a rumour that GPT-3 is so smart because it has a data feed directly from the future. What do you think, can GPT-3 predict the future?')


def ask_for_tech_input():
    col1, col2, col3 = st.columns(3)
    col1.markdown('##')
    col1.markdown('<div style="text-align: right;">I want to know the future of:</div>', unsafe_allow_html=True)
    tech_name = col2.text_input("", max_chars=50)
    col2.markdown('*For example, try: Computers*')

    col3.markdown('##')
    if tech_name:
        col3.button('Ask me again!')
    else:
        col3.button('Ask!')

    return tech_name


def print_prediction(prediction):
    st.markdown('\n---\n')
    st.markdown(f"**In the future**,{prediction}")
    st.markdown('\n---\n')
    # col1, col2, col3 = st.columns(3)
    # col3.button('Ask me again')


def request_future(tech_name):
    response = openai.Completion.create(
        engine='davinci',
        prompt=build_prompt(tech_name),
        max_tokens=150,
        temperature=0.9,
        stop='\n'
    )
    completion = response['choices'][0]['text']
    return completion

    
def build_prompt(tech_name):
    return f"""
This is a predictor of the future of technology.

Q: What is the future of cars?
A: In the future, automobiles will be battery-powered, linked to networks, and smart in terms of automated driving, the study found. And coupled with that are on-board digital entertainment and shared-mobility features that will also require powerful computing technology.

Q: What is the future of computers?
A: In the future, computers promise to be even faster than today's computers and smaller than a deck of cards. Perhaps they will become the size of coins and offer "smart" or artificial intelligence features like expert intelligence, neural network pattern recognition features, or natural language capabilities.

Q: What is the future of television?
A: In the future, TV will be an immersive experience for viewers. Instead of simply watching something happen on their screens, viewers will participate in the show and have a chance to interact and potentially impact the outcome of the show.

Q: What is the future of {tech_name}?
A: In the future,
""".strip()



if __name__ == '__main__':
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main()
