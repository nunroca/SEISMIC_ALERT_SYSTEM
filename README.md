<p align=center><img src='img/Logos/bannernew.png' width=2000 height=600></p>
<h1 align=center>--------------------------------------------------------------------------</h1>
<h1 align=center>Sistema de Alertas Sísmicas</h1>
<h1 align=center>--------------------------------------------------------------------------</h1>

<h2> Índice:</h2>
<p> 1. Introducción </p> <a href="https://github.com/JPIP8/SISTEMA_DE_ALERTAS_SISMICA/blob/main/README.md#1-introducci%C3%B3n"><p>Int</p></a> 
<p> 2. Objetivos </p>
<p> 3. Calidad de datos </p>
<p> 4. Desarrollo del Proyecto </p>
<p> 5. Conclusiones y Recomendaciones </p>
<p> 6. Stack Tecnológico </p>
<p> 7. Integrantes </p>


<h1 align=center>1. Introducción</h1>
<h2>Quantum Analytics</h2>

<p>Nosotros somos una consultora llamada Quantum Analytics. A partir de la recolección y análisis de datos de movimientos sísmicos en Estados Unidos, Japón y Chile, nuestra consultora utiliza un modelo de machine learning específico para clasificar los movimientos sísmicos y detectar patrones. Al validar la precisión de nuestro modelo, podemos estar seguros de que proporciona resultados confiables para informar a los ciudadanos sobre posibles peligros sísmicos. Finalmente, comunicamos de manera efectiva estos resultados para que la información llegue a la mayor cantidad de personas posible y contribuir así a la seguridad pública.</p>

<h2>Entendimiento de la situación actual</h2>

<p align=center><img src='img/Logos/ciudadAI.png' width=500></p>

<p>Los eventos naturales impredecibles como los sismos se cobran la vidad de cientos de personas cuando suceden, incluso pueden ocasionar otros eventos secundarios como tsunamis, activación de volcanes, peligros nucleares y después que suceden no se conoce como están las estructuras de las edificaciones.
Las alertas actuales con números o colores no brindan mucha información acerca de eventos secundarios o la destructividad de un sismo.
Nos enfrentamos a la necesidad de poder comunicar y alertar a la población de una región, sobre la posibilidad de eventos naturales su destructividad y sus consecuencias.</p>

<p>Este equipo propone un análisis de la situación de los últimos años 2018-2023 y un método de clasificación de sismos.</p>

<h1 align=center>2. Objetivos</h1>
<h2>Alcance</h2>

<p>El alcance del proyecto será para los países: Chile, Estados Unidos y Japón. Se usarán datos de sus respectivos observatorios. No se descarta el uso de datos externos o de otros países para mejorar el modelo. El modelo sera de clasificación.</p>

<h2>KPIs</h2>

<ul>
<li>Kpi: Porcentaje de cobertura efectiva --> objetivo: Ampliar la cobertura de alertas.</li>
<li>Kpi: Promedio de tiempo de reacción --> objetivo: Mejorar el tiempo y tipo de reacción.</li>
<li>Kpi: Promedio de usuarios por plataforma red social --> objetivo: Garantizar la accesibilidad al sistema de alertas.</li>
<li>Kpi: Ratio de presición de alertas actuales --> objetivo: Aumentar la presición por lo tanto la calidad de la clasificación.</li>
</ul>
<p>Todos los kpis serán tomados de manera anual.</p>

<h2>Solución propuesta</h2>
<p>La solución que se propone es una API de alerta que podrá implementarse en distintas redes sociales y aplicaciones móviles, para lograr esto se propone las siguientes tareas.</p>

<p><li>Data engineering: Se extraerán datos de diferentes fuentes, se transformarán y se almacenarán en la nube de amazon AWS.</p>
<p><li>Data analytics: Se usarán los datos almacenados para mostrar la situal actual con un dashboard interactivo.</p>
<p><li>Data science: Se creará un modelo de clasificacián de sismos con un modelo de machine learning.</p>

<h1 align=center>3. Calidad de datos</h1>

<p>Fuente de datos:</br>

<li>Estados unidos: &nbsp <a href='https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2012-01-01%2000:00:00&endtime=2022-12-31%2023:59:59&maxlatitude=50&minlatitude=24.6&maxlongitude=-65&minlongitude=-125&minmagnitude=3&orderby=time-asc'>earthquake.usgs.gov/usa </a></p>

<p><li>Japon: &nbsp <a href='https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2012-01-01%2000:00:00&endtime=2022-12-31%2023:59:59&minlatitude=27.000000&maxlatitude=44.000000&minlongitude=132.780000&maxlongitude=145.530000&&minmagnitude=3&orderby=time-asc'>earthquake.usgs.gov/japan </a></p>

<p><li>Chile: &nbsp <a href='https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2012-01-01%2000:00:00&endtime=2022-12-31%2023:59:59&minlatitude=-56.800000&maxlatitude=-19.000000&minlongitude=-79.000000&maxlongitude=-69.900000&jsonerror=true'>earthquake.usgs.gov/chile </a>
</p>

<p>Mapa de países involucrados.</p>

<p align=center><img src='img/Logos/alcance.jpeg' width=500></p>


<h1 align=center>4. Desarrollo del Proyecto</h1>
<h2>ETL</h2>

<p>Explicar un poco sobre el ETL</p>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam tincidunt feugiat nulla in luctus. Morbi accumsan dapibus justo, vel facilisis enim fermentum vitae. Cras dignissim bibendum metus ac fringilla. Pellentesque mollis magna viverra viverra faucibus. Pellentesque dictum sodales sapien sit amet maximus. Aliquam metus neque, vehicula at eleifend in, rutrum id turpis. Aenean ac odio efficitur sem lobortis molestie. Etiam mattis ac odio vel dignissim. Sed aliquet ante non erat mollis, eu ornare leo volutpat. Proin ac risus id risus egestas malesuada nec nec lacus.</p>

