

print("=== Manufacturing Production Planner ===")


available_material = float(input("Enter available raw material (kg): "))
material_per_product = float(input("Enter material required per product (kg): "))
planned_production = int(input("Enter planned production quantity: "))
order_demand = int(input("Enter customer order demand: "))
defect_count = int(input("Enter number of defective products: "))
allowed_defect_rate = float(input("Enter maximum allowed defect rate (%): "))


if (available_material < 0 or material_per_product <= 0
        or planned_production < 0 or order_demand < 0
        or defect_count < 0 or allowed_defect_rate < 0
        or allowed_defect_rate > 100):
    print("Error: Please enter valid input values.")

elif defect_count > planned_production:
    print("Error: Defect count cannot exceed planned production.")

else:
    
    max_production = int(available_material // material_per_product)
    material_required = planned_production * material_per_product
    material_shortage = max(0, material_required - available_material)

    # Calculate quality details
    if planned_production > 0:
        defect_rate = (defect_count / planned_production) * 100
    else:
        defect_rate = 0

    good_products = planned_production - defect_count
    product_shortage = max(0, order_demand - good_products)

    print("\n--- Production Analysis ---")
    print("Maximum possible production:", max_production, "units")
    print("Planned production:", planned_production, "units")
    print(f"Material required: {material_required:.2f} kg")
    print(f"Material shortage: {material_shortage:.2f} kg")

    if material_shortage == 0:
        print("Production feasibility: FEASIBLE")
    else:
        print("Production feasibility: NOT FEASIBLE")

    print("Defective products:", defect_count)
    print(f"Defect rate: {defect_rate:.2f}%")
    print("Good products:", good_products)

    if defect_rate <= allowed_defect_rate:
        print("Quality status: ACCEPTABLE")
    else:
        print("Quality status: QUALITY VIOLATION")

    print("Customer order demand:", order_demand, "units")
    print("Product shortage:", product_shortage, "units")

    if product_shortage == 0:
        print("Order status: DEMAND CAN BE FULFILLED")
    else:
        print("Order status: DEMAND CANNOT BE FULLY FULFILLED")

    if material_shortage > 0:
        print("Recommendation: Obtain additional raw materials.")

    if defect_rate > allowed_defect_rate:
        print("Recommendation: Improve the production quality process.")

    if product_shortage > 0:
        print("Recommendation: Produce additional good-quality products.")
```
