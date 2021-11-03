from flask import Flask, jsonify
import os
import googlemaps

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    text = "To use, add '/place_ID' after the above url. You can find place ID at https://developers.google.com/places/place-id. For example, try '/ChIJW69I7FhZwokR61IbDPnsqTo'"
    return text

@app.route('/<place_id>', methods=['GET'])
def reviews(place_id):
    gmaps = googlemaps.Client(key='AIzaSyDj7clChH8kmGTe5uga8JUz21Q0AAm_9iA')
    
    place = gmaps.place(place_id=place_id)  # Find placeID @: https://developers.google.com/places/place-id
    reviews = []  # empty list to hold dictionaries of reviews

    for i in range(len(place['result']['reviews'])):
        text = place['result']['reviews'][i]['text']
        rating = place['result']['reviews'][i]['rating']
        
        if rating >= 5:  # retrieve 5-star reviews only
            reviews.append({'rating': rating,
                            'text': text})
        if len(reviews) == 2:  # number of reviews to display
            break
    return jsonify(reviews)

# Listener
if __name__ == "__main__":
    #app.run(host="flip3.engr.oregonstate.edu", port=33133)
    port = int(os.environ.get('PORT', 33133))
    app.run(port=port, debug=True) 
