import numpy as np
from flask import Flask, request, render_template
import pickle
import requests
import geopy
from geopy.geocoders import Nominatim
app = Flask(__name__)

model = pickle.load(open("new_model.pkl", "rb"))

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/capstone_model')
def bnbprice():
    return render_template('bnbprice.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')
#-------------------------- PREDICTION FUNCTION -------------------------#

@app.route('/predict', methods=['POST', 'GET'])
def predict():

    locater = Nominatim(user_agent="MyApp")

    if request.method == 'POST':

        #latitude and longitude
        location = locater.geocode(request.form["City"])
        latitude = location.latitude
        longitude = location.longitude

        # latitude = 38
        # longitude = 104

        #total listings
        host_listings_count = int(request.form['host_listings_count'])

        #beds and bathrooms
        beds = int(request.form['beds'])
        bath_count = float(request.form['bath_count'])

        #min and max nights
        minimum_nights = int(request.form['minimum_nights'])
        maximum_nights = int(request.form['maximum_nights'])

        #30 day avilability
        availability_30 = int(request.form['availability_30'])

        #Review Info
        review_scores_rating = float(request.form['review_scores_rating'])
        reviews_per_month = float(request.form['reviews_per_month'])

        #Length of Description
        desc_len = 500

        #Number of Years being a host
        years_host = int(request.form['years_host'])

        #True/False Fields
        superhost_tf = request.form['superhost_tf']
        if superhost_tf == 'Yes':
            superhost_tf = int(1)
        else:
            superhost_tf = int(0)

        id_verified_tf = request.form['id_verified_tf']
        if id_verified_tf == 'Yes':
            id_verified_tf = int(1)
        else:
            id_verified_tf = int(0)

        instant_book_tf = request.form['instant_book_tf']
        if instant_book_tf == 'Yes':
            instant_book_tf = int(1)
        else:
            instant_book_tf = int(0)

        #Room Type (One Hot Encoded)
        #Entire House/Apt was dropped from Column
        room_type = request.form['room_type']
        if (room_type == 'Shared Room'):
            room_type_Hotel_room = 0
            room_type_Private_room = 0
            room_type_Shared_room = 1

        elif (room_type == 'Hotel Room'):
            room_type_Hotel_room = 1
            room_type_Private_room = 0
            room_type_Shared_room = 0

        elif (room_type == 'Private Room'):
            room_type_Hotel_room = 0
            room_type_Private_room = 1
            room_type_Shared_room = 0

        else:
            room_type_Hotel_room = 0
            room_type_Private_room = 0
            room_type_Shared_room = 0

        #Host Response Time
        #Within a few days or more was dropped from Column
        host_response_time = request.form['host_response_time']
        if (host_response_time == 'Within an Hour'):
            host_response_time_within_an_hour = 1
            host_response_time_within_a_few_hours = 0
            host_response_time_within_a_day = 0

        elif (host_response_time == 'Within a Few Hours'):
            host_response_time_within_an_hour = 0
            host_response_time_within_a_few_hours = 1
            host_response_time_within_a_day = 0

        elif (host_response_time == 'Within a Day'):
            host_response_time_within_an_hour = 0
            host_response_time_within_a_few_hours = 0
            host_response_time_within_a_day = 1

        else:
            host_response_time_within_an_hour = 0
            host_response_time_within_a_few_hours = 0
            host_response_time_within_a_day = 0

        #Binned Host Response Rate
        host_response_rate = float(request.form['host_response_rate'])
        if (host_response_rate > 99.0):
            binned_host_response_1 = 0
            binned_host_response_2 = 0
            binned_host_response_3 = 0
            binned_host_response_4 = 0
            binned_host_response_5 = 0
            binned_host_response_6 = 1

        elif (host_response_rate > 97.0 <= 99.0):
            binned_host_response_1 = 0
            binned_host_response_2 = 0
            binned_host_response_3 = 0
            binned_host_response_4 = 0
            binned_host_response_5 = 1
            binned_host_response_6 = 0

        elif (host_response_rate > 95.0 <= 97.0):
            binned_host_response_1 = 0
            binned_host_response_2 = 0
            binned_host_response_3 = 0
            binned_host_response_4 = 1
            binned_host_response_5 = 0
            binned_host_response_6 = 0

        elif (host_response_rate > 90.0 <= 95.0):
            binned_host_response_1 = 0
            binned_host_response_2 = 0
            binned_host_response_3 = 1
            binned_host_response_4 = 0
            binned_host_response_5 = 0
            binned_host_response_6 = 0

        elif (host_response_rate > 85.0 <= 90.0):
            binned_host_response_1 = 0
            binned_host_response_2 = 1
            binned_host_response_3 = 0
            binned_host_response_4 = 0
            binned_host_response_5 = 0
            binned_host_response_6 = 0

        elif (host_response_rate > 75.0 <= 85.0):
            binned_host_response_1 = 1
            binned_host_response_2 = 0
            binned_host_response_3 = 0
            binned_host_response_4 = 0
            binned_host_response_5 = 0
            binned_host_response_6 = 0

        else:
            binned_host_response_1 = 0
            binned_host_response_2 = 0
            binned_host_response_3 = 0
            binned_host_response_4 = 0
            binned_host_response_5 = 0
            binned_host_response_6 = 0

        #Binned Host Acceptance Rate
        host_acceptance_rate = float(request.form['host_acceptance_rate'])
        if (host_acceptance_rate > 99.0):
            binned_host_acceptance_1 = 0
            binned_host_acceptance_2 = 0
            binned_host_acceptance_3 = 0
            binned_host_acceptance_4 = 0
            binned_host_acceptance_5 = 0
            binned_host_acceptance_6 = 1

        elif (host_acceptance_rate > 97.0 <= 99.0):
            binned_host_acceptance_1 = 0
            binned_host_acceptance_2 = 0
            binned_host_acceptance_3 = 0
            binned_host_acceptance_4 = 0
            binned_host_acceptance_5 = 1
            binned_host_acceptance_6 = 0

        elif (host_acceptance_rate > 95.0 <= 97.0):
            binned_host_acceptance_1 = 0
            binned_host_acceptance_2 = 0
            binned_host_acceptance_3 = 0
            binned_host_acceptance_4 = 1
            binned_host_acceptance_5 = 0
            binned_host_acceptance_6 = 0

        elif (host_acceptance_rate > 90.0 <= 95.0):
            binned_host_acceptance_1 = 0
            binned_host_acceptance_2 = 0
            binned_host_acceptance_3 = 1
            binned_host_acceptance_4 = 0
            binned_host_acceptance_5 = 0
            binned_host_acceptance_6 = 0

        elif (host_acceptance_rate > 80.0 <= 90.0):
            binned_host_acceptance_1 = 0
            binned_host_acceptance_2 = 1
            binned_host_acceptance_3 = 0
            binned_host_acceptance_4 = 0
            binned_host_acceptance_5 = 0
            binned_host_acceptance_6 = 0

        elif (host_acceptance_rate > 60.0 <= 80.0):
            binned_host_acceptance_1 = 1
            binned_host_acceptance_2 = 0
            binned_host_acceptance_3 = 0
            binned_host_acceptance_4 = 0
            binned_host_acceptance_5 = 0
            binned_host_acceptance_6 = 0

        else:
            binned_host_acceptance_1 = 0
            binned_host_acceptance_2 = 0
            binned_host_acceptance_3 = 0
            binned_host_acceptance_4 = 0
            binned_host_acceptance_5 = 0
            binned_host_acceptance_6 = 1

#------------------------------------- MODEL PREDICTION ----------------------------------------- #

        prediction = model.predict([[
            host_listings_count, latitude, longitude, beds,
            minimum_nights, maximum_nights, availability_30,
            review_scores_rating, reviews_per_month, desc_len, years_host,
            bath_count, superhost_tf, id_verified_tf, instant_book_tf,
            room_type_Hotel_room, room_type_Private_room,
            room_type_Shared_room, host_response_time_within_a_day,
            host_response_time_within_a_few_hours,
            host_response_time_within_an_hour, binned_host_response_1,
            binned_host_response_2, binned_host_response_3,
            binned_host_response_4, binned_host_response_5,
            binned_host_response_6, binned_host_acceptance_1,
            binned_host_acceptance_2, binned_host_acceptance_3,
            binned_host_acceptance_4, binned_host_acceptance_5,
            binned_host_acceptance_6
        ]])

        output=round(prediction[0], 2)

        return render_template('bnbprice.html',prediction_text="The Predicted Price for the AirBnB is ${}".format(output))

    return render_template("bnbprice.html")


if __name__ == "__main__":
    app.run(debug=True)