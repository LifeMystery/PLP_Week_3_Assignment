def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if it's 20% or more.
    
    Parameters:
    - price (float): Original price of the item.
    - discount_percent (float): Discount percentage to apply.
    
    Returns:
    - float: Final price after discount if applicable, otherwise original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")
