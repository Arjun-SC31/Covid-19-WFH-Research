# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 14:53:52 2022

@author: Acer
"""

#🔬

import streamlit as st
import base64

st.set_page_config(
    page_title="Research Background", page_icon="🔬", initial_sidebar_state="expanded"
)



def main():
    
    st.title("This Is The Research On The Basis Of Which The Model Was Built")
    st.subheader("")
    st.subheader("Publisher: IGI Global Inc. ")
    st.subheader("Book Name: Principles and Applications of Socio-Cognitive and Affective Computing")
    
    html_temp1 = """
    <div style = 'background-color: tomato; padding: 50px>
    <h3 style = 'color: white; text-align: center;'></h3>
    <h3 style = 'color: white; text-align: left; padding-left: 20px'>Research Title:</h3>
    <h4 style = 'color: white; text-align: left; padding-left: 20px'>Statistical Hypothesization and Predictive Modeling of Reactions to COVID-19 Induced Remote Work</h3>
    </div>
    """
    st.markdown(html_temp1, unsafe_allow_html=True)
    
    #st.subheader("Publisher: IGI Global Inc. ")
    #st.subheader("Book Name: Principles and Applications of Socio-Cognitive and Affective Computing")
        
    displayPDF("Covid-19-WFH-Research/pages/research paper.pdf")
    
    st.subheader("Important Note")
    html_note = '''
    <p>Please note that this study was conducted between September and December, 2020.
    At that time frame, the world was still relatively new to the virtual work and study space
    expedited by COVID-19. We had to rush into working remotely, with a lot of different
    circumstances and events playing out in our personal, academic, and professional lives.
    As with any major change, psychologically, we have the tendency to resist change initially.
    We noticed this in our questionnaire response trends. 73% of our respondents wished to 
    return to the original work-setting, this even included those who were really liking
    the virtual setting.</p>
    <p>Now that remote work has become the norm in some sense, there is resistence to
    returning back to the office, which corroborates our psychological tendency to
    resist change.</p>
    <p>A lot has changed with respect to the work environment conditions, some of which
    even we did not speculate despite our in-depth analysis of psychological literature
    and other studies conducted by corporate and certain consulting firms. Since the whole
    scenario with respect to working patterns has changed so dramatically over the past two
    years, we request you not to take the results of this test very seriously. The model
    built by us uses data collected in the latter half of 2020, when most people wished to
    return to the office despite loving WFH otherwise.</p>
    <p>Hence, chances are that you might be suggested a physical attendance setting,
    even if your responses indicate that WFH might be a more appropriate setting for you.</p>
    <p>That said, we wish to share the results of our work with the world, because we believe
    that in the several studies conducted, ours could contribute to the community for the 
    context of people's mindset at a particular time frame. '''
    
    st.markdown(html_note, unsafe_allow_html=True)

    # Function to display PDF file. 
    # Source: https://discuss.streamlit.io/t/rendering-pdf-on-ui/13505
    
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    #pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    pdf_display = f'<p align="center"><iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe></p>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
    
if __name__ == '__main__':
    main()
    st.subheader("")
    st.caption(f"You can find me on [LinkedIn](https://www.linkedin.com/in/as3152k)")
    st.caption(f"Here is my [Personal Website](https://arjun-sc31.github.io)")
