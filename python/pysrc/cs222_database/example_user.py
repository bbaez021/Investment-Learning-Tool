"""File used exclusively to set up testing environment"""
import os
from pymongo import MongoClient

cluster = MongoClient(os.getenv("dbKey"))

db = cluster["cs222"]
collection = db["Test1"]

TEST_USER_NAME = "test_for_stock_read"
TEST_USER_TWO = "user_two"


def fill_collection():
    """Clears collection and the fills with default data used for testing"""
    db.collection.drop()
    collection.insert_one({"user_name": TEST_USER_NAME, "email": "example@example.com",
                           "password": "password",
                           "all_stocks": [
                               {"stock_id": "AMZN", "val_at_purchase": 115.15, "qty": 1},
                               {"stock_id": "MSFT", "val_at_purchase": 237.45, "qty": 1},
                               {"stock_id": "AAPL", "val_at_purchase": 150.77, "qty": 1},
                               {"stock_id": "QSR", "val_at_purchase": 54.97, "qty": 1}
                           ], "money": 3000.00, "safe_mode": False,
                           "watchlist_stock_id": ["HPQ", "TSLA", "ACER", "AAPL"]
                           })

    collection.insert_one({"user_name": TEST_USER_TWO, "email": "user2@example.com",
                           "password": "12345",
                           "all_stocks": [
                               {"stock_id": "PZZA", "val_at_purchase": 73.45, "qty": 8},
                               {"stock_id": "MMM", "val_at_purchase": 113.22, "qty": 1},
                               {"stock_id": "CAKE", "val_at_purchase": 29.10, "qty": 2}],
                           "money": 3.50, "safe_mode": True, "watchlist_stock_id": ["BUD", "HEINY", "TAP"]})
