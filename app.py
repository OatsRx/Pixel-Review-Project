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


# Edit review
@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    the_review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    all_games = mongo.db.games.find()
    all_platforms = mongo.db.platforms.find()
    reviews = mongo.db.reviews.find()
    return render_template('editreview.html', review=the_review,
    all_games=all_games, all_platforms=all_platforms, reviews=reviews, page_title='Edit Review')


# Update edited review
@app.route('/update_review/<review_id>', methods=['POST'])
def update_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    reviews = mongo.db.reviews
    reviews.update({"_id": ObjectId(review_id)},
    {
        'game_title': request.form.get('game_title'),
        'platform_name': request.form.get('platform_name'),
        'hours_played': request.form.get('hours_played'),
        'review_text': request.form.get('review_text')
    })
    return redirect(url_for('home', review=review))


# Deleting review
@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('delete_confirm'))


# Delete confirmation
@app.route('/delete_confirm')
def delete_confirm():
    return render_template('deleteconfirm.html', page_title='Deleted')


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
