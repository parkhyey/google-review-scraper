## Google Review Scraper Microservice

This microservice provides Google reviews and star ratings scraped into a JSON string where the key ‘rating’ is the number of the star ratings and the key ‘text’ is the review text.

  e.g.)
  
    [{"rating":5,"text":"We booked our Maldives honeymoon through Maldives Resorts and we were very pleased with it. They handed all our many questions and provided great accommodation for a good price."},
    {"rating":5,"text":"loved It so much!!!!!! saw a couple of sharks. but it was bloody fantastic"}]

#### # Sample Integration
![image](https://user-images.githubusercontent.com/71689421/145152941-1bfa7eb5-fd1f-4be1-8860-1ea2ede602b7.png)

## How to run Flask script persistantly
#### # To run gunicorn:

  Install virtual environment and 
    python3 -m venv env

    source ./env/bin/activate 

    pip3 install -r requirements.txt

    pip3 install gunicorn

    export FLASK_APP=app.py

    gunicorn --bind 0.0.0.0:<your-desired-port-here> wsgi:app -D

#### # To kill gunicorn:
  ps ax | grep gunicorn
  
      13067 ?        S      0:00 /nfs/stak/users/yourname/foldername/env/bin/python3 /nfs/stak/users/yourname/foldername/env/bin/gunicorn --bind 0.0.0.0:12345 wsgi:app -D
  
  kill 13067   
  
  You will see 4 or 5 digit integers on the left, and you might also see your username if you read further down the line. The very first number is the number of the main gunicorn process we want to kill. 
