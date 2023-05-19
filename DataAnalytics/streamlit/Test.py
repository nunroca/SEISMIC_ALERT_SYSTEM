##################################################################################################
#################################   Start of Importing Section   #################################
import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 

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
# print(historical_chile.head(2))

# SELECTING the table "JAPAN" and giving the info to a pandas data frame
query = ("SELECT * FROM JAPAN;")
japan = pd.read_sql(query, connection)
# print(historical_japan.head(2))

# SELECTING the table "USA" and giving the info to a pandas data frame
query = ("SELECT * FROM USA;")
usa = pd.read_sql(query, connection)
# print(historical_usa.head(2))

# Closing the connection with the database
connection.close()


#############################    Closing connection with database   ##############################
##################################################################################################





##################################################################################################
##################################   Start of STREAMLIT CODE   ###################################

st.title("Test")


# Set up Streamlit
st.title("Magnitude-Frequency Relationship")
st.write("Scatter Plot")

# Create a multiselect filter for countries
selected_countries = st.multiselect("Select Countries", facts['idcountry'].unique(), default = 1)

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





