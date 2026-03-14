from flask import Flask, render_template, request, redirect, url_for

from pymongo import MongoClient

from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Connection

client = MongoClient("mongodb://localhost:27017/")

db = client["ecommerce_db"]

collection = db["products"]

# HOME PAGE - Display Products

@app.route('/')

def index():

products = collection.find()

return render_template('index.html', products=products)

# ADD PRODUCT

@app.route('/add', methods=['GET', 'POST'])

def add():

if request.method == 'POST':

name = request.form['name']

price = request.form['price']

stock = request.form['stock']

collection.insert_one({

"name": name,

"price": float(price),

"stock": int(stock)

})

return redirect(url_for('index'))

return render_template('add.html')
