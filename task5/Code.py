

fine_rules = {
    "speeding": 1000,
    "signal_jump": 500,
    "no_helmet": 500,
    "drunk_driving": 5000
}

vehicle_rates = {
    "two_wheeler": 1.0,
    "car": 1.5,
    "heavy_vehicle": 2.0
}

REPEAT_MULTIPLIER = 2

violations = []
vehicle_repeat_count = {}
vehicle_disqualified = {}
total_penalty = 0

print("===== TRAFFIC VIOLATION PENALTY CALCULATOR =====")
n = int(input("Enter number of violations: "))

if n <= 0:
    print("Invalid number of violations.")

else:
    for i in range(n):
        print(f"\nViolation {i + 1}")

        vehicle_no = input("Vehicle registration number: ").upper()
        category = input(
            "Vehicle category (two_wheeler/car/heavy_vehicle): "
        ).lower()

        offence = input(
            "Offence (speeding/signal_jump/no_helmet/drunk_driving): "
        ).lower()

        repeat = input(
            "Is this a repeat offence? (yes/no): "
        ).lower()

        # Validate inputs
        if (
            not vehicle_no.strip()
            or category not in vehicle_rates
            or offence not in fine_rules
            or repeat not in ("yes", "no")
        ):
            print("Invalid details. Violation skipped.")
            continue

        
        base_fine = fine_rules[offence]
        base_fine *= vehicle_rates[category]

        
        if repeat == "yes":
            penalty = base_fine * REPEAT_MULTIPLIER
            vehicle_repeat_count[vehicle_no] = (
                vehicle_repeat_count.get(vehicle_no, 0) + 1
            )
        else:
            penalty = base_fine
            vehicle_repeat_count.setdefault(vehicle_no, 0)

    
        if offence == "drunk_driving":
            vehicle_disqualified[vehicle_no] = True
        else:
            vehicle_disqualified.setdefault(vehicle_no, False)

        violations.append({
            "vehicle": vehicle_no,
            "category": category,
            "offence": offence,
            "repeat": repeat,
            "penalty": penalty
        })

        total_penalty += penalty

    
    for vehicle_no, count in vehicle_repeat_count.items():
        if count >= 3:
            vehicle_disqualified[vehicle_no] = True

    
    print("\n========== TRAFFIC PENALTY REPORT ==========")

    for v in violations:
        print(f"\nVehicle Number : {v['vehicle']}")
        print(f"Category       : {v['category']}")
        print(f"Offence        : {v['offence']}")
        print(f"Repeat Offence : {v['repeat']}")
        print(f"Final Penalty  : Rs. {v['penalty']:.2f}")

        if vehicle_disqualified.get(v["vehicle"], False):
            print("Status         : Disqualification condition met")
        else:
            print("Status         : No disqualification condition met")

        print("-" * 45)

    print(f"\nTotal Penalty: Rs. {total_penalty:.2f}")

    print("\nVehicle Disqualification Summary:")
    for vehicle_no, status in vehicle_disqualified.items():
        if status:
            print(f"{vehicle_no}: Disqualification condition met")
        else:
            print(f"{vehicle_no}: No disqualification condition met")

    print("=============================================")
