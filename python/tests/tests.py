"""Test cases for functions.py"""
from python.pysrc.cs222_database import functions as fn
from python.pysrc.cs222_database import example_user as start
from python.pysrc.cs222_database import global_values as glb
from python.pysrc.cs222_database import accounts as acc


def test0_clear_database():
    """Clears and sets up database for testing purposes. Will only fail if invalid"""
    glb.collection.drop()
    start.fill_collection()
    fn.update_local_user_data(glb.TEST_USER_NAME)


def test1_existing_user():
    """Tests if a user exists"""
    non_existing_user = acc.download_other_user_data("my_user")
    assert non_existing_user is None

    existing_user_name = "user_two"
    existing_user = acc.download_other_user_data(existing_user_name)
    assert existing_user is not None

    stock_read = "test_for_stock_read"
    assert acc.download_other_user_data(stock_read) is not None


def test2_buy_stock_in_wishlist():
    """Tests if stock in watchlist is bought, added to portfolio, and removed from watchlist"""
    stock_to_purchase = "TSLA"

    download = glb.collection.find_one({"user_name": glb.TEST_USER_NAME},
                                       {"all_stocks": 1, "money": 1, "safe_mode": 1,
                                        "watchlist_stock_id": 1})
    matching_dict = None
    for dicts in download["all_stocks"]:
        if dicts["stock_id"] == stock_to_purchase:
            matching_dict = dicts
    assert matching_dict is None

    assert fn.buy_stock(stock_to_purchase, 1, glb.TEST_USER_NAME) is True

    watchlist_array_value = None
    for ids in download["watchlist_stock_id"]:
        if ids == stock_to_purchase:
            watchlist_array_value = ids
    assert watchlist_array_value is not None

    download = glb.collection.find_one({"user_name": glb.TEST_USER_NAME})
    watchlist_array_value = None
    for ids in download["watchlist_stock_id"]:
        if ids == stock_to_purchase:
            watchlist_array_value = ids
    assert watchlist_array_value is None

    assert download["money"] < 3000.00


def test3_buy_stock_not_in_wishlist():
    """Tests if stock is purchasable that is not in watchlist"""
    pre_addition = glb.collection.find_one({"user_name": glb.TEST_USER_NAME})["money"]
    fn.buy_stock("CAKE", 1, glb.TEST_USER_NAME)
    download = glb.collection.find_one({"user_name": glb.TEST_USER_NAME})

    value = fn.yf.Ticker("CAKE").info['currentPrice']

    assert glb.collection.find_one({"user_name": glb.TEST_USER_NAME,
                                    "all_stocks": {"$elemMatch": {"stock_id": "CAKE"}}}) is not None
    upper_bound = (pre_addition - round(value, 2)) * 1.01
    lower_bound = (pre_addition - round(value, 2)) * 0.99

    assert lower_bound <= download["money"] <= upper_bound

    value2 = fn.yf.Ticker("AMZN").info['currentPrice']
    assert fn.buy_stock("AMZN", 2, glb.TEST_USER_NAME) is True
    duplicate_stock = glb.collection.find_one({"user_name": glb.TEST_USER_NAME})

    matching_dict = None
    for dicts in duplicate_stock["all_stocks"]:
        if dicts["stock_id"] == "AMZN":
            matching_dict = dicts

    assert matching_dict["qty"] > 2
    assert duplicate_stock["money"] <= download["money"] - round(value2, 2)

    pre_addition = glb.collection.find_one({"user_name": glb.TEST_USER_TWO})
    assert fn.buy_stock("AAPL", 1, glb.TEST_USER_TWO) is False
    assert fn.buy_stock("CAKE", 99, glb.TEST_USER_TWO) is False
    post_addition = glb.collection.find_one({"user_name": glb.TEST_USER_TWO})

    assert pre_addition == post_addition


def test4_check_if_safe_mode():
    """Tests if safe_mode variable is accessible"""
    user_one = glb.collection.find_one({"user_name": glb.TEST_USER_NAME})
    user_two = glb.collection.find_one({"user_name": "user_two"})
    assert user_one["safe_mode"] is False
    assert user_two["safe_mode"] is True


def test5_remove_from_wishlist():
    """Removes a stock from the watchlist without touching the all_stocks portfolio"""
    stock_name = "ACER"
    assert fn.remove_from_wishlist("ACER", glb.TEST_USER_NAME) is True
    assert fn.remove_from_wishlist("ACER", glb.TEST_USER_NAME) is False


