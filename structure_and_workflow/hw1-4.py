product_name = input("Please enter the product name: ")
manufacture_date = input("Please enter the manufacture date (DD-MM-YYYY): ")
product_id = f"{product_name[:3].upper()}-{manufacture_date[6:10]}{len(product_name)}{product_name[-1]}"

print(f"The product ID is: {product_id}")
