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


# Write review
@app.route('/write_review')
def write_review():
    return render_template('writereview.html', games=mongo.db.games.find(),
    platforms=mongo.db.platforms.find(), page_title='Write Review')


# Insert new review
@app.route('/insert_review', methods=['POST'])
def insert_review():
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
