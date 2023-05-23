<p align=center><img src='DTS_img/Banner-en.png' width=2000 height=600></p>

<h1 align=center>Machine Learning</h1>


<h2>Model</h2>

<p>We choose the model called 'Kmeans', it is an unsupervised model based on clustering and. That means the data will be grouped based on features relations, similarities and it does not need correct labeled data to train it. The following picture depict the idea.</p>

<p align=center><img src='DTS_img/kmeansgraph.png' width=800 height=600></p>

<h2>Variables</h2>

<p>Variables have been chosen based on its importance and correlation. they are:</p>

<ul>
<li>idcountry</li>
<li>mag</li>
<li>tsunami</li>
<li>depth</li>
</ul>

<p>We based the selection on the following headmap.</p>
<p align=center><img src='DTS_img/variablesCorrelation.png' width=600 height=600></p>

<h2>Clusters 'elbow method'</h2>

<p>A fundamental step for any unsupervised algorithm is to determine the optimal number of clusters into which the data may be clustered. Since we do not have any predefined number of clusters in unsupervised learning. We tend to use some method that can help us decide the best number of clusters.  In the case of K-Means clustering, we use Elbow Method for defining the best number of clustering. </br>'Elbow graph'</p>

<p align=center><img src='DTS_img/cluster_selection.png' width=600 height=600></p>


<h2>Open and use the model</h2>

<p>The model is saved already trained as modelo_ml.pickle file, instructions to open and use it are:</p>

<p align=center><img src='DTS_img/open_and_use_ml.png' width=1200 height=550></p>


<h2>Testing performance</h2>

<p>The test was made using <b>seismicTest.csv</b> file which contains only dangerous events, the model must be able to label with 0 and 2 at least 90% of the total.</p>

<p align=center><img src='DTS_img/seismicTestPic.png' width=1000 height=750></p>