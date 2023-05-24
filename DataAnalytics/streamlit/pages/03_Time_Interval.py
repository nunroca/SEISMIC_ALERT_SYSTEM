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

st.markdown('<p class = "title_1">Time Interval Between Consecutive Seisms</p>', unsafe_allow_html=True)
st.markdown("***")



# ================================================================
# 03 - Creating Seismic Magnitude-Time Distribution graph
# ================================================================
st.markdown("***")
st.markdown('<p class = "title_2">Time Interval Between Consecutive Seisms</p>', unsafe_allow_html=True)
st.markdown('<div class="block_intro"><p class="text">The "Time Interval Between Consecutive Seisms" graph is a visualization that helps evaluate the temporal patterns of earthquake occurrence over a specific period, from 2010 until 2023. The graph displays the time intervals between consecutive seismic activities on the x-axis and the total count of seismic activities on the y-axis. Additionally, each country is represented by a distinct color in the graph, with Japan, Chile, and the United States being the specific countries highlighted.<br><br>This graph facilitates the analysis of temporal patterns in earthquake occurrence, allowing researchers and stakeholders to identify trends, clusters, or anomalies in seismic activity. It can aid in earthquake prediction, risk assessment, and the development of mitigation strategies to enhance preparedness and response measures.</p></div>', unsafe_allow_html=True)


# Changing numbers to the actual country name.
facts['idcountry'] = facts['idcountry'].replace(1, "USA")
facts['idcountry'] = facts['idcountry'].replace(2, "Japan")
facts['idcountry'] = facts['idcountry'].replace(3, "Chile")

# Calculate time intervals between consecutive earthquakes
facts['time_between'] = facts['time'].diff()

# Get unique countries
unique_countries_03 = facts['idcountry'].unique()


# Create multiselect filter for countries
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<p class = "title_3">Filter by Country:</p>', unsafe_allow_html=True)
selected_countries_03 = st.multiselect("  ", unique_countries_03, default = ["Japan"])

# Filter data based on selected countries
filtered_data = facts[facts['idcountry'].isin(selected_countries_03)]

# Create the histogram
fig, ax = plt.subplots()

# Assign a unique color to each country
colors = plt.cm.get_cmap('tab20', len(selected_countries_03))

# Calculate bin edges based on the maximum time interval
max_time_interval = filtered_data['time_between'].max().total_seconds() / 3600
bin_edges = np.linspace(0, max_time_interval, num = 20)  # Adjust the number of bins as needed

# Create histogram for each country
for i, country in enumerate(selected_countries_03):
    country_data = filtered_data[filtered_data['idcountry'] == country]
    ax.hist(
        country_data['time_between'].dropna().dt.total_seconds() / 3600,
        bins=bin_edges,
        label=country,
        color=colors(i),
        alpha=0.7
    )

# Set x-axis limits to zoom in
ax.set_xlim(0, 150)  # Adjust the limits as needed

# Customize the plot
plt.title('Time Interval Between Consecutive Seisms')
ax.set_xlabel("Time Intervals (hours)")
ax.set_ylabel("Total Count")
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