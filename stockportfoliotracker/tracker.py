# Stock Portfolio Tracker

# Predefined stock prices (in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 145,
    "MSFT": 310
}

portfolio = {}
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker 📈\n")
print("Available Stocks:", ', '.join(stock_prices.keys()))
print("Enter 'done' to finish input.\n")

# User Input: Stock name and quantity
while True:
    stock_name = input("Enter stock name: ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("❌ Stock not found. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity < 0:
            print("❌ Quantity cannot be negative.")
            continue
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("❌ Please enter a valid number.")

# Calculating Total Investment
print("\n📊 Investment Summary:\n")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment Value: ${total_investment}\n")

# Optional: Save to a text file
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
        file.write("📊 Investment Summary:\n\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock}: {quantity} shares × ${price} = ${investment}\n")
        file.write(f"\n💰 Total Investment Value: ${total_investment}\n")
    print("✅ Portfolio summary saved to 'portfolio_summary.txt'")
