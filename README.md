# AirBnB Nightly Price Prediction Overview
* Created a model that predicts the nightly price of an AirBnB to help hosts have an idea of what price they should use.
* This model looks at data from various different cities across the US (Austin, Boston, Chicago, Denver, Nashville, Portland, San Diego, Asheville, Seattle, NYC, New Orleans, Los Angles, and Dallas)
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

<img src="https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/05ee2f9b8f1815f7ffda2d2204c65e3243b4b5b3/eda1.png" width=1000 height=500> <img src="https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/05ee2f9b8f1815f7ffda2d2204c65e3243b4b5b3/eda2.png" width=500 height=500> 
<img src="https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/05ee2f9b8f1815f7ffda2d2204c65e3243b4b5b3/eda3.png" width=500 height=500>
<img src="https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/e0dc97a656ec8d56f3f9b0bb67c07caa0b9a0bf7/eda4.png" width=500 height=500>



## Model Building 

After EDA I looked into related features a bit further in order to eliminate multicillinearity. Once I was happy with that result, I proceeded to One Hot Encode categorical variable as well as my new created binned variables. Following this, I split the data into train and test sets, using 20% as test size.

I tried three different models and evaluated them using Root Mean Squared Error. 

List of models:
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

Interestingly enough, I ran the feature importance function from XGBoost and discovred that Longitude and Latitude were the most important. Although this is not very surprising as real estate prices fluctuate throughout the US. I feel that I could perhaps acheive a more accurate model if I collected more data which was more representative of most all cities throughout the US. Also, I perhaps could fine tune some of the features a bit more and remove clear outliers in the data. I would have like to see a much smaller RMSE number, in the range of 10-20. 

<img src="https://github.com/Stephe262/airbnb_nightlyprice_predictor/blob/b3b89e65307e2c16df5e591ba0c502bfcdcca088/feature_importance.png" width=1000 height=500>

## Productionization 
I built a Flask interface in order to host this model. This will take you to an interactive display in which AirBnB hosts can enter in their information in order to receive a price for their AirBnB.
