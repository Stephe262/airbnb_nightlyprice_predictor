# AirBnB Nightly Price Prediction Overview
* Created a model that predicts the nightly price of an AirBnB to help hosts have an idea of what price they should use.
* Binned features (Host Acceptance Rate & Host Response Rate) that contained percentages (ranging from 0-100%) into 6 bins respectively. 
* Optimized Random Forest, Gradient Boosted Trees, and XGBoost using GridsearchCV to reach the best model.
* Added these 3 best performing model to a Stacking Regressor to create an ensemble which performed even better
* Built a client facing API using flask

## Code and Resources Used 
**Python Version:** 3.9.5  
**Packages:** pandas, numpy, sklearn, xgboost, matplotlib, seaborn, flask, pickle, geopy
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  

## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

* Parse nightly price column to remove $ symbol
* dropped all rows with more than 30 beds
* Parsed bathroom columns and create new column with just number of baths
* added new column with listing description length
* added new column for how many years people have been a host
* created new columns for true/false columns (1's and 0's) --> superhost, identity_verified, instant_book
* remove unecessary columns and rows (number_of_reviews == 0, reviews per month > 30, host_response_time isna, etc.)   



## EDA
I looked at the distributions of the data and the value counts for the various categorical variables as well as a heatmap 

![alt text](https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/05ee2f9b8f1815f7ffda2d2204c65e3243b4b5b3/eda1.png)
![alt text](https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/05ee2f9b8f1815f7ffda2d2204c65e3243b4b5b3/eda2.png)
![alt text](https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/05ee2f9b8f1815f7ffda2d2204c65e3243b4b5b3/eda3.png)
![alt text](https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/05ee2f9b8f1815f7ffda2d2204c65e3243b4b5b3/eda4.png)



## Model Building 

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**XGBoost** 
*	**Gradient Boosted Trees**
*	**Random Forest**
 

## Model performance
The Stacking Regressor Ensemble Performed the best by just a slight margin compared to the ML models on their own
* **Stacking Regressor**: RMSE = 
*	**XGBoost**: RMSE = 
*	**Gradient Boosted Trees**: RMSE = 
*	**Random Forest**: RMSE = 

## Productionization 
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 
