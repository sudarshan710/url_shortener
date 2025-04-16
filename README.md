# URL Shortener

### Overview
The URL Shortener is a simple yet secure URL shortening service built using Flask and MongoDB. The core idea behind this project is to shorten long URLs while ensuring that each shortened URL is unique and secure. The project uses SHA256 encryption to hash original URLs and generates an ASCII sum based on the hash. The uniqueness of the shortened URL is enhanced by multiplying the hash with the length of the original URL, ensuring that each shortened URL is not only unique but also more difficult to guess.

### Features
- Encrypted URLs: The original long URLs are encrypted using the SHA256 hashing algorithm.
- ASCII Sum Generation: An ASCII sum is created from the hashed URL to further enhance the uniqueness.
- Unique Identifier: The hashed URL is multiplied by the length of the original URL to strengthen its uniqueness, and the result is used as an ID for database lookups.
- Database Integration: The unique shortened URLs and their corresponding original URLs are stored in MongoDB, ensuring fast and efficient retrieval.

### Tech Stack
- Flask: Web framework used to build the backend API.
- MongoDB: NoSQL database used to store the mappings of shortened URLs and original URLs.

## Installation
### Prerequisites
- Python 3.9 or above
- MongoDB (local or cloud-based)

### Step 1: Clone the Repository
```
git clone https://github.com/sudarshan710/url_shortener.git
cd url-shortener
```

### Step 2: Install Dependencies
Make sure you have ``pip`` installed, then run the following command:
```
pip install -r requirements.txt
```
### Step 3: Set Up MongoDB
Ensure MongoDB is installed and running. If you're using MongoDB Atlas, create a cluster and get your connection string. Then, set up the following environment variables:
``
MONGO_URI="your_mongodb_connection_string"
``
### Step 4: Run the Application
```
flask run
```
or
```
python3 app.py
```
