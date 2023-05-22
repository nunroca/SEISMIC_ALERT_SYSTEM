##################################################################################################
#################################   Start of Importing Section   #################################

import streamlit as st
from PIL import Image

##################################   End of Importing Section   ##################################
##################################################################################################


# TO RUN STREAMLIT IN LOCAL SERVER WRITE THIS IN YOUR COMMAND LINE:

# $ streamlit run introduction.py



##################################################################################################
##################################   Start of STREAMLIT CODE   ###################################

st.markdown('<p class = "title_1">Seismic Alert System</p>', unsafe_allow_html=True)
st.markdown("***")

st.markdown('<p class="title_2">Introduction</p>', unsafe_allow_html=True)
st.markdown('<div class="block_intro"><p class="text">We are a consulting firm called Quantum Analytics. Using data collection and analysis of seismic movements in the United States, Japan, and Chile, our consultancy utilizes a specific machine learning model to classify seismic movements and detect patterns. By validating the accuracy of our model, we can ensure that it provides reliable results to inform citizens about potential seismic hazards. Finally, we effectively communicate these results to reach as many people as possible and contribute to public safety.</p></div>', unsafe_allow_html=True)


# Load and display image from a local file
# image = Image.open('analytics.jpg')

# st.image(image, caption='Data Analytics is Key for Success', use_column_width=True)

st.markdown('<p class="title_2">Our Team</p>', unsafe_allow_html=True)
st.markdown('<div class="block_team"><p class="text"> <a href="https://www.linkedin.com/in/juan-pablo-idrovo-3366a351/" target="_blank">Juan Pablo Idrovo</a> - Data Analyst<br><a href="https://www.linkedin.com/in/juanm-araoz4168/" target="_blank">Juan Manuel Araoz</a> - Data Scientist<br> <a href="https://www.linkedin.com/in/esteban-roca-carbajal-5b3957135/" target="_blank">Esteban Roca Carbajal</a> - Data Scientist<br> <a href="https://www.linkedin.com/in/jhon-velasque-228093211/" target="_blank">Jhon Velasque Durand</a> - Data Engineer<br> <a href="https://www.linkedin.com/in/luis-fernando-montero-castro-711b6524b/" target="_blank">Luis Fernando Montero</a> - Data Engineer</p></div>', unsafe_allow_html=True)

st.markdown('<p class="title_2">KPIs</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)


with col1:
    st.markdown('<div class="block_kpis"><p class="title_3">Alert Response Time: </p><p class="text">This measures the time it takes for the alert system to notify the people after an earthquake event occurs. This KPI helps assess the speed and efficiency of your alert.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="block_kpis"><p class="title_3">Alert Reach: </p><p class="text">Assess the percentage of the population reached by the alerts. This KPI provides insights into the coverage and penetration of the alert system and helps identify areas or demographic groups that may need additional attention.</p></div>', unsafe_allow_html=True)
 
with col3:
    st.markdown('<div class="block_kpis"><p class="title_3">Impact Assesment:</p><p class="text">Assess the impact of earthquakes by analyzing their relationships with secondary events, such as tsunamis and volcanic hazards. This KPI can provide insights into the potential consequences. Increase accuracy and clasification quality.</p></div>', unsafe_allow_html=True)

st.markdown('<p class="title_2">Metrics</p>', unsafe_allow_html=True)

formula1, formula2, formula3 = st.columns(3)

with formula1:
    st.markdown('<div class="block_formulas"><p class="title_3_dark">KPI 1 =</p><p class="textDark">[(RTactual-RTpast)/ RTpast]*100%<br>RT: Response Time</p></div>', unsafe_allow_html=True)

with formula2:
    st.markdown('<div class="block_formulas"><p class="title_3_dark">KPI 2 =</p><p class="textDark">[(NºVactual-Nº_past)/Nº_past]*100%<br>V: Views</p></div>', unsafe_allow_html=True)
 
with formula3:
    st.markdown('<div class="block_formulas"><p class="title_3_dark">KPI 3  =</p><p class="textDark">[Ractual-R_past)/R_past]*100%<br>R: Reliability</p></div>', unsafe_allow_html=True)

st.markdown('<p class="title_2">How can we achieve this?</p>', unsafe_allow_html=True)

sol1, sol2, sol3 = st.columns(3)


with sol1:
    st.markdown('<div class="block_solution"><p class="title_3">Improve</p><p class="text">Improve the response system and make the code more efficient.</p></div>', unsafe_allow_html=True)

with sol2:
    st.markdown('<div class="block_solution"><p class="title_3">Establish</p><p class="text">Establish new dissemination points for alerts, such as Twitter, Facebook, and Telegram.</p></div>', unsafe_allow_html=True)
 
with sol3:
    st.markdown('<div class="block_solution"><p class="title_3">Train</p><p class="text">Train the ML model with more variables, refine the results with test cases.</p></div>', unsafe_allow_html=True)



st.sidebar.markdown("Home")

###################################   End of STREAMLIT CODE   ####################################
##################################################################################################





##################################################################################################
#####################################    Start "CSS" Code   ######################################

st.markdown(""" <style>
.title_1 {
font-size:50px;
color: #92B8FF;
font-weight: bold;
}

.title_2 {
font-size:30px;
color: #92B8FF;
margin: 8px;
font-weight: bold;

}

.title_3 {
font-size:22px;
color: #92B8FF;
font-weight: bold;
}

.title_3_dark {
font-size:22px;
color: #003B8E;
font-weight: bold;
}

.text {
font-size:16px;
color: #92B8FF;
}

.textDark {
font-size:16px;
color: #003B8E;
}

.block_intro {
background-color: #003B8E;
border: 2px solid #92B8FF;
border-radius: 5px;
padding: 15px;
}

.block_team {

border: 2px solid #92B8FF;
border-radius: 5px;
padding: 15px;
}

.block_kpis {
background-color: #003B8E;
border: 2px solid #92B8FF;
border-radius: 5px;
padding: 15px;
margin: 8px;
height: 400px;
}

.block_formulas {
background-color: #92B8FF;
border: 2px solid #003B8E;
border-radius: 5px;
padding: 15px;
margin: 8pxs;
height: 175px;
}

.block_solution {
background-color: #003B8E;
border: 2px solid #92B8FF;
border-radius: 5px;
padding: 15px;
margin: 8pxs;
height: 200px;
}
</style> """, unsafe_allow_html=True)

######################################    End "CSS" Code   #######################################
##################################################################################################



