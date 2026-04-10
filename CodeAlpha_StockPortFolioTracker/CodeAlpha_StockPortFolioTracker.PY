def stock_tracker():
    print("📈 Stock Portfolio Tracker")
    
    # Predefined stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 300
    }

    total_investment = 0
    portfolio = {}

    while True:
        stock = input("Enter stock name (or 'done' to finish): ").strip().upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not found! Available:", list(stock_prices.keys()))
            continue

        try:
            qty = int(input(f"Enter quantity for {stock}: "))
            if qty <= 0:
                print("❌ Quantity must be positive!")
                continue
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + qty
        total_investment += stock_prices[stock] * qty

    print("\n📊 Your Portfolio:")
    for stock, qty in portfolio.items():
        print(f"{stock} → {qty} shares")

    print(f"\n💰 Total Investment: ${total_investment}")
