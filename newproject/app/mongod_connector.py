import pymongo

url = "mongodb://localhost:27017/"
client = pymongo.MongoClient(url)
db = client['local']

# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client['']






# # settings.py
# # from pymongo import mo
# # Import pymongo
# from pymongo import MongoClient

# # MongoDB connection settings
# MONGO_DB_NAME = 'your_database_name'
# MONGO_DB_USERNAME = 'your_username'
# MONGO_DB_PASSWORD = 'your_password'
# MONGO_DB_HOST = 'localhost'
# MONGO_DB_PORT = 27017  # Default MongoDB port

# # Connect to MongoDB using pymongo
# client = MongoClient(host=MONGO_DB_HOST, port=MONGO_DB_PORT)
# db = client[MONGO_DB_NAME]

# # If your MongoDB server requires authentication
# # db.authenticate(MONGO_DB_USERNAME, MONGO_DB_PASSWORD)

# # Django database settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.dummy',  # Dummy engine since we're using pymongo directly
#         'NAME': MONGO_DB_NAME,
#         'USER': MONGO_DB_USERNAME,
#         'PASSWORD': MONGO_DB_PASSWORD,
#         'HOST': MONGO_DB_HOST,
#         'PORT': MONGO_DB_PORT,
#     }
# }
