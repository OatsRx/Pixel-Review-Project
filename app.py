import os
from flask import Flask, render_template, request, url_for, redirect, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
if os.path.exists('env.py'):
    import env

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'pixelReviews'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.secret_key = os.getenv('secret_key')

mongo = PyMongo(app)


# Home
@app.route('/')
def home():
    return render_template('home.html', page_title='Home')


#########LOGIN SYSTEM START#########
# Register
@app.route('/register')
def register():
    return render_template('register.html', page_title='Register')


# Registered data pushed to mongo
@app.route('/register_push', methods=['POST'])
def register_push():

    """ if the request method is POST we'll
    search the database for existing users that match """
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        """ if there is no matching user we can
        then make a new user and hash their password """
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('logged_in'))

        return render_template('userexists.html', page_title='User Error')

    return render_template('loggedin.html')


# Login
@app.route('/login')
def login():
    return render_template('login.html', page_title='Login')


# Login data queried to mongo
@app.route('/login_push', methods=['POST', 'GET'])
def login_push():

    """ first we search the database of users
    to match data """
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'),
        login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('logged_in'))

    return 'Incorrct Username/Password'


@app.route('/logged_in')
def logged_in():
    if 'username' in session:
        return render_template('loggedin.html', page_title='Logged In')


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
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=False)
