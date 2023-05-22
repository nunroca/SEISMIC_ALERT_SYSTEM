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
port = "3306"

# Opening the connection to the database
connection = mysql.connector.connect(
    host = host,
    port = port,
    user = user,
    password = password,
    database = database
)

# SELECTING the table "FACTS" and giving the info to a pandas data frame
query = ("SELECT * FROM FACTS;")
facts = pd.read_sql(query, connection)
# print(historical_chile.head(2))

# SELECTING the table "JAPAN" and giving the info to a pandas data frame
query = ("SELECT * FROM JAPAN;")
japan = pd.read_sql(query, connection)
# print(historical_japan.head(2))

# SELECTING the table "USA" and giving the info to a pandas data frame
query = ("SELECT * FROM USA;")
usa = pd.read_sql(query, connection)
# print(historical_usa.head(2))

# SELECTING the table "CHILE" and giving the info to a pandas data frame
query = ("SELECT * FROM CHILE;")
chile = pd.read_sql(query, connection)
# print(historical_usa.head(2))

# Closing the connection with the database
connection.close()


#############################    Closing connection with database   ##############################
##################################################################################################





##################################################################################################
##################################   Start of STREAMLIT CODE   ###################################

st.markdown('<p class = "title_1">Visualization</p>', unsafe_allow_html=True)
st.markdown("***")


st.markdown('<p class = "title_2">DataFrames:</p>', unsafe_allow_html=True)


if st.button("Show preview"):
    st.write("Facts table:")
    st.dataframe(facts.head(3))
    st.write("Japan table:")
    st.dataframe(japan.head(3))
    st.write("USA table:")
    st.dataframe(usa.head(3))
    st.write("Chile table:")
    st.dataframe(chile.head(3))

st.markdown("***")


# ================================================================
# 01 - Creating Sum of Seismic Activities per Country
# ================================================================
st.markdown('<p class = "title_2">Sum of Seismic Activities per Country</p>', unsafe_allow_html=True)
st.markdown('<div class="block_intro"><p class="text">The first graph, titled "Sum of Seismic Activities per Country", represents the cumulative seismic activity from 2010 to 2023 for three specific countries: Japan, Chile, and the United States. This metric helps identify areas with higher seismic activity by showcasing the total amount of seismic events recorded in each country over the specified time period.<br><br> On the y-axis, the graph displays the sum of seismic activities, which represents the cumulative number or intensity of earthquakes occurring in each country. Higher values on the y-axis indicate a greater overall seismic activity for a particular country, while lower values suggest relatively lower seismic activity.<br><br> Please have in mind that the IDs for the countries are:<br> USA[1] - Japan[2] - Chile[3]</p></div>', unsafe_allow_html=True)


# Create a Streamlit sidebar date input for the time filter
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<p class = "title_3">Filter by Date:</p>', unsafe_allow_html=True)
time_filter = st.date_input(" ", value=(facts['time'].min().date(), facts['time'].max().date()))

# Filter the data based on the time filter value
start_date, end_date = pd.to_datetime(time_filter)
filtered_data = facts[(facts['time'] >= start_date) & (facts['time'] <= end_date)]

# Count the number of seisms in the filtered data
earthquake_count = len(filtered_data)

# Group the filtered data by country and count the seisms
earthquake_counts = filtered_data['idcountry'].value_counts()

# Create a bar plot using seaborn
sns.barplot(x=earthquake_counts.index, y=earthquake_counts.values)

# Set the labels and title
plt.xlabel("Country")
plt.ylabel("Number of Seisms")
plt.title("Sum of Seismic Activities per Country")

# Rotate the x-axis labels if needed
# plt.xticks(rotation=90)

# Display the earthquake count to the user
st.markdown(f'<p class = "title_3">Number of seism: {earthquake_count} </p>', unsafe_allow_html=True)

# Display the plot using Streamlit
st.pyplot(plt)


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