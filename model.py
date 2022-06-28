import pandas as pd

#read in master df for all cleaned data
df = pd.read_csv('final_df.csv')

## Import ML libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import StackingRegressor

import pickle

# Define our X and y features and split into training/test sets
X = df.drop(['Unnamed: 0', 'nightly_price'], axis=1)
y = df['nightly_price'].values

print(X.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#define the ML models used
rf = RandomForestRegressor(max_depth=50, n_estimators=530, min_samples_leaf=2, min_samples_split=2)

gbt = GradientBoostingRegressor(learning_rate=0.11, max_depth=20, n_estimators=1100, min_samples_split=5,
                               min_samples_leaf=24)

xg = XGBRegressor(learning_rate=0.1, max_depth=10, n_estimators=730, min_child_weight=1, gamma=0.4,
                 colsample_bytree=0.7)

#define the stacking ensemble used for prediction
final_model = StackingRegressor(estimators=[('rf', rf), ('gbt', gbt), ('xg', xg)],
                              final_estimator=LinearRegression())

print('fitting next')

final_model = final_model.fit(X_train.values, y_train)

pickle.dump(final_model, open('new_model.pkl', 'wb'))