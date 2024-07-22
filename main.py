import csv
from datetime import datetime
import matplotlib.pyplot as plt
import collections


def read_sales_data(file_path):
    sales_data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        sales_reader = csv.reader(csvfile)
        for row in sales_reader:
            product_name, quantity, price, date = row
            sales_data.append({
                'product_name': product_name,
                'quantity': int(quantity),
                'price': float(price),
                'date': datetime.strptime(date, '%Y-%m-%d').date()
            })
    return sales_data


def total_sales_per_product(sales_data):
    product_sales = {}
    for sale in sales_data:
        product_name = sale['product_name']
        total_sale = sale['quantity'] * sale['price']
        if product_name in product_sales:
            product_sales[product_name] += total_sale
        else:
            product_sales[product_name] = total_sale
    return product_sales


def sales_over_time(sales_data):
    daily_sales = {}
    for sale in sales_data:
        date = sale['date']
        total_sale = sale['quantity'] * sale['price']
        if date in daily_sales:
            daily_sales[date] += total_sale
        else:
            daily_sales[date] = total_sale
    od = collections.OrderedDict(sorted(daily_sales.items()))
    return od


def find_max_revenue_product(product_sales):
    max_product = max(product_sales, key=product_sales.get)
    return max_product, product_sales[max_product]


def find_max_revenue_day(daily_sales):
    max_day = max(daily_sales, key=daily_sales.get)
    return max_day, daily_sales[max_day]


def plot_sales_per_product(product_sales):
    products = list(product_sales.keys())
    sales = list(product_sales.values())

    plt.figure(figsize=(10, 5))
    plt.bar(products, sales, color='blue')
    plt.xlabel('Продукты')
    plt.ylabel('Общая сумма продаж')
    plt.title('Общая сумма продаж по продуктам')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_sales_over_time(daily_sales):
    dates = list(daily_sales.keys())
    sales = list(daily_sales.values())

    plt.figure(figsize=(10, 5))
    plt.plot(dates, sales, marker='o', linestyle='-', color='red')
    plt.xlabel('Дата')
    plt.ylabel('Общая сумма продаж')
    plt.title('Общая сумма продаж по дням')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    file_path = 'sales_data.csv'  # путь к вашему файлу с данными о продажах
    sales_data = read_sales_data(file_path)

    product_sales = total_sales_per_product(sales_data)
    daily_sales = sales_over_time(sales_data)

    max_product, max_revenue = find_max_revenue_product(product_sales)
    print(f"Продукт с наибольшей выручкой: {max_product}, выручка: {max_revenue}")

    max_day, max_day_revenue = find_max_revenue_day(daily_sales)
    print(f"День с наибольшей суммой продаж: {max_day}, сумма продаж: {max_day_revenue}")

    plot_sales_per_product(product_sales)
    plot_sales_over_time(daily_sales)
