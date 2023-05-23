##################################################################################################
#################################   Start of Importing Section   #################################
import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

##################################   End of Importing Section   ##################################
##################################################################################################

# TO RUN STREAMLIT IN LOCAL SERVER WRITE THIS IN YOUR COMMAND LINE:

# $ streamlit run introduction.py


##################################################################################################
###################    Retrieving the information from the database from AWS   ###################


# Information of the AMAZON REDSHIFT database.
host = "database-alertas-sismicas.crcnepco0igw.us-east-1.rds.amazonaws.com"
user = "admin"
password = "admin4168"
database = "alertasSismicas"

# Opening the connection to the database
connection = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

# SELECTING the table "FACTS" and giving the info to a pandas data frame
query = ("SELECT * FROM FACTS;")
facts = pd.read_sql(query, connection)

# Closing the connection with the database
connection.close()


#############################    Closing connection with database   ##############################
##################################################################################################





##################################################################################################
##################################   Start of STREAMLIT CODE   ###################################

st.markdown('<p class = "title_1">Magnitude-Frequency Relationship</p>', unsafe_allow_html=True)
st.markdown("***")


# ================================================================
# 04 - Creating Magnitude-Frequency Relationship graph
# ================================================================
st.markdown("***")
st.markdown('<p class = "title_2">Magnitude-Frequency Relationship</p>', unsafe_allow_html=True)
st.markdown('<div class="block_intro"><p class="text">The frequency axis in the "Magnitude-Frequency Relationship" scatter plot represents the number of occurrences or frequency of earthquakes for each magnitude value. In this context, the frequency indicates how many earthquakes have been recorded for a specific magnitude. For example, if a certain magnitude value has a high frequency, it means that earthquakes with that magnitude have occurred frequently or in larger numbers.<br><br>The frequency axis provides insights into the distribution of earthquakes across different magnitudes. It can help identify patterns or trends in earthquake occurrence, such as the presence of more frequent smaller-magnitude earthquakes or rare, larger-magnitude events. This information is valuable for understanding seismic activity and assessing the relative occurrence rates of different magnitudes.<br><br> Please have in mind that the IDs for the countries are:<br> USA[1] - Japan[2] - Chile[3]</p></div>', unsafe_allow_html=True)

# Changing numbers to the actual country name.
facts['idcountry'] = facts['idcountry'].replace(1, "USA")
facts['idcountry'] = facts['idcountry'].replace(2, "Japan")
facts['idcountry'] = facts['idcountry'].replace(3, "Chile")

# Create a multiselect filter for countries
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<p class = "title_3">Filter by Country:</p>', unsafe_allow_html=True)
selected_countries = st.multiselect("   ", facts['idcountry'].unique(), default = "USA")

# Filter the data based on selected countries
filtered_data = facts[facts['idcountry'].isin(selected_countries)]

# Aggregate the filtered data to calculate frequency of each magnitude per country
frequency_data = filtered_data.groupby(['idcountry', 'mag']).size().reset_index(name='frequency')

# Create the scatter plot for each country
fig, ax = plt.subplots()
for country in selected_countries:
    country_data = frequency_data[frequency_data['idcountry'] == country]
    ax.scatter(country_data['mag'], country_data['frequency'], label=country)

ax.set_xlabel("Magnitude")
ax.set_ylabel("Frequency")
ax.legend()

# Display the plot using Streamlit
st.pyplot(fig)



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

.text {
font-size:16px;
color: #92B8FF;
}

.block_intro {
background-color: #003B8E;
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
height: 350px;
}
</style> """, unsafe_allow_html=True)

######################################    End "CSS" Code   #######################################
##################################################################################################