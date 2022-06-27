# AirBnB Nightly Price Prediction Overview
* Created a model that predicts the nightly price of an AirBnB to help hosts have an idea of what price they should use.
* Binned features (Host Acceptance Rate & Host Response Rate) that contained percentages (ranging from 0-100%) into 6 bins respectively. 
* Optimized Random Forest, Gradient Boosted Trees, and XGBoost using GridsearchCV to reach the best model.
* Added these 3 best performing model to a Stacking Regressor to create an ensemble which performed even better
* Built a user interface website using flask

## Resources
**Python Version:** 3.9.5  
**Packages:** pandas, numpy, sklearn, xgboost, matplotlib, seaborn, flask, pickle, geopy

## Data Cleaning
The following is a list of changes I made to certain features

* Parse nightly price column to remove $ symbol
* dropped all rows with more than 30 beds
* Parsed bathroom columns and create new column with just number of baths
* added new column with listing description length
* added new column for how many years people have been a host
* created new columns for true/false columns (1's and 0's) --> superhost, identity_verified, instant_book
* remove unecessary columns and rows (number_of_reviews == 0, reviews per month > 30, host_response_time isna, etc.)   



## EDA
Here a few different snapshots from my EDA including a few scatterplot and a heatmap

![alt text](https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/05ee2f9b8f1815f7ffda2d2204c65e3243b4b5b3/eda1.png)=250x250
![alt text](https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/05ee2f9b8f1815f7ffda2d2204c65e3243b4b5b3/eda2.png)=250x250
![alt text](https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/05ee2f9b8f1815f7ffda2d2204c65e3243b4b5b3/eda3.png)=250x250
![alt text](https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/e0dc97a656ec8d56f3f9b0bb67c07caa0b9a0bf7/eda4.png)=250x250



## Model Building 

After EDA I looked into related features a bit further in order to eliminate multicillinearity. Once I was happy with that result, I proceeded to One Hot Encode categorical variable as well as my new created binned variables. Following this, I split the data into train and test sets, using 20% as test size.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried a number of different models:
* **Multiple Linear Regression**
* **Lasso Regression**
* **SVR**
* **Decision Tree**
* **SGD Regressor**
*	**XGBoost** 
*	**Gradient Boosted Trees**
*	**Random Forest**
 

## Model performance
The Stacking Regressor Ensemble Performed the best by just a slight margin compared to the ML models on their own
* **Stacking Regressor**: RMSE = 46.88
*	**XGBoost**: RMSE = 47.28
*	**Gradient Boosted Trees**: RMSE = 48.63
*	**Random Forest**: RMSE = 48.97

## Productionization 
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 
