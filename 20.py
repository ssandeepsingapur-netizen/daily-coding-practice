from secrets import choice


class market:
    def __init__(self, product_names,price_product):
        self.product_names = product_names
        self.price_product = price_product
    def display_products(self):
        for name, price in zip(self.product_names, self.price_product):
            print(f"{name}: ${price}")
# Example usage:
n = int(input("Enter the number of products: "))
product_names = []
price_product = []
for i in range(n):
    name = input(f"Enter the name of product {i+1}: ")
    price = float(input(f"Enter the price of product {i+1}: "))
    product_names.append(name)
    price_product.append(price)
market_instance = market(product_names, price_product)
market_instance.display_products()