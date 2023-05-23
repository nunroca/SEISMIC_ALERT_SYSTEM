##################################################################################################
#################################   Start of Importing Section   #################################

import streamlit as st

##################################   End of Importing Section   ##################################
##################################################################################################


# TO RUN STREAMLIT IN LOCAL SERVER WRITE THIS IN YOUR COMMAND LINE:

# $ streamlit run introduction.py



##################################################################################################
##################################   Start of STREAMLIT CODE   ###################################

st.markdown('<p class = "title_1">Seismic Alert System</p>', unsafe_allow_html=True)
st.markdown("***")

st.markdown('<p class = "title_2">Conclusion</p>', unsafe_allow_html=True)
st.markdown('<div class="block_intro"><p class="text">In summary, the four graphs presented in this seismic analysis are key tools for understanding seismic activity in Japan, Chile, and the United States. The "Sum of Seismic Activities per Country" graph allows for the identification of areas with higher seismic activity and assesses the intensity of earthquakes recorded in each country over time. The "Seismic Magnitude-Time Distribution" reveals temporal patterns and trends in seismic magnitudes, providing valuable information for risk assessment and planning of mitigation measures. The "Time Interval Between Consecutive Seisms" provides insights into the temporal patterns of earthquake occurrence, helping to understand clustering and gaps between seismic events. Lastly, the "Magnitude-Frequency Relationship" reveals the distribution of earthquakes according to their magnitudes, allowing for the identification of the frequency of events of different sizes. These combined graphs provide a comprehensive view of seismic activity, supporting informed decision-making and the implementation of appropriate safety measures.</p></div>', unsafe_allow_html=True)
st.markdown("***")



st.markdown('<p class = "title_2">Conclusion - KPIs</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)


with col1:
    st.markdown('<div class="block_conc"><p class="title_3">Alert Response Time: </p><p class="text">This measures the time it takes for the alert system to notify the people after an earthquake event occurs. This KPI helps assess the speed and efficiency of your alert.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="block_conc"><p class="title_3">Alert Reach: </p><p class="text">Assess the percentage of the population reached by the alerts. This KPI provides insights into the coverage and penetration of the alert system and helps identify areas or demographic groups that may need additional attention.</p></div>', unsafe_allow_html=True)
 
with col3:
    st.markdown('<div class="block_conc"><p class="title_3">Impact Assesment:</p><p class="text">Assess the impact of earthquakes by analyzing their relationships with secondary events, such as tsunamis and volcanic hazards. This KPI can provide insights into the potential consequences. Increase accuracy and clasification quality.</p></div>', unsafe_allow_html=True)


st.markdown("***")
st.markdown('<p class = "title_1">Thank You !</p>', unsafe_allow_html=True)

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
margin: 12px;
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

.block_conc {

border: 2px solid #92B8FF;
border-radius: 5px;
padding: 15px;
height: 400px;
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



