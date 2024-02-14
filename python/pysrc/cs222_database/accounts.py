"""Collections of all functions relating to account creation, editing, and deletion"""
from email_validator import validate_email, EmailNotValidError
import python.pysrc.cs222_database.global_values as glb


def create_account(user_name, email, password):
    """creates accounts based on given parameters. If existent, account will not be made"""
    check_name = glb.collection.find_one({"user_name": user_name})
    if check_name is None and check_valid_email(email) != "INVALID":
        glb.collection.insert_one({"user_name": user_name, "email": email,
                                   "password": password, "all_stocks": [],
                                   "money": 500.00, "safe_mode": False,
                                   "watchlist_stock_id": []})
        return True
    return False


def delete_account(user_name, password):
    """removes account from database given username and password"""
    if glb.collection.find_one({"user_name": user_name, "password": password}) is None:
        return False
    glb.collection.delete_one({"user_name": user_name, "password": password})
    return True


def change_user_name(user_name, new_user_name):
    """Changes account's username if possible"""
    if glb.collection.find_one({"user_name": new_user_name}) is None and " " not in new_user_name:
        glb.collection.update_one({"user_name": user_name},
                                  {"$set": {"user_name": new_user_name}})
        return True
    return False


def change_email_address(user_name, new_email):
    """changes account's email address is possible"""

    if check_valid_email(new_email) != "INVALID":
        glb.collection.update_one({"user_name": user_name},
                                  {"$set": {"email": new_email}})
        return True
    return False


def reset_password(user_name, password, new_password):
    """changes password of account if possible"""
    download = glb.collection.find_one({"user_name": user_name})
    if download["password"] == password:
        glb.collection.update_one({"user_name": user_name, "password": password},
                                  {"$set": {"password": new_password}})
        return True
    return False


def reset_account(user_name, password):
    """resets account's portfolio back to default"""
    if glb.collection.find_one({"user_name": user_name}) is not None:
        glb.collection.update_one({"user_name": user_name, "password": password},
                                  {"$set": {"all_stocks": [], "money": 500.00,
                                            "safe_mode": True, "watchlist_stock_id": []}})
        return True
    return False


def check_valid_email(email):
    """checks if email address is valid"""
    try:
        check_for_validity = validate_email(email)
        email = check_for_validity["email"]
    except EmailNotValidError:
        return "INVALID"
    if glb.collection.find_one({"email": email}) is None:
        return email
    return "INVALID"


def download_other_user_data(user):
    """download user data without compromising information"""
    data = glb.collection.find_one({"user_name": user}, {"email": 0, "password": 0, "safe_mode": 0,
                                                         "watchlist_stock_id": 0})
    return data