def test6_sell_stock():
    """Tests if a stock is sellable, and allocates money accordingly"""
    stock_name = "AMZN"
    nonexistent_stock = "PZZA"

    pre_removal = glb.collection.find_one({"user_name": glb.TEST_USER_NAME})
    amzn_dict = None
    for dicts in pre_removal["all_stocks"]:
        if dicts["stock_id"] == stock_name:
            amzn_dict = dicts
    assert amzn_dict is not None

    assert fn.sell_stock(nonexistent_stock, 1, glb.TEST_USER_NAME) is None
    assert abs(fn.sell_stock(stock_name, 3, glb.TEST_USER_NAME)) > 0

    post_removal = glb.collection.find_one({"user_name": glb.TEST_USER_NAME})
    amzn_dict = None
    for dicts in post_removal["all_stocks"]:
        if dicts["stock_id"] == stock_name:
            amzn_dict = dicts
    assert amzn_dict is None

    assert pre_removal["money"] < post_removal["money"]

    diff_user_two = fn.sell_stock("PZZA", 1, glb.TEST_USER_TWO)
    assert diff_user_two is not None
    stock_sold_once = glb.collection.find_one({"user_name": glb.TEST_USER_NAME})["all_stocks"]
    for dicts in stock_sold_once:
        if dicts["stock_id"] == "PZZA":
            assert dicts["qty"] < 8
            break


def test7_buy_multiple_stocks():
    """Tests if multiple stocks are purchasable"""
    pre_addition = glb.collection.find_one({"user_name": glb.TEST_USER_NAME})
    stock_name = "TM"

    fn.buy_stock(stock_name, 4, glb.TEST_USER_NAME)

    post_addition = glb.collection.find_one({"user_name": glb.TEST_USER_NAME})

    matching_dict = None
    for dicts in post_addition["all_stocks"]:
        if dicts["stock_id"] == stock_name:
            matching_dict = dicts

    assert matching_dict is not None
    assert matching_dict["qty"] == 4
    assert pre_addition["money"] > post_addition["money"]


def test8_accounts():
    """tests account creation and deletion"""
    test8_name = "user_three"
    test8_email = "baez5@illinois.edu"
    test8_password = "test8"

    user_download = glb.collection.find_one({"user_name": test8_name})
    assert user_download is None

    assert acc.create_account(glb.TEST_USER_NAME, "example@example.com", "123123123") is False
    assert acc.create_account(test8_name, test8_email, test8_password) is True

    assert acc.delete_account(test8_name, test8_password) is True
    assert acc.delete_account(glb.TEST_USER_NAME, test8_password) is False


def test9_test_changes_to_account():
    """tests functions pertaining to account information changes"""
    test8_name = "user_three"
    test8_email = "fjbaez2@illinois.edu"
    test8_password = "test8"
    acc.create_account(test8_name, test8_email, test8_password)

    new_name = "python_project"

    assert acc.change_user_name(test8_name, new_name) is True
    assert acc.change_user_name(new_name, glb.TEST_USER_TWO) is False

    new_password = "415101439_new_key"
    new_password2 = "password123"
    assert acc.reset_password(new_name, test8_password, new_password) is True
    assert acc.reset_password(new_name, test8_password, new_password2) is False

    new_email = "baez5@illinois.edu"
    assert acc.change_email_address(new_name, new_email) is True
    assert acc.change_email_address(new_name, "example@example.com") is False

    assert acc.reset_account(glb.TEST_USER_NAME, "password") is True
    download = glb.collection.find_one({"user_name": glb.TEST_USER_NAME, "email": glb.T_UN_EMAIL})
    assert download["all_stocks"] == []
    assert download["money"] == 500.00
    assert download["safe_mode"] is True
    assert download["watchlist_stock_id"] == []


def test10_safe_mode_logic():
    """Tests for safe mode logic and manual override"""
    diff = fn.sell_stock("CAKE", 2, glb.TEST_USER_TWO)
    assert diff < 0

    download = glb.collection.find_one({"user_name": glb.TEST_USER_TWO})
    assert download["safe_mode"] is False

    fn.buy_stock("CAKE", 99, glb.TEST_USER_TWO)
    download = glb.collection.find_one({"user_name": glb.TEST_USER_TWO})
    assert download["safe_mode"] is True

    assert fn.manual_safe_mode(glb.TEST_USER_TWO) is False
    assert fn.manual_safe_mode(glb.TEST_USER_TWO) is True


def test11_other_user_data():
    """downloads user data and makes sure that some data is not copied from the database"""
    try:
        download = acc.download_other_user_data(glb.TEST_USER_NAME)
        password = download["password"]
    except KeyError:
        password = None

    assert password is None
