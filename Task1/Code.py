
tax_rates = {
    "food": 5,
    "clothing": 12,
    "electronics": 18,
    "other": 5
}

MAX_CONCESSION = 1000

products = []
subtotal = 0
total_tax = 0

print("===== RETAIL BILLING SYSTEM =====")

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nEnter details for Product {i + 1}")

    name = input("Product name: ")
    category = input(
        "Category (food/clothing/electronics/other): "
    ).lower()

    price = float(input("Price per unit: "))
    quantity = int(input("Quantity: "))

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity. Try again.")
        continue

    
    tax_rate = tax_rates.get(category, tax_rates["other"])

    
    amount = price * quantity
    tax = amount * tax_rate / 100

    subtotal += amount
    total_tax += tax

    products.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "amount": amount,
        "tax_rate": tax_rate,
        "tax": tax
    })

if subtotal >= 5000:
    discount = subtotal * 0.10
elif subtotal >= 2000:
    discount = subtotal * 0.05
else:
    discount = 0

discount = min(discount, MAX_CONCESSION)

final_amount = subtotal + total_tax - discount


print("\n" + "=" * 85)
print("                         RETAIL INVOICE")
print("=" * 85)

print(
    f"{'Product':<15}{'Category':<15}{'Qty':<6}"
    f"{'Price':<10}{'Amount':<10}{'Tax %':<8}{'Tax':<10}"
)

print("-" * 85)

for p in products:
    print(
        f"{p['name']:<15}{p['category']:<15}"
        f"{p['quantity']:<6}{p['price']:<10.2f}"
        f"{p['amount']:<10.2f}{p['tax_rate']:<8}"
        f"{p['tax']:<10.2f}"
    )

print("-" * 85)
print(f"Subtotal                 : Rs. {subtotal:.2f}")
print(f"Total Tax                : Rs. {total_tax:.2f}")
print(f"Discount                 : Rs. {discount:.2f}")
print(f"Maximum Concession       : Rs. {MAX_CONCESSION:.2f}")
print(f"Final Amount Payable     : Rs. {final_amount:.2f}")
print("=" * 85)
print("       Thank you for shopping with us!")
