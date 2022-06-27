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

*	Parsed numeric data out of salary 
*	Made columns for employer provided salary and hourly wages 
*	Removed rows without salary 
*	Parsed rating out of company text 
*	Made a new column for company state 
*	Added a column for if the job was at the company’s headquarters 
*	Transformed founded date into age of company 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * R  
    * Excel  
    * AWS  
    * Spark 
*	Column for simplified job title and Seniority 
*	Column for description length 

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/salary_by_job_title.PNG "Salary by Position")
![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/positions_by_state.png "Job Opportunities by State")
![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/correlation_visual.png "Correlations")

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
