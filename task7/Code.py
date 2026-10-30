

FIXED_CHARGE = 50
SURCHARGE_LIMIT = 250
SURCHARGE_RATE = 10
REBATE_LIMIT = 100
REBATE_RATE = 5
INCREASE_LIMIT = 30

monthly_bills = []

print("===== ELECTRICITY BILLING SYSTEM =====")

household = input("Enter household name: ")
months = int(input("Enter number of months: "))

if not household.strip() or months <= 0:
    print("Invalid household name or number of months.")

else:
    for i in range(months):
        print(f"\nMonth {i + 1}")

        month_name = input("Enter month name: ")
        units = float(input("Enter electricity consumption (kWh): "))

        if not month_name.strip() or units < 0:
            print("Invalid input. Month skipped.")
            continue


        if units <= 100:
            energy_charge = units * 2

        elif units <= 200:
            energy_charge = 100 * 2 + (units - 100) * 3

        else:
            energy_charge = (
                100 * 2
                + 100 * 3
                + (units - 200) * 5
            )


        fixed_charge = FIXED_CHARGE

      
        surcharge = 0
        rebate = 0

        if units > SURCHARGE_LIMIT:
            surcharge = energy_charge * SURCHARGE_RATE / 100

        elif units <= REBATE_LIMIT:
            rebate = energy_charge * REBATE_RATE / 100


        bill = (
            energy_charge
            + fixed_charge
            + surcharge
            - rebate
        )

        monthly_bills.append({
            "month": month_name,
            "units": units,
            "energy": energy_charge,
            "fixed": fixed_charge,
            "surcharge": surcharge,
            "rebate": rebate,
            "bill": bill
        })


    print("\n========== MONTHLY ELECTRICITY BILLS ==========")
    print(f"Household: {household}")

    for b in monthly_bills:
        print(f"\nMonth       : {b['month']}")
        print(f"Units       : {b['units']:.2f} kWh")
        print(f"Energy Cost : Rs. {b['energy']:.2f}")
        print(f"Fixed Charge: Rs. {b['fixed']:.2f}")
        print(f"Surcharge   : Rs. {b['surcharge']:.2f}")
        print(f"Rebate      : Rs. {b['rebate']:.2f}")
        print(f"Final Bill  : Rs. {b['bill']:.2f}")
        print("-" * 40)


    print("\n========== BILL COMPARISON ==========")

    unusual_found = False

    for i in range(1, len(monthly_bills)):
        previous = monthly_bills[i - 1]
        current = monthly_bills[i]

        if previous["bill"] > 0:
            increase = (
                (current["bill"] - previous["bill"])
                / previous["bill"]
            ) * 100

            print(
                f"{previous['month']} to {current['month']}: "
                f"{increase:.2f}% change"
            )

            if increase > INCREASE_LIMIT:
                print("WARNING: Unusual bill increase detected!")
                unusual_found = True

    if not unusual_found:
        print("No unusual bill increases detected.")

    total = sum(b["bill"] for b in monthly_bills)

    print(f"\nTotal Amount: Rs. {total:.2f}")
    print("====================================")
