<p align=center><img src='img/Logos/Banner-en.png' width=2000 height=600></p>

<h1 align=center>Project proposal</h1>
<h1 align=center>Seismic Alert System</h1>

<h2>Understanding of the current situation</h2>

<p>Unpredictable natural events such as earthquakes claim the lives of hundreds of people when they happen, they can even cause other secondary events such as tsunamis, volcano activation, nuclear hazards and after they happen, the structure of the buildings is not known.
Current alerts with numbers or colors do not provide much information about secondary events or the destructiveness of an earthquake.
We face the need to be able to communicate and alert the population of a region about the possibility of natural events, their destructiveness and their consequences.</p>

<p>This team proposes an analysis of the situation of the last years 2018-2023 and an earthquake classification method.</p>

<h2>General Objetives</h2>

<ul>
<li>Expand alert coverage.</li>
<li>Improve the time and type of reaction.</li>
<li>Guarantee accessibility to the alert system.</li>
<li>Deliver a quality system.</li>
</ul>

<h2>Project Scope</h2>

<p>The scope of the project will be for the countries: Chile, United States and Japan. Data from their respective observatories will be used. The use of external data or data from other countries to improve the model is not ruled out. The model will be of classification.</p>


<h2>KPIs</h2>

<ul>
<li>Kpi: Effective coverage percentage --> objective: Expand alert coverage.</li>
<li>Kpi: Average reaction time --> objective: Improve the time and type of reaction.</li>
<li>Kpi: Average number of users per social network platform --> objective: Guarantee accessibility to the alert system.</li>
<li>Kpi: Precision ratio of current alerts --> objective: Increase the precision and therefore the quality of the classification.</li>
</ul>
<p>All kpis will be taken on an annual basis.</p>

<h2>GitHub Repository</h2>

<p><img src=img/Logos/ghLogo.png width=20 height=20> <a href="https://github.com/jhonvelasque/SISTEMA_DE_ALERTAS_SISMICA"> &nbsp SISTEMA_DE_ALERTAS_SISMICAS</a></p>

<p>The repository will be organized in folders for each work area.</br>And also a /img folder to orderly store the images of the reports for each stage.</p>

<img src='img/Logos/carpetas.png' width=200 height=120>

<p>To collaborate we opted for two methods that github gives us at the choice of the collaborator.</br>

<li> The fork and pull request system, where everyone works on their personal copy of the original repository in their account and sends the changes every day for the rest to see their progress.</br>
<li>The system of direct cloning of the original repository to work in a branch with its name and see the progress from its branch, when finishing the work the branch will be merged to the main branch.</p>

<h2>Proposed solution</h2>
<p>The proposed solution is an alert API that can be implemented in different social networks and mobile applications, to achieve this the following tasks are proposed.</p>

<p><li>Data engineering: Data will be extracted from different sources, transformed and stored in the Amazon AWS cloud.</p>
<p><li>Data analytics: The stored data will be used to show the current situation with an interactive dashboard.</p>
<p><li>Data science: An earthquake classification model will be created with a machine learning model.</p>

<h2>Work Team</h2>

<p><a href="https://www.linkedin.com/in/jhon-velasque-228093211/"><img alt="Jhon" title="Conectar con Jhon" src="https://img.shields.io/badge/Jhon Velasque Durand-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> Data Engineering</p>

<p><a href="https://www.linkedin.com/in/luis-fernando-montero-castro-711b6524b/"><img alt="Luis" title="Conectar con Luis" src="https://img.shields.io/badge/Luis Fernando Montero-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> Data Engineering</p>

<p><a href="https://www.linkedin.com/in/juan-pablo-idrovo-3366a351/"><img alt="Juan Pablo" title="Conectar con Juan Pablo" src="https://img.shields.io/badge/Juan Pablo Idrovo-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> Data Analyst</p>

<p><a href="https://www.linkedin.com/in/esteban-roca-carbajal-5b3957135/"><img alt="Esteban" title="Conectar con Esteban" src="https://img.shields.io/badge/Esteban Roca Carbajal-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> Data Science</p>

<p><a href="https://www.linkedin.com/in/juanm-araoz4168/"><img alt="juan" title="Conectar con Juan" src="https://img.shields.io/badge/Juan Manuel Araoz-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> Data Science</p>

<p>The system of managers by area and assistants will be used if help is needed.</p>

<h2>Technologic Stack</h2>

<h3>Planning and Collaboration</h3>

<p><img src='img/Logos/notionLogo.png' width=20 height=20> &nbsp Notion</p>

<p><img src='img/Logos/discordLogo2.png' width=20 height=20> &nbsp Discord</p>

<p><img src='img/Logos/whatsappLogo.png' width=20 height=20> &nbsp Whatsapp</p>

<p><img src='img/Logos/ghLogo.png' width=20 height=20> &nbsp GitHub</p>


<h3>Data Engineering</h3>

<p><img src='img/Logos/pythonLogo.png' width=20 height=20> &nbsp Python</p>

<p><img src='img/Logos/numpyLogo.png' width=60 height=20> &nbsp Numpy</p>

<p><img src='img/Logos/seabornLogo.svg' width=30 height=20> &nbsp Seaborn</p>

<p><img src='img/Logos/amazonLogo.png' width=30 height=20> &nbsp Amazon AWS</p>

<h3>Data Analytics</h3>

<p><img src='img/Logos/seabornLogo.svg' width=30 height=20> &nbsp Seaborn</p>

<p><img src='img/Logos/matplotlibLogo.png' width=50 height=20> &nbsp Matplotlib</p>

<p><img src='img/Logos/powerbiLogo.jpg' width=60 height=20> &nbsp PowerBI</p>

<h3>Data Science</h3>

<p><img src='img/Logos/pythonLogo.png' width=20 height=20> &nbsp Python</p>

<p><img src='img/Logos/sklearnLogo.png' width=60 height=20> &nbsp Sklearn</p>

<p><img src='img/Logos/fastApiLogo.png' width=60 height=20> &nbsp FastAPI</p>

<p><img src='img/Logos/renderLogo.png' width=60 height=20> &nbsp Render</p>

<h2>Data Quality</h2>

<p>The data will be extracted from the following sources:</br>

<li>EEUU: &nbsp <a href='https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2012-01-01%2000:00:00&endtime=2022-12-31%2023:59:59&maxlatitude=50&minlatitude=24.6&maxlongitude=-65&minlongitude=-125&minmagnitude=3&orderby=time-asc'>earthquake.usgs.gov/usa </a></p>

<p align=center><img src='img/Logos/usadataAnalisis.png' width=500 height=350></p>

<p><li>Japan: &nbsp <a href='https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2012-01-01%2000:00:00&endtime=2022-12-31%2023:59:59&minlatitude=27.000000&maxlatitude=44.000000&minlongitude=132.780000&maxlongitude=145.530000&&minmagnitude=3&orderby=time-asc'>earthquake.usgs.gov/japan </a></p>

<p align=center><img src='img/Logos/japondataAnalisis.png' width=500 height=350></p>

<p><li>Chile: &nbsp <a href='https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2012-01-01%2000:00:00&endtime=2022-12-31%2023:59:59&minlatitude=-56.800000&maxlatitude=-19.000000&minlongitude=-79.000000&maxlongitude=-69.900000&jsonerror=true'>earthquake.usgs.gov/chile </a>
</p>

<p align=center><img src='img/Logos/chiledataAnalisis.png' width=500 height=350></p>

<p>Map of countries involved.</p>

<p align=center><img src='img/Logos/alcance.jpeg' width=500></p>

<p>quantum analytics</p>