##################################################################################################
#################################   Start of Importing Section   #################################
import streamlit as st
import pandas as pd
import mysql.connector
import folium
from streamlit_folium import folium_static



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
# query = ("SELECT * FROM FACTS2;")
query = ("SELECT * FROM FACTS;")
facts = pd.read_sql(query, connection)

# Closing the connection with the database
connection.close()


#############################    Closing connection with database   ##############################
##################################################################################################





##################################################################################################
##################################   Start of STREAMLIT CODE   ###################################

st.markdown('<p class = "title_1">Seismic Event Map By Danger</p>', unsafe_allow_html=True)
st.markdown("***")




# ================================================================
# 05 - Creating TEST Map
# ================================================================
st.markdown('<div class="block_intro"><p class="text">The map provides a clear overview of where and how severe the earthquakes have been. On the map, you will see circles representing each earthquake event. The size of the circles remains constant, but the color varies based on the danger level of the earthquake. This color distinction helps us quickly identify the severity of each event.<br><br> The legend for the colors is very intuitive, is as follows:<br><br>  - Green circles represent earthquakes with a danger level of 1.<br>  - Orange circles represent earthquakes with a danger level of 2.<br>  - Red circles represent earthquakes with a danger level of 3.</p></div>', unsafe_allow_html=True)
st.markdown("***")


# Changing numbers to the actual country name.
facts['idcountry'] = facts['idcountry'].replace(1, "USA")
facts['idcountry'] = facts['idcountry'].replace(2, "Japan")
facts['idcountry'] = facts['idcountry'].replace(3, "Chile")




# Use for FACTS2
# facts.rename(columns={'Ing': 'lon'}, inplace=True)


# Use for FACTS
facts.rename(columns={'lng': 'lon'}, inplace=True)

# Filter the data based on the selected year
# min_year = pd.to_datetime(facts['time']).dt.year.min()
# max_year = pd.to_datetime(facts['time']).dt.year.max()

# Test
min_year = int(facts['time'].dt.year.min())
max_year = int(facts['time'].dt.year.max())

selected_year = st.slider("Select Year:", min_value=min_year, max_value=max_year)

# Filter the data based on the selected year
filtered_facts = facts[pd.to_datetime(facts['time']).dt.year == selected_year]

# Create the map
m = folium.Map(location=[0, 0], zoom_start=2)

# Add circles to the map
for _, row in filtered_facts.iterrows():
    danger = row['danger']
    color = 'green' if danger == 1 else 'orange' if danger == 2 else 'red'
    
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
        popup=f"Magnitude: {row['mag']} | Depth: {row['depth']} | Danger: {danger}"
    ).add_to(m)

# Display the map using Streamlit
folium_static(m)




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