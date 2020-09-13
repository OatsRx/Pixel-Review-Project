import os
from flask import Flask, render_template, request, url_for, redirect, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists('env.py'):
    import env

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'pixelReviews'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


# Home
@app.route('/')
def home():
    return render_template('home.html', page_title='Home')


# Get reviews
@app.route('/get_reviews/<game_title>')
def get_reviews(game_title):
    return render_template('getreviews.html', page_title='Reviews',
    reviews=mongo.db.reviews.find({'game_title': game_title}))


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
