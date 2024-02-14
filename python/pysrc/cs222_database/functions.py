"""Collection of all the functions that are used in the manipulation of the database"""
import yfinance as yf
import pysrc.cs222_database.global_values as glb


def buy_stock(stock_name, qty, user):
    """"Checks if stock can be purchased"""
    local_data_download = download_data_locally(user)
    desired_stock_ticker = yf.Ticker(stock_name)
    stock_price = desired_stock_ticker.info['currentPrice']
    if local_data_download["safe_mode"] is True and stock_price > 50:
        print("You are in safe mode and prevented from buying stock greater than 50")
    elif local_data_download["money"] < stock_price * qty:
        local_data_download["safe_mode"] = True
        update_data(local_data_download, user)
    else:
        add_stock_to_database(stock_name, stock_price, qty, local_data_download, user)


def add_stock_to_database(stock_name, stock_price, qty, user_dict, user):
    """adds the desired stock to the database after passing checks from buy_stock"""
    stock_price = round(stock_price, 2)
    total_price = stock_price * qty
    matching_dict = None
    for dicts in user_dict["all_stocks"]:
        if dicts["stock_id"] == stock_name:
            matching_dict = dicts
            user_dict["all_stocks"].remove(matching_dict)

    if matching_dict is not None:
        matching_dict["qty"] += qty
        matching_dict["val_at_purchase"] += total_price
        user_dict["all_stocks"].append(matching_dict)
    else:
        if stock_name in user_dict["watchlist_stock_id"]:
            user_dict["watchlist_stock_id"].remove(stock_name)

        user_dict["all_stocks"].append({"stock_id": stock_name,
                                        "val_at_purchase": total_price, "qty": qty})
    user_dict["money"] -= round((stock_price * qty), 2)
    update_data(user_dict, user)


def remove_from_wishlist(stock_name, user):
    """Removes stock from watchlist if present"""
    local_data_download = download_data_locally(user)
    if stock_name in local_data_download["watchlist_stock_id"]:
        local_data_download["watchlist_stock_id"].remove(stock_name)
    update_data(local_data_download, user)


def add_to_wishlist(stock_name, user):
    """Adds stock to watchlist if not already present"""
    local_data_download = download_data_locally(user)
    if stock_name not in local_data_download["watchlist_stock_id"]:
        local_data_download["watchlist_stock_id"].append(stock_name)
    update_data(local_data_download, user)


def sell_stock(stock_name, qty, user):
    """Sells stock based on current price. Returns difference in value from when purchased"""
    local_data_download = download_data_locally(user)
    stock_ticker = yf.Ticker(stock_name)
    matching_dict = None
    stock_price = round((stock_ticker.info['currentPrice']), 2)
    for dicts in local_data_download["all_stocks"]:
        if dicts["stock_id"] == stock_name:
            matching_dict = dicts

    if matching_dict is not None and qty <= matching_dict["qty"]:

        val_at_purchase = matching_dict["val_at_purchase"]
        total_old_qty = matching_dict["qty"]
        local_data_download["money"] += stock_price * qty
        local_data_download["all_stocks"].remove(matching_dict)
        if matching_dict["qty"] > qty:
            matching_dict["qty"] -= qty
            matching_dict["val_at_purchase"] -= stock_price * qty
            local_data_download["all_stocks"].append(matching_dict)

        proportion = (val_at_purchase / total_old_qty) * qty
        difference = proportion - (stock_price * qty)
        safe_mode(val_at_purchase, stock_price * qty, local_data_download, user)
        return difference
    return None


def safe_mode(avg_val_at_purchase, selling_value, user_dict, user):
    """enables or disables safe mode if conditions are met"""
    if selling_value / avg_val_at_purchase <= 0.4 and user_dict["safe_mode"] is False:
        user_dict["safe_mode"] = True
    elif user_dict["safe_mode"] is True and selling_value / avg_val_at_purchase >= 1.2:
        user_dict["safe_mode"] = False
    update_data(user_dict, user)


def update_local_user_data(user_name):
    """updates local download of user data based on changes done to database"""
    glb.local_data_download = glb.collection.find_one({"user_name": user_name})


def update_data(new_dict, user_name):
    """updates data on database based on changes done in other functions"""
    glb.collection.update_one({"user_name": user_name},
                              {"$set": {"all_stocks": new_dict["all_stocks"],
                                        "money": new_dict["money"],
                                        "safe_mode": new_dict["safe_mode"],
                                        "watchlist_stock_id": new_dict["watchlist_stock_id"]}})
    update_local_user_data(user_name)


def download_data_locally(user_name):
    """creates a local download of data based on a username"""
    return glb.collection.find_one({"user_name": user_name})


def manual_safe_mode(user_name):
    """sets safe mode to its opposite state (disables if enabled, enables if disabled"""
    user_dict = glb.collection.find_one({"user_name": user_name})
    user_dict["safe_mode"] = not user_dict["safe_mode"]
    update_data(user_dict, user_name)
    return user_dict["safe_mode"]
