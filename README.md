[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/SGWUF1eE)
# Generic Real Estate Consulting Project 31 README.md

## Team Members: 
1. `CLARISSA ARDELIA SO, 1275582`
2. `EDWIN IGOR BROTOATMODJO, 1275566`
3. `PATRICK POON PAN, `
4. `VANESSA GRACIA TAN, 1297696`
5. `WILLIAM CONLON, 1169893`

**Research Goal:** Our reserach goal is to determine and analyse the most liveable and affordable property suburb using the predicted growth, appropriate metrics and important features to provide insights and helps to investors in choosing best property to invest. 

To run the pipeline, please visit the `notebooks` and `scipts` directory and run the files in this order:
1. `web_scrape.py`: This script scrapes the property data from `domain.com.au` including the corresponding features and save it to the `dataset` under the`data/raw` directory.
2. `preprocess.ipynb`: This notebook details all preprocessing steps of the raw property data and outputs it to the `clean_data.csv` under the `data/landing` directory.
3. `trainstation_maps.ipynb`: This notebook retrieves the location and maps the geometry points of the train stations in Victoria and output it to the `train_station.csv` under the `data/landing` directory.
4. `tramstops_maps.ipynb`: This notebook retrieves the location and maps the geometry points of the tram stops in Victoria and output it to the `tram_stop.csv` under the `data/landing` directory.
5. `places_data.ipynb`: This notebook collects the landmarks in Melbourne region including `Church`, `Facitilies (Parks)`, `Places of Interest`, `Office`, and `other landmarks`. The output is `melb_landmarks.csv` under the `data/landing` directory.
6. `ABS.ipynb`: This notebook retrieves and preprocess the relevant ABS data and output it as `2021ABS.csv` in `data/landing` directory.
7. `joining.ipynb`: This notebook merges the property data and the ABS data and output it as `Property_external.csv` under the `data/landing` directory.
8. `get_long_lat.ipynb`: This notebook geocodes the longitude and latitude of each property and output the geometry points as `geometry.csv` under the `data/landing` directory and `geometry_property.csv` under the `data/curated` directory.
9. `distance.ipynb`: This notebook calculates the distance by car between the properties and aminities. The output is saved as `places_property.csv` under the `data/curated` directory.
10. `preliminary_analysis.ipynb`: This notebook is used to conduct preliminary analysis of the curated `geometry_property.csv` and `places_property.csv`.
11. `price_affected.ipynb`: 
12. `feature_selection.ipynb`: This notebook is used to run the model for feature selection of our data for the first question. 
13. `predicted_growth.ipynb`: This notebook conducts analysis to calculate the predicted growth of our chosen suburb to answer the second question.
14. `liveability.ipynb`: This notebook analyses the most liveable and affordable suburbs to answer the third question. 