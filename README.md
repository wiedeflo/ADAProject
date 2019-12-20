# The Chicago Case: Food inspections in a divided city

# Website
Our Data Story is available at : https://wiedeflo.github.io/ADAProject/

# Note
In the notebook and the data story, maps and plotly plots don't always show on Chrome, however they should be displayed on Firefox. We put the ```project.html``` in the repo so that you can see them in case they don't show in your notebooks. 

# Abstract
Chicago is a notoriously unequal city: Passengers travelling on its red metro line have life expectancies that vary by 30 years depending on their stop, according to The Economist. We want to investigate how geographical socio-economic divisions in Chicago reflect in food inspections in two ways: results to food inspections, and quantities of food inspections. By analysing results to food inspections, we want to find out which areas are performing better and which are performing worse, and compare this to measures of the socio-economic divide. By inspecting the quantity of inspections per area, we hope to gain insight on a potential bias in the choice of inspected establishment and whether the chances of an establishment getting inspected depend only on its performance or also on its location.


# Research questions
How does the intense geographical socio-economic inequality that exists in Chicago, and which we can measure looking at indicators such as income or life expectancy, show in the results to the food inspections being carried out?  

How to best analyse the violations that are reported when an establishment doesn’t pass an inspection?

Is there a correlation between the type of facility being inspected (restaurant, hospital, tavern) and the results of the inspection?

Is there a bias in the amount of inspections for some establishment, or does it only depend on its performance?

# Dataset
1) Chicago Food Inspections: A dataset providing the facility, the time, the latitude and longitude, the result (pass, or fail, and risk level) and a short comment on the inspection.
https://www.kaggle.com/chicago/chicago-food-inspections
Note : this database is updated every friday, we downloaded ours after the update of the 18th of October.

2) Cencus Data - Seleted socio-economic indicators in Chicago, 2008 - 2012 (https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2). This dataset provides information on income per capita per area.

3) Public Health Statistics- Life Expectancy By Community Area Health (https://data.cityofchicago.org/Health-Human-Services/Public-Health-Statistics-Life-Expectancy-By-Commun/qjr3-bm53). This dataset provides information on life expectancy per capita per area.

4) We download the Chicago community areas bounderies on :
https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6
Click on "export", then download the Shapefile format and the GEOJson format, and put the downloaded folder in "data". The 4 files downloaded have random hashes appended to their names, so rename them to match "geo_export" leaving the extension.

The city of Chicago offers a wide variety of datasets of which we might take advantage in the future, and which might allow us to analyse other aspects of geographical inequality in Chicago, such as crime, population density, education, etc.

# A list of internal milestones up until project milestone 2
1) Download all 3 datasets. Clean them if needed. Report basic statistics on the important fields.

2) Analyse the Chicago food inspections: Where do they happen most frequently ? Inspect the geographical food inspections result & quantity per area.

3) Analyse the socio-economic indicators: determine how the rich/poor areas are divided in Chicago.

# A list of internal milestones up until project milestone 3
1) Description of the violations and how they are influencing the risk of an establishment.

2) See what other interesting analysis can be done by combining the databases.

3) Use Machine Learning to cluster establishments or predict their pass/failure evaluation.

4) Write a data story/report.

# Contributions
Florian Wiedemair : parts of webscraping unknown locations, parts of map visualization, parts of website design, parts of written analysis\
Mohamed Ndoye : \
Raphael Strebel : Cleaning of databases, parts of written analysis in the data story, parts of webscraping unknown locations, interactive "per capita income wrt households below poverty line" plot\
Jose Garrido Ramas : Parts of written analysis in the data story, ML part to predict if a facility will get inspected, 
correlation between socioeconomic indicators, correlation between socio economic indicators and food inspection results.\
Everyone will work on the final presentation.

# Structure of the code
The data is in the ```data``` folder, the code is in the ```src``` folder. The ```src/project.ipynb``` notebook contains the pipeline of the project, with multiple references to ```src/utils``` where helper functions can be found (to avoid overloading the notebook).

# Questions for TAa
1) Do you think the direction we follow is the right one ?
2) Any ideas for further analysis ?
3) We have many maps, do you think some of them are unnecessary ?
4) About machine learning we plan on doing for the next milestone, do you have any advice on what we proposed, or any ideas what else we could do ?
5) Any feedback is more than welcome :) 

# Libraries
pandas \
numpy \
geopandas \
vincent \
folium \
json \
math \
re \
datetime \
geopy \
shapely \
requests \
os \
plotly

# Authors
Florian Wiedemair, Mohamed Ndoye, Raphael Strebel, Jose Garrido Ramas