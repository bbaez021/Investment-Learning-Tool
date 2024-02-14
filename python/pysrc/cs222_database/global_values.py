"""This file contains variables that are used across multiple files"""
import os
from pymongo import MongoClient


cluster = MongoClient(os.getenv("dbKey"))

db = cluster["cs222"]
collection = db["Test1"]

TEST_USER_NAME = "test_for_stock_read"
T_UN_EMAIL = "example@example.com"
TEST_USER_TWO = "user_two"
local_data_download = collection.find_one({"user_name": TEST_USER_NAME})
