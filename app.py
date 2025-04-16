from flask import Flask, render_template, jsonify, request, redirect
from dotenv import load_dotenv
from pymongo import MongoClient, errors
import os
import hashlib

load_dotenv()
app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
collection = db[os.getenv("COLLECTION")]

base_url = os.getenv("VERCEL_URL", "http://127.0.0.1:5000")

@app.route('/health')
def health():
    try:
        client.admin.command('ping')
        return jsonify({"status": "MongoDB is alive!"}), 200
    except Exception as e:
        return jsonify({"status": "MongoDB not reachable", "error": str(e)}), 500


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_data', methods=['POST'])
def add_data():
    if collection is None:
        return jsonify({"error": "No database connection found"}), 500
    collection.insert_one({"name": "url shortener"})
    
    return jsonify({"message": "Data added successfully"}), 


def hash_and_sum_ascii(input_url):
    sha256_hash = hashlib.sha256(input_url.encode('utf-8')).hexdigest()
    ascii_sum = sum(ord(char) for char in sha256_hash)

    return ascii_sum*len(input_url)

@app.route('/add_url', methods=['POST'])
def add_url():
    if collection is None:
        return jsonify({"error": "No database connection found"}), 500
    og_url = request.form['url']
    url_sum = hash_and_sum_ascii(og_url)
    short_url = f'{base_url}/short/{url_sum}'
    collection.insert_one({
        "og_url": og_url,
        "short_url": short_url,
        "url_sum": url_sum,
    })
    message = f'The short-url is {short_url}'
    return render_template('index.html', short_url=short_url)


@app.route('/short/<int:url_sum>')
def get_url(url_sum):
    if collection is None:
        return jsonify({"error": "No database connection found"}), 500

    data = collection.find_one({"url_sum": url_sum})

    if data:
        long_url = data["og_url"]
        return redirect(long_url)
    
    # error = 'No long URL for it.'
    
    return render_template('index,html')
          

if __name__ == '__main__':
    app.run(debug=True)


