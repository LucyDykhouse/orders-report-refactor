# SALESPERSON_INDEX = 0
# INTERNET_INDEX = 1
# DORKY_LINE_LENGTH = 80
#
# print("*" * DORKY_LINE_LENGTH)
# f = open("orders-by-type.txt")
# melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}
#
# for l in f:
#     data = l.split("|")
#     melon_type = data[1]
#     melon_count = int(data[2])
#     melon_tallies[melon_type] += melon_count
#
# f.close()
# melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
# total_revenue = 0
# for melon_type in melon_tallies:
#     price = melon_prices[melon_type]
#     revenue = price * melon_tallies[melon_type]
#     total_revenue += revenue
#     print(f"We sold {melon_tallies[melon_type]} {melon_type} melons at {price:.2f} each for a total of {revenue:.2f}")
# print("******************************************")
# f = open("orders-with-sales.txt")
# sales = [0, 0]
# for line in f:
#     d = line.split("|")
#     if d[1] == "0":
#         sales[0] += float(d[3])
#     else:
#         sales[1] += float(d[3])
# print(f"Salespeople generated ${sales[1]:.2f} in revenue.")
# print(f"Internet sales generated ${sales[0]:.2f} in revenue.")
# if sales[1] > sales[0]:
#     print("Guess there's some value to those salespeople after all.")
# else:
#     print("Time to fire the sales team! Online sales rule all!")
# print("******************************************")


def get_melon_counts(filename):
    """Add comment here"""

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
    """Add comment here"""
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
    """Add comment here"""

    with open(filename, 'r') as sales_data:

        sales_by_type = [0,0]

        for line in sales_data:
            _, sales_type, _, amt = line.rstrip().split('|')

            if sales_type == "0":
                sales_by_type[0] += float(amt)
            else:
                sales_by_type[1] += float(amt)

        print(f"Salespeople generated ${sales_by_type[1]:.2f} in revenue.")
        print(f"Internet sales generated ${sales_by_type[0]:.2f} in revenue.")

        if sales_by_type[1] > sales_by_type[0]:
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

