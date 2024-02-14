const stocks = [
    {
        user_name: "test_user_name", 
        all_stocks: [
            { "stock_id": "AMZN", "val_at_purchase": 115.15, "qty": 1 },
            { "stock_id": "MSFT", "val_at_purchase": 237.45, "qty": 1 },
            { "stock_id": "AAPL", "val_at_purchase": 150.77, "qty": 1 },
            { "stock_id": "QSR", "val_at_purchase": 54.97, "qty": 1 }
        ],
        money: 3000.00,
        safe_mode: false,
        watchlist_stock_id: ["HPQ", "TSLA"]

    },
    {
        user_name: "test_user_name2",
        all_stocks: [
            { "stock_id": "AMZN", "val_at_purchase": 115.45, "qty": 6 },
            { "stock_id": "MSFT", "val_at_purchase": 100, "qty": 8 },
        ],
        money: 7595.23,
        safe_mode: true,
        watchlist_stock_id: ["TSLA"]
    },
];

module.exports = stocks;