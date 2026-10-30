


zones = {
    "local": 1.0,
    "regional": 1.5,
    "national": 2.5
}
services = {
    "Basic": {
        "rate": 40,
        "max_weight": 10,
        "max_dimension": 100,
        "express_fee": 0,
        "restrictions": {"none"}
    },
    "Express": {
        "rate": 60,
        "max_weight": 20,
        "max_dimension": 150,
        "express_fee": 100,
        "restrictions": {"none", "fragile"}
    },
    "Premium": {
        "rate": 85,
        "max_weight": 50,
        "max_dimension": 200,
        "express_fee": 150,
        "restrictions": {"none", "fragile", "liquid"}
    }
}

VOLUMETRIC_DIVISOR = 5000

print("===== COURIER CHARGE OPTIMIZATION =====")

try:
    weight = float(input("Enter parcel weight (kg): "))
    length = float(input("Enter length (cm): "))
    width = float(input("Enter width (cm): "))
    height = float(input("Enter height (cm): "))

    zone = input(
        "Enter distance zone (local/regional/national): "
    ).strip().lower()

    urgency = input(
        "Enter urgency (standard/express): "
    ).strip().lower()

    restriction = input(
        "Enter restriction (none/fragile/liquid/restricted): "
    ).strip().lower()


    if (
        weight <= 0
        or min(length, width, height) <= 0
        or zone not in zones
        or urgency not in ("standard", "express")
        or restriction not in (
            "none", "fragile", "liquid", "restricted"
        )
    ):
        print("Invalid input. Please check the details.")

    else:
        
        volumetric_weight = (
            length * width * height / VOLUMETRIC_DIVISOR
        )

        chargeable_weight = max(weight, volumetric_weight)

        print("\nVolumetric Weight:",
              round(volumetric_weight, 2), "kg")
        print("Chargeable Weight:",
              round(chargeable_weight, 2), "kg")

        eligible_services = []

  
        print("\n========== SERVICE COMPARISON ==========")

        for name, service in services.items():

            # Check weight and dimension limits
            if chargeable_weight > service["max_weight"]:
                print(f"{name}: Not eligible (weight limit)")
                continue

            if max(length, width, height) > service["max_dimension"]:
                print(f"{name}: Not eligible (size limit)")
                continue

            if restriction not in service["restrictions"]:
                print(f"{name}: Not eligible (restriction)")
                continue

      
            charge = (
                chargeable_weight
                * service["rate"]
                * zones[zone]
            )

            # Add urgency fee
            if urgency == "express":
                charge += service["express_fee"]

            # Add fragile handling fee
            if restriction == "fragile":
                charge += 30

            eligible_services.append({
                "name": name,
                "charge": charge
            })

            print(f"{name}: Rs. {charge:.2f} (Eligible)")


        print("\n========== RECOMMENDATION ==========")

        if eligible_services:
            best = min(
                eligible_services,
                key=lambda s: s["charge"]
            )

            print("Recommended Service:", best["name"])
            print(f"Delivery Charge: Rs. {best['charge']:.2f}")
        else:
            print("No eligible courier service found.")

        print("=====================================")

except ValueError:
    print("Invalid input. Please enter numeric values correctly.") 
