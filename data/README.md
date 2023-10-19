# Datasets

This `Readme.md` provides the information of our chosen datasets corresponding to our analysis. 

## Raw Data
This `data/raw` directory contains all of our main raw internal and external datasets for our `Real Estate Project Analysis`. 

1. `ABS SA2 Inner Melbourne\`: This folder contains ABS details for each SA2 Inner Melbourne region in the form of .csv files.

2. `dataset\`: This folder contains rental property details that were web scraped from `domain.com.au` website for each page in the form of .csv files.

3. `PTV METRO TRAIN STATION\`: This folder contains the full information on PTV Metro Train Station including the shape file and the geometry data.

4. `PTV METRO TRAM STOP\`: This folder contains the full information on PTV Metro Tram Stop including the shape file and the geometry data.

5. `crime_count.csv`: This data contains the number of crimes in each suburb.

6. `melb_landmarks.csv`: This data contains the location of melbourne landmarks, such as public facilities.

7. `Moving annual rent by suburb - March quarter 2023.csv`: This data contains a quarterly annual rent prices from March 2000 to March 2023.

8. `school_locations.csv`: This data contains the location of schools in Melbourne.

9. `recorded_offence.csv`: This data contains the number of offence recorded by suburb.


## Landing Data
After cleaning and transforming the `raw data`, the output of each transformation is saved under `data/landing` directory. 

1. `clean_data.csv`: This data contains property data after some simple preprocessing (removing missing rows and extracting relevant features).

2. `2021ABS.csv`: This data contains ABS data after some simple preprocessing (removing missing rows and extracting relevant data and features).

3. `train_station.csv`: This data contains the relevant features extracted from `raw PTV METRO TRAIN STATION`.

4. `tram_stop.csv`: This data contains the relevant features extracted from `raw PTV METRO TRAM STOP`.

5. `Property_external.csv`: This data is the output after joining both `property clean data` and `ABS data`.

6. `geometry.csv`: This dataset consists of the point geometry of each property extracted from geocoding each address. 


## Curated Data
Finally, after further preprocess the `landing data`, datasets that ready for analysis are kept under `data/curated`.

1. `geometry_property.csv`: This dataset contains the property addresses along with the corresponding longitude and latitude extracted through geocoding. 

2. `places_property.csv`: This dataset consists of the property complete data, including number of transportation within desired distance, distance to CBD, number of landmarks within desired distance, and geometry points (latitude and longitude).

3. `complete_dataset.csv`: This dataset is the extended version of `places_property.csv`, which consists of information about the property including the important features. 

4. `liveable_growth_rate.csv`: This dataset consists of information on the growth rate of liveable suburb calculated in `liveability.ipynb`

5. `10_growth_suburbs.csv`: This dataset consists of information about the top 10 highest predicted growth rate forecasted in `predicted_growth.ipynb`. 