

FIXED_FEE = 50
EXCESS_LIMIT = 30
PENALTY_RATE = 10

households = []
total_revenue = 0

print("===== WATER TARIFF BILLING SYSTEM =====")

n = int(input("Enter number of households: "))

if n <= 0:
    print("Invalid number of households.")

else:
    for i in range(n):
        print(f"\nHousehold {i + 1}")

        name = input("Enter household name: ")
        consumption = float(
            input("Enter water consumption (kL): ")
        )

        if not name.strip() or consumption < 0:
            print("Invalid details. Household skipped.")
            continue

        # Calculate progressive water charges
        if consumption <= 10:
            water_charge = consumption * 10

        elif consumption <= 20:
            water_charge = 10 * 10
            water_charge += (consumption - 10) * 15

        else:
            water_charge = 10 * 10
            water_charge += 10 * 15
            water_charge += (consumption - 20) * 25

        # Add fixed service fee
        subtotal = water_charge + FIXED_FEE

        # Apply penalty for excessive usage
        if consumption > EXCESS_LIMIT:
            penalty = water_charge * PENALTY_RATE / 100
            status = "Excessive Usage"
        else:
            penalty = 0
            status = "Normal Usage"


        bill = subtotal + penalty

        households.append({
            "name": name,
            "consumption": consumption,
            "water_charge": water_charge,
            "fixed_fee": FIXED_FEE,
            "penalty": penalty,
            "bill": bill,
            "status": status
        })

        total_revenue += bill


    print("\n========== WATER BILL REPORT ==========")

    for h in households:
        print(f"\nHousehold Name : {h['name']}")
        print(f"Consumption    : {h['consumption']:.2f} kL")
        print(f"Water Charges  : Rs. {h['water_charge']:.2f}")
        print(f"Fixed Fee      : Rs. {h['fixed_fee']:.2f}")
        print(f"Penalty        : Rs. {h['penalty']:.2f}")
        print(f"Final Bill     : Rs. {h['bill']:.2f}")
        print(f"Usage Status   : {h['status']}")
        print("-" * 38)

  
    if households:
        highest = max(
            households,
            key=lambda h: h["consumption"]
        )

        lowest = min(
            households,
            key=lambda h: h["consumption"]
        )

        print("\n========== CONSUMPTION ANALYSIS ==========")
        print(
            f"Highest Consumption: {highest['name']} "
            f"({highest['consumption']:.2f} kL)"
        )
        print(
            f"Lowest Consumption : {lowest['name']} "
            f"({lowest['consumption']:.2f} kL)"
        )
        print(f"Total Revenue      : Rs. {total_revenue:.2f}")

        print("\nExcessive Usage Households:")
        excessive = [
            h["name"] for h in households
            if h["consumption"] > EXCESS_LIMIT
        ]

        if excessive:
            for name in excessive:
                print(name)
        else:
            print("No excessive usage detected.")

        print("==========================================")
