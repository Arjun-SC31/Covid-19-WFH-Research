# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 16:49:31 2022

@author: Arjun
"""
import numpy as np
import pickle
import pandas as pd
import streamlit as st
import sklearn
from xgboost import XGBClassifier

st.set_page_config(
    page_title="Work Style Suggestions", page_icon="👨‍💻", initial_sidebar_state="expanded"
)


pickle_in = open('xgboost_model.pkl', 'rb')
predictor_model = pickle.load(pickle_in)

data = pd.read_csv('psycho.csv')

# Function for making and returning the prediction
# 21 input parameters 
def WFH_predict(diff_online, home_env, prod_inc, sleep_bal,
       new_skill, fam_connect, relaxed, self_time, net_diff, ages,
       no_office_commute, loved_ones_close, lethargy, no_exercise,
       no_travel, bad_social_life, gender_Male, Occupation_Other,
       Occupation_Student, Occupation_Professional):
    
    
    prediction = predictor_model.predict([[diff_online, home_env, prod_inc, sleep_bal,
           new_skill, fam_connect, relaxed, self_time, net_diff, ages,
           no_office_commute, loved_ones_close, lethargy, no_exercise,
           no_travel, bad_social_life, gender_Male, Occupation_Other,
           Occupation_Student, Occupation_Professional]])
    
    
    return prediction


def main():
    
    st.title("Unsure if WFH is for you?")
    html_temp = """
    <div style = 'background-color: tomato; padding: 50px>
    <h3 style = 'color: white; text-align: center;'></h3>
    <h3 style = 'color: white; text-align: center;'>Use this Web-app I made to judge whether WFH suits you</h3>
    <h3 style = 'color: white; text-align: center;'>This is built based on my previous research.</h3>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    st.subheader("")

    if st.checkbox('Show the dataset'):
        data

    with st.form(key = 'form1', clear_on_submit=False):
        st.text_input("Enter your Name: ", key="name")
    
    
        st.subheader("Please enter the required information below.")
    
        # Enter age
        age = st.number_input('Enter your age (years)')

        # Input for fuel type
        gender = st.selectbox('Select the gender you identify as: ', options=['Male', 'Female', 'Non-Binary'])

        gender_type = 0
        if gender == 'Male':
            gender_type = 1
        else:
            gender_type = 0
                
                
                # Travel time daily
        travel = st.number_input('Enter the amount of time you spend travelling to and from your workplace')
    
    
        #Work hour difference calculation
        work_hours_office = st.number_input('How many hours did you work on a daily basis before COVID-19 struck?')
        work_hours_home = st.number_input('How many hours do you spend working on a daily basis while working at home?')
    
    
        #Work Hour Difference 
        time_diff = abs(int(travel + work_hours_office - work_hours_home))
    
    
        # Input for diff_of_online work 
        diff_online = 0
        diff_online1 = st.select_slider(
            'How difficult was it for you to adjust to an online environment?',
            options=['No sweat!', 'Slightly Challenging', 'Noticeably Difficult', 'Bothersome Difficulty', 'Earth-shattering Difficulty'])
        
        if diff_online1 == 'No sweat!':
            diff_online = 1
        elif diff_online1 == 'Slightly Challenging':
            diff_online = 2
        elif diff_online1 == 'Noticeably Difficult':
            diff_online = 3
        elif diff_online1 == 'Bothersome Difficulty':
            diff_online = 4
        else:
            diff_online = 5
    
    
        # Input for home-environment noise
        home_environment = 0
        home_environment1 = st.select_slider(
            'How noisy would you describe your home-environment?',
            options=['Pin-drop silence', 'Very little noise', 'Appreciable noise', 'It is Quite Noisy!', 'Colleagues often complain!'])
        
        if home_environment1 == 'Pin-drop silence':
            home_environment = 1
        elif home_environment1 == 'Very little noise':
            home_environment = 2
        elif home_environment1 == 'Appreciable noise':
            home_environment = 3
        elif home_environment1 == 'It is Quite Noisy!':
            home_environment = 4
        else:
            home_environment = 5
        
    
        # Input for occupation
        occ_student = occ_pro = occ_other = 0
        occupation1 = st.radio("What is your occupation?", ('Student', 'Working Professional', 'Other'))
        
        if occupation1 == 'Student':
            occ_student = 1
        elif occupation1 == 'Working Professional':
            occ_pro = 1
        else:
            occ_other = 1
        
    
        # Input for productivity levels
        st.subheader("For the next few questions, you would have to select your level of agreement to the statement")

    
        # Input for productivity levels
        prod_inc = 0
    
        productivity = st.radio("I feel more productive when I work from home: ", ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))
        
        if productivity == 'Strongly Disagree':
            prod_inc = 1
        elif productivity == 'Disagree':
            prod_inc = 2
        elif productivity == 'Neutral':
            prod_inc = 3
        elif productivity == 'Agree':
            prod_inc = 4
        else:
            prod_inc = 5
    
    
        # Input for Balanced Sleep
        sleep_bal = 0
    
        balanced_sleep = st.radio("I feel like my sleep cycle is more balanced when I work from home: ", ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))
        
        if balanced_sleep == 'Strongly Disagree':
            sleep_bal = 1
        elif balanced_sleep == 'Disagree':
            sleep_bal = 2
        elif balanced_sleep == 'Neutral':
            sleep_bal = 3
        elif balanced_sleep == 'Agree':
            sleep_bal = 4
        else:
            sleep_bal = 5
        
        
        # Input for new skill/hobby
        hobby = 0
    
        new_hobby_skill = st.radio("Working from home has allowed me to pick up a new skill or a hobby: ", ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))
    
        if new_hobby_skill == 'Strongly Disagree':
            hobby = 1
        elif new_hobby_skill == 'Disagree':
            hobby = 2
        elif new_hobby_skill == 'Neutral':
            hobby = 3
        elif new_hobby_skill == 'Agree':
            hobby = 4
        else:
            hobby = 5
        
    
        # Input for family connection
    
        fam_connect = 0
    
        family = st.radio("I am able to better connect with my family and spend quality time with them when WFH: ", ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))
    
        if family == 'Strongly Disagree':
            fam_connect = 1
        elif family == 'Disagree':
            fam_connect = 2
        elif family == 'Neutral':
            fam_connect = 3
        elif family == 'Agree':
            fam_connect = 4
        else:
            fam_connect = 5
        
    
        # Input for relaxed 
    
        relaxed = 0
    
        stress_levels = st.radio("I am able to manage my stress better while working from home, I feel more relaxed: ", ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))
    
        if stress_levels == 'Strongly Disagree':
            relaxed = 1
        elif stress_levels == 'Disagree':
            relaxed = 2
        elif stress_levels == 'Neutral':
            relaxed = 3
        elif stress_levels == 'Agree':
            relaxed = 4
        else:
            relaxed = 5
        
    
        # Input for self-care
    
        self_time = 0
    
        self_care = st.radio("I find time to concentrate on self-care while WFH: ", ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))
    
        if self_care == 'Strongly Disagree':
            self_time = 1
        elif self_care == 'Disagree':
            self_time = 2
        elif self_care == 'Neutral':
            self_time = 3
        elif self_care == 'Agree':
            self_time = 4
        else:
            self_time = 5
    
    
        st.subheader("For the next few questions, you would have to answer with a 'Yes' or 'No' ")
    
    # Input for no commute
    
        no_office_commute = 0
    
        no_commute = st.radio('Do you like not having to travel to your workplace every day?', ('Yes', 'No'))
    
        if no_commute == 'Yes':
            no_office_commute = 1
        else:
            no_office_commute = 0
        
    
    # Input for always having family close
    
    
        loved_ones_close = 0
    
        people = st.radio('Do you prefer having your loved ones in close proximity all the time?', ('Yes', 'No'))
    
        if people == 'Yes':
            loved_ones_close = 1
        else:
            loved_ones_close = 0
        
    
    # Input for Sedentary lifestyle
    
        lethargy = 0
    
        sedentary_lifestyle = st.radio('Do you feel like you lead a sedentary lifestyle at home because of WFH?', ('Yes', 'No'))
    
        if sedentary_lifestyle == 'Yes':
            lethargy = 1
        else:
            lethargy = 0
    
    
    # Input for no travel
    
        no_travel = 0
    
        no_travel1 = st.radio('Do you feel bothered by not being able to travel much?', ('Yes', 'No'))
    
        if no_travel1 == 'Yes':
            no_travel= 1
        else:
            no_travel = 0
        
    
    # Input for no exercise
    
        no_exercise = 0
    
        no_exercise1 = st.radio('Do you wish you could get more exercise when you WFH?', ('Yes', 'No'))
    
        if no_exercise1 == 'Yes':
            no_exercise= 1
        else:
            no_exercise = 0
        
    
    # Input for bad social life
    
        bad_social_life = 0
    
        sad_social = st.radio('Do you feel that your social life has been affected negatively while working from home?', ('Yes', 'No'))
    
        if sad_social == 'Yes':
            bad_social_life = 1
        else:
            bad_social_life = 0
        
        
        result = ''

        submit_button = st.form_submit_button(label = 'What work-style suits me?')
            
        if submit_button:
            result = WFH_predict(diff_online, home_environment, prod_inc, sleep_bal,
                                 hobby, fam_connect, relaxed, self_time, time_diff, age,
                                 no_office_commute, loved_ones_close, lethargy, no_exercise,
                                 no_travel, bad_social_life, gender_type, occ_other, occ_student, occ_pro)
        
        
            if(str(result) == '[0]'):
                result = 'Physical Attendence'
            else:
                result = 'Work From Home'
            
            st.success('Based on your answers, it looks like {} is suitable for you.'.format(str(result)))
            st.success(f'Thank you {st.session_state.name}! I hope you liked it.')
    



if __name__ == '__main__':
    main()
    st.subheader("")
    st.caption(f"You can find me on [LinkedIn](https://www.linkedin.com/in/as3152k)")
    st.caption(f"Here is my [Personal Website](https://arjun-sc31.github.io)")