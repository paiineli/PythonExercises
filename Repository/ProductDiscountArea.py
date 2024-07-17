# Product Discount exercise
print("Calculate the discount for your product")
product_price = input("How much does your product cost? ")
discount = input("What is your discount percentage? ")
product_discount = float(product_price) * float(discount) / 100
discounted_price = float(product_price) - product_discount
print(f"The price of the discounted product is: {discounted_price}")
