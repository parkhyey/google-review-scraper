## Google Review Scraper Microservice

### To run gunicorn:

  python3 -m venv env

  source ./env/bin/activate 

  pip3 install -r requirements.txt

  pip3 install gunicorn

  export FLASK_APP=app.py

  gunicorn --bind 0.0.0.0:<your-desired-port-here> wsgi:app -D

### To kill gunicorn:
  ps ax | grep gunicorn
  
      13067 ?        S      0:00 /nfs/stak/users/yourname/foldername/env/bin/python3 /nfs/stak/users/yourname/foldername/env/bin/gunicorn --bind 0.0.0.0:12345 wsgi:app -D
  
  kill 13067   
  
  You will see 4 or 5 digit integers on the left, and you might also see your username if you read further down the line. The very first number is the number of the main gunicorn process we want to kill. 
