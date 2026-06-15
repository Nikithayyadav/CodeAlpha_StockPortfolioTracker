# Step 1: Define stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800, 
    "MSFT": 320,
    "INFY": 1450
}
 
# Step 2: User input
portfolio = {}
total_investment = 0

print("📊 Welcome to Stock Portfolio Tracker")
num_stocks = int(input("How many different stocks do you want to add? "))

for i in range(num_stocks):
    stock = input(f"\nEnter stock symbol (e.g., AAPL, TSLA): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment
        portfolio[stock] = {
            "quantity": quantity,
            "price": price,
            "investment": investment
        }
    else:
        print(f"❌ '{stock}' is not in the price list. Skipped.")

# Step 3: Display Results
print("\n📈 Investment Summary:")
for stock, details in portfolio.items():
    print(f"{stock}: {details['quantity']} shares × ₹{details['price']} = ₹{details['investment']}")

print(f"\n💰 Total Investment Value: ₹{total_investment}")

# Step 4: Save to file (optional)
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as f:
        f.write("📈 Stock Portfolio Summary\n\n")  # ✅ no warning now

        for stock, details in portfolio.items():
            f.write(f"{stock}: {details['quantity']} × ₹{details['price']} = ₹{details['investment']}\n")
        f.write(f"\nTotal Investment: ₹{total_investment}")
    print("✅ Summary saved to 'portfolio_summary.txt'")
