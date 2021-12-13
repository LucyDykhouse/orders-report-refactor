def get_melon_counts(filename):
    """Return tally of melons by type"""

    with open(filename) as order_data:
        melon_counts = {
            'musk': 0,
            'hybrid': 0,
            'watermelon': 0,
            'winter': 0
        }
        for line in order_data:
            _, melon_type, melon_count = line.rstrip().split('|')
            melon_counts[melon_type.lower()] += int(melon_count)

        return melon_counts


def get_total_revenue(counts):
    """Prints revenue for each melon type"""

    total_revenue = 0

    melon_prices = {
        'musk': 1.15,
        'hybrid': 1.30,
        'watermelon': 1.75,
        'winter': 4.00
    }

    for melon_type in counts:
        price = melon_prices[melon_type]
        revenue = counts[melon_type] * melon_prices[melon_type]
        total_revenue += revenue
        print(f"We sold {counts[melon_type]} {melon_type} melons at ${price:.2f} each for a total of ${revenue:.2f}")


def get_sales_by_type(filename):
    """Compare sales revenue of online orders and orders from salespeople"""

    with open(filename, 'r') as sales_data:
        online_revenue = 0
        salesperson_revenue = 0

        for line in sales_data:
            _, sales_type, _, amt = line.rstrip().split('|')

            if sales_type == "0":
                online_revenue += float(amt)
            else:
                salesperson_revenue += float(amt)

        print(f"Salespeople generated ${salesperson_revenue:.2f} in revenue.")
        print(f"Internet sales generated ${online_revenue:.2f} in revenue.")

        if salesperson_revenue > online_revenue:
            print("Guess there's some value to those salespeople after all.")
        else:
            print("Time to fire the sales team! Online sales rule all!")


def main():
    """Add comment here"""

    # Get the order counts
    counts = get_melon_counts('orders-by-type.txt')

    # Get the total revenue
    print('*' * 50)
    get_total_revenue(counts)

    # Get the revenue by type
    print('*' * 50)
    get_sales_by_type('orders-with-sales.txt')


# Call main function
main()

