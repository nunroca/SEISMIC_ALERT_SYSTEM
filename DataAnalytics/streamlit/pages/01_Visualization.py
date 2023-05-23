##################################################################################################
#################################   Start of Importing Section   #################################
import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image


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

st.sidebar.markdown("Visualization page with graphs.")

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

# Load and display image from a local file
image = Image.open('img/BBA.jpeg')
st.image(image, caption=' ', use_column_width=True)

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

# ================================================================
# 02 - Creating Seismic Magnitude-Time Distribution graph
# ================================================================
st.markdown("***")
st.markdown('<p class = "title_2">Seismic Magnitude-Time Distribution</p>', unsafe_allow_html=True)
st.markdown('<div class="block_intro"><p class="text">The second graph, titled "Seismic Magnitude-Time Distribution", depicts the relationship between seismic magnitude and time for three countries: Japan, Chile, and the United States. This metric helps identify temporal trends and changes in seismic magnitudes over the specified time period, providing valuable insights into the overall seismic activity and potential risks within each country or region.<br><br> Understanding the magnitude-time distribution is crucial for seismic forecasting, hazard assessment, and preparedness efforts. By visualizing the variations in seismic magnitudes over time, this graph provides a broader perspective on the temporal behavior of seismic activity in Japan, Chile, and the United States. It aids in identifying potential patterns, trends, or anomalies that can contribute to a better understanding of the seismic activity and inform risk mitigation strategies.<br><br> Please have in mind that the IDs for the countries are:<br> USA[1] - Japan[2] - Chile[3]</p></div>', unsafe_allow_html=True)

# Filter the data for the three countries you want to plot
countries_list = facts['idcountry'].unique().tolist()

st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<p class = "title_3">Filter by Country:</p>', unsafe_allow_html=True)
countries = st.multiselect(" ", countries_list, default = [2])

# Create a Streamlit sidebar with a time filter slider

st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<p class = "title_3">Filter by Year:</p>', unsafe_allow_html=True)
min_year = int(facts['time'].dt.year.min())
max_year = int(facts['time'].dt.year.max())
selected_year = st.slider(" ", min_value = min_year, max_value = max_year)

# Filter the data based on the selected year and countries
# filtered_data = facts[(facts['time'].dt.year == selected_year)]
filtered_data = facts[(facts['time'].dt.year == selected_year) & (facts['idcountry'].isin(countries))]

# Create a figure and axes with adjusted size
fig, ax = plt.subplots(figsize=(10, 6))

# Create a line chart for each country
for country in countries:
    country_data = filtered_data[filtered_data['idcountry'] == country]
    plt.plot(country_data['time'], country_data['mag'], label=country)

# Set the chart title and labels
plt.title('Seismic Magnitude-Time Distribution')
plt.xlabel('Time')
plt.ylabel('Magnitude')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add a legend
plt.legend()

# Display the plot using Streamlit
st.pyplot(fig)


# ================================================================
# 03 - Creating Seismic Magnitude-Time Distribution graph
# ================================================================
st.markdown("***")
st.markdown('<p class = "title_2">Time Interval Between Consecutive Seisms</p>', unsafe_allow_html=True)
st.markdown('<div class="block_intro"><p class="text">The "Time Interval Between Consecutive Seisms" graph is a visualization that helps evaluate the temporal patterns of earthquake occurrence over a specific period, from 2010 until 2023. The graph displays the time intervals between consecutive seismic activities on the x-axis and the total count of seismic activities on the y-axis. Additionally, each country is represented by a distinct color in the graph, with Japan, Chile, and the United States being the specific countries highlighted.<br><br>This graph facilitates the analysis of temporal patterns in earthquake occurrence, allowing researchers and stakeholders to identify trends, clusters, or anomalies in seismic activity. It can aid in earthquake prediction, risk assessment, and the development of mitigation strategies to enhance preparedness and response measures.<br><br> Please have in mind that the IDs for the countries are:<br> USA[1] - Japan[2] - Chile[3]</p></div>', unsafe_allow_html=True)


# Calculate time intervals between consecutive earthquakes
facts['time_between'] = facts['time'].diff()

# Get unique countries
unique_countries_03 = facts['idcountry'].unique()



# Create multiselect filter for countries
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<p class = "title_3">Filter by Country:</p>', unsafe_allow_html=True)
selected_countries_03 = st.multiselect("  ", unique_countries_03, default = [2])

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







# ================================================================
# 04 - Creating Magnitude-Frequency Relationship graph
# ================================================================
st.markdown("***")
st.markdown('<p class = "title_2">Magnitude-Frequency Relationship</p>', unsafe_allow_html=True)
st.markdown('<div class="block_intro"><p class="text">The frequency axis in the "Magnitude-Frequency Relationship" scatter plot represents the number of occurrences or frequency of earthquakes for each magnitude value. In this context, the frequency indicates how many earthquakes have been recorded for a specific magnitude. For example, if a certain magnitude value has a high frequency, it means that earthquakes with that magnitude have occurred frequently or in larger numbers.<br><br>The frequency axis provides insights into the distribution of earthquakes across different magnitudes. It can help identify patterns or trends in earthquake occurrence, such as the presence of more frequent smaller-magnitude earthquakes or rare, larger-magnitude events. This information is valuable for understanding seismic activity and assessing the relative occurrence rates of different magnitudes.<br><br> Please have in mind that the IDs for the countries are:<br> USA[1] - Japan[2] - Chile[3]</p></div>', unsafe_allow_html=True)



# Create a multiselect filter for countries
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<p class = "title_3">Filter by Country:</p>', unsafe_allow_html=True)
selected_countries = st.multiselect("   ", facts['idcountry'].unique(), default = 1)

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
