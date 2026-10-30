

FIXED_CHARGE = 50
REBATE_LIMIT = 100
REBATE_RATE = 0.10


def calculate_energy_charge(units):
    """Calculate charges using progressive tariff slabs."""
    if units <= 100:
        return units * 2
    elif units <= 200:
        return (100 * 2) + ((units - 100) * 3)
    else:
        return (100 * 2) + (100 * 3) + ((units - 200) * 5)


apartments = []

print("=== Smart Electricity Billing System ===")

try:
    count = int(input("Enter number of apartments: "))

    if count <= 0:
        print("Error: Number of apartments must be positive.")
    else:
        for i in range(count):
            print(f"\nApartment {i + 1}")

            name = input("Enter apartment name: ").strip()
            units = float(input("Enter units consumed: "))
            recorded_bill = float(input("Enter recorded bill (Rs.): "))

            if not name or units < 0 or recorded_bill < 0:
                print("Error: Invalid apartment details.")
                apartments = []
                break

  
            energy_charge = calculate_energy_charge(units)

          
            if units <= REBATE_LIMIT:
                rebate = energy_charge * REBATE_RATE
            else:
                rebate = 0

            
            final_bill = energy_charge + FIXED_CHARGE - rebate

      
            discrepancy = abs(final_bill - recorded_bill)

            apartments.append({
                "name": name,
                "units": units,
                "energy_charge": energy_charge,
                "rebate": rebate,
                "final_bill": final_bill,
                "recorded_bill": recorded_bill,
                "discrepancy": discrepancy
            })

        if apartments:
            print("\n========== APARTMENT BILL DETAILS ==========")

            for apartment in apartments:
                print(f"\nApartment: {apartment['name']}")
                print(f"Units consumed: {apartment['units']:.2f}")
                print(
                    f"Energy charge: Rs. "
                    f"{apartment['energy_charge']:.2f}"
                )
                print(f"Fixed charge: Rs. {FIXED_CHARGE:.2f}")
                print(f"Rebate: Rs. {apartment['rebate']:.2f}")
                print(
                    f"Calculated bill: Rs. "
                    f"{apartment['final_bill']:.2f}"
                )
                print(
                    f"Recorded bill: Rs. "
                    f"{apartment['recorded_bill']:.2f}"
                )

                if apartment["discrepancy"] > 0.01:
                    print(
                        f"Billing discrepancy: Rs. "
                        f"{apartment['discrepancy']:.2f}"
                    )
                    print("Status: DISCREPANCY FOUND")
                else:
                    print("Billing discrepancy: Rs. 0.00")
                    print("Status: BILL VERIFIED")

          
            ranked = sorted(
                apartments,
                key=lambda apartment: apartment["units"],
                reverse=True
            )

            print("\n========== CONSUMPTION RANKING ==========")

            for rank, apartment in enumerate(ranked, start=1):
                print(
                    f"{rank}. {apartment['name']} - "
                    f"{apartment['units']:.2f} units"
                )

except ValueError:
    print("Error: Please enter valid numeric values.")