<h2>EDA</h2>

<p>Explicar un poco sobre el EDA</p>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam tincidunt feugiat nulla in luctus. Morbi accumsan dapibus justo, vel facilisis enim fermentum vitae. Cras dignissim bibendum metus ac fringilla. Pellentesque mollis magna viverra viverra faucibus. Pellentesque dictum sodales sapien sit amet maximus. Aliquam metus neque, vehicula at eleifend in, rutrum id turpis. Aenean ac odio efficitur sem lobortis molestie. Etiam mattis ac odio vel dignissim. Sed aliquet ante non erat mollis, eu ornare leo volutpat. Proin ac risus id risus egestas malesuada nec nec lacus.</p>

<h2>Modelo de Machine Learning</h2>

<p>Explicar un poco sobre el Modelo de Machine Learning</p>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam tincidunt feugiat nulla in luctus. Morbi accumsan dapibus justo, vel facilisis enim fermentum vitae. Cras dignissim bibendum metus ac fringilla. Pellentesque mollis magna viverra viverra faucibus. Pellentesque dictum sodales sapien sit amet maximus. Aliquam metus neque, vehicula at eleifend in, rutrum id turpis. Aenean ac odio efficitur sem lobortis molestie. Etiam mattis ac odio vel dignissim. Sed aliquet ante non erat mollis, eu ornare leo volutpat. Proin ac risus id risus egestas malesuada nec nec lacus.</p>

<h2>Visualización</h2>

<p>Explicar un poco sobre la Visualización</p>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam tincidunt feugiat nulla in luctus. Morbi accumsan dapibus justo, vel facilisis enim fermentum vitae. Cras dignissim bibendum metus ac fringilla. Pellentesque mollis magna viverra viverra faucibus. Pellentesque dictum sodales sapien sit amet maximus. Aliquam metus neque, vehicula at eleifend in, rutrum id turpis. Aenean ac odio efficitur sem lobortis molestie. Etiam mattis ac odio vel dignissim. Sed aliquet ante non erat mollis, eu ornare leo volutpat. Proin ac risus id risus egestas malesuada nec nec lacus.</p>

<h1 align=center>5. Conclusiones y Recomendaciones</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam tincidunt feugiat nulla in luctus. Morbi accumsan dapibus justo, vel facilisis enim fermentum vitae. Cras dignissim bibendum metus ac fringilla. Pellentesque mollis magna viverra viverra faucibus. Pellentesque dictum sodales sapien sit amet maximus. Aliquam metus neque, vehicula at eleifend in, rutrum id turpis. Aenean ac odio efficitur sem lobortis molestie. Etiam mattis ac odio vel dignissim. Sed aliquet ante non erat mollis, eu ornare leo volutpat. Proin ac risus id risus egestas malesuada nec nec lacus.</p>

<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam tincidunt feugiat nulla in luctus. Morbi accumsan dapibus justo, vel facilisis enim fermentum vitae. Cras dignissim bibendum metus ac fringilla. Pellentesque mollis magna viverra viverra faucibus. Pellentesque dictum sodales sapien sit amet maximus. Aliquam metus neque, vehicula at eleifend in, rutrum id turpis. Aenean ac odio efficitur sem lobortis molestie. Etiam mattis ac odio vel dignissim. Sed aliquet ante non erat mollis, eu ornare leo volutpat. Proin ac risus id risus egestas malesuada nec nec lacus.</p>

<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam tincidunt feugiat nulla in luctus. Morbi accumsan dapibus justo, vel facilisis enim fermentum vitae. Cras dignissim bibendum metus ac fringilla. Pellentesque mollis magna viverra viverra faucibus. Pellentesque dictum sodales sapien sit amet maximus. Aliquam metus neque, vehicula at eleifend in, rutrum id turpis. Aenean ac odio efficitur sem lobortis molestie. Etiam mattis ac odio vel dignissim. Sed aliquet ante non erat mollis, eu ornare leo volutpat. Proin ac risus id risus egestas malesuada nec nec lacus.</p>


<h1 align=center>6. Stack Tecnológico</h1>

<h3>Planificación y Colaboración</h3>

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


<h1 align=center>7. Integrantes</h1>
<h2>Conecta con Nosotros</h2>

<p><a href="https://www.linkedin.com/in/jhon-velasque-228093211/"><img alt="Jhon" title="Conectar con Jhon" src="https://img.shields.io/badge/Jhon Velasque Durand-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> Data Engineer</p>

<p><a href="https://www.linkedin.com/in/luis-fernando-montero-castro-711b6524b/"><img alt="Luis" title="Conectar con Luis" src="https://img.shields.io/badge/Luis Fernando Montero-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> Data Engineer</p>

<p><a href="https://www.linkedin.com/in/juan-pablo-idrovo-3366a351/"><img alt="Juan Pablo" title="Conectar con Juan Pablo" src="https://img.shields.io/badge/Juan Pablo Idrovo-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> Data Analyst</p>

<p><a href="https://www.linkedin.com/in/esteban-roca-carbajal-5b3957135/"><img alt="Esteban" title="Conectar con Esteban" src="https://img.shields.io/badge/Esteban Roca Carbajal-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> Data Scientist</p>

<p><a href="https://www.linkedin.com/in/juanm-araoz4168/"><img alt="juan" title="Conectar con Juan" src="https://img.shields.io/badge/Juan Manuel Araoz-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> Data Scientist</p>


<h1 align=center>Gracias !</h1>
<h2>Gracias por llegar hasta aquí!</h2>

<p>Esperamos que te haya gustado este proyecto :)</p>
