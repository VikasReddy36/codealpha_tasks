
"""
CodeAlpha Python Programming Internship
Task 2: Stock Portfolio Tracker

Goal: Let the user input stock names and quantities, calculate the total
investment value using hardcoded stock prices, and save a report to a file.

Key Concepts: dictionary, input/output, basic arithmetic, file handling.
"""

# Hardcoded dictionary of stock prices (in USD per share)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330,
    "META": 300,
    "NFLX": 480,
}


def show_available_stocks():
    """Print the list of stocks the user can invest in."""
    print("\nAvailable Stocks and Prices (per share):")
    print("-" * 35)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<8} ${price}")
    print("-" * 35)


def get_portfolio():
    """
    Ask the user which stocks they want to buy and how many shares.
    Returns a dictionary like {"AAPL": 10, "TSLA": 5}.
    """
    portfolio = {}

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print(f"'{stock}' not found in our price list. Please try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock} shares: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        # Add to existing quantity if the stock was already entered
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"Added {quantity} shares of {stock}.")

    return portfolio


def calculate_investment(portfolio):
    """
    Calculate the value of each holding and the total investment.
    Returns (details_list, total_value) where details_list is a list of
    tuples: (symbol, quantity, price_per_share, value).
    """
    details = []
    total_value = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        details.append((symbol, quantity, price, value))
        total_value += value

    return details, total_value


def display_summary(details, total_value):
    """Print a nicely formatted summary of the portfolio."""
    print("\n" + "=" * 45)
    print("PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 45)

    for symbol, quantity, price, value in details:
        print(f"{symbol:<8}{quantity:<8}${price:<9}${value:<9}")

    print("-" * 45)
    print(f"Total Investment Value: ${total_value}")
    print("=" * 45)


def save_to_file(details, total_value, filename="portfolio_report.txt"):
    """Save the portfolio summary to a text file."""
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO REPORT\n")
        f.write("=" * 45 + "\n")
        f.write(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
        f.write("-" * 45 + "\n")

        for symbol, quantity, price, value in details:
            f.write(f"{symbol:<8}{quantity:<8}${price:<9}${value:<9}\n")

        f.write("-" * 45 + "\n")
        f.write(f"Total Investment Value: ${total_value}\n")

    print(f"\nReport saved to '{filename}'.")


def main():
    print("Welcome to the Stock Portfolio Tracker!")
    show_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks were added. Exiting without a report.")
        return

    details, total_value = calculate_investment(portfolio)
    display_summary(details, total_value)

    choice = input("\nSave this report to a file? (y/n): ").strip().lower()
    if choice == "y":
        save_to_file(details, total_value)


if __name__ == "__main__":
    main()