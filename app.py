from flask import Flask, jsonify
import googlemaps
import os
from flask_cors import CORS

# Google review scraper
# Takes place_id and respond JSON data of reviews and ratings of the place
# Request format = url/ + place_id

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    # general info page
    text = "To use, add '/place_ID' after the above url. You can find place ID at https://developers.google.com/places/place-id. For example, try '/ChIJW69I7FhZwokR61IbDPnsqTo'"
    return text

@app.route('/<place_id>', methods=['GET'])
def reviews(place_id):
    # use personal google API key
    gmaps = googlemaps.Client(key='AIzaSyDj7clChH8kmGTe5uga8JUz21Q0AAm_9iA')  
    
    # find place_id at https://developers.google.com/places/place-id
    place = gmaps.place(place_id=place_id) 
    # empty list to hold dictionaries of reviews
    reviews = []  

    # pull only reviews and star ratings
    for i in range(len(place['result']['reviews'])):
        text = place['result']['reviews'][i]['text']
        rating = place['result']['reviews'][i]['rating']
        
        # customize response
        # set star ratings criteria
        if rating >= 4:  
            reviews.append({'rating': rating,
                            'text': text})
        # number of reviews to retrieve
        if len(reviews) == 10:  
            break
    response = jsonify(reviews)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Listener
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
