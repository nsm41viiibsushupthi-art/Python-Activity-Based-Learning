
def get_rate(distance):
    if distance <= 100:
        return 2.0
    elif distance <= 500:
        return 1.5
    else:
        return 1.2


class_multiplier = {
    "sleeper": 1.0,
    "ac3": 2.0,
    "ac2": 3.0,
    "firstac": 4.0
reservation_fee = {
    "sleeper": 20,
    "ac3": 40,
    "ac2": 60,
    "firstac": 80
}

CANCELLATION_RATE = 25

passengers = []
total_booking = 0

print("===== RAILWAY FARE CALCULATOR =====")

n = int(input("Enter number of passengers: "))

if n <= 0:
    print("Invalid number of passengers.")

else:
    for i in range(n):
        print(f"\nPassenger {i + 1}")

        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))
        distance = float(input("Enter travel distance (km): "))
        travel_class = input(
            "Enter class (Sleeper/AC3/AC2/FirstAC): "
        ).strip().lower()
        if (
            not name.strip()
            or age < 0
            or distance <= 0
            or travel_class not in class_multiplier
        ):
            print("Invalid details. Passenger skipped.")
            continue

        
        rate = get_rate(distance)
        basic_fare = (
            distance * rate * class_multiplier[travel_class]
        )

        if 5 <= age <= 12:
            concession_rate = 50
        elif age >= 60:
            concession_rate = 20
        else:
            concession_rate = 0

        concession = basic_fare * concession_rate / 100

      
        discounted_fare = basic_fare - concession

        
        reservation = reservation_fee[travel_class]
        final_fare = discounted_fare + reservation

        # Cancellation option
        cancel = input(
            "Cancel ticket? (yes/no): "
        ).strip().lower()

        if cancel not in ("yes", "no"):
            print("Invalid cancellation choice. Passenger skipped.")
            continue

        if cancel == "yes":
            penalty = final_fare * CANCELLATION_RATE / 100
            refund = final_fare - penalty
            payable = 0
        else:
            penalty = 0
            refund = 0
            payable = final_fare

        total_booking += payable

        passengers.append({
            "name": name,
            "age": age,
            "distance": distance,
            "class": travel_class.upper(),
            "basic": basic_fare,
            "concession": concession,
            "reservation": reservation,
            "fare": final_fare,
            "penalty": penalty,
            "refund": refund,
            "payable": payable,
            "cancelled": cancel == "yes"
        })

    
    print("\n========== RAILWAY FARE INVOICE ==========")

    for p in passengers:
        print(f"\nPassenger Name : {p['name']}")
        print(f"Age            : {p['age']}")
        print(f"Distance       : {p['distance']:.1f} km")
        print(f"Travel Class   : {p['class']}")
        print(f"Basic Fare     : Rs. {p['basic']:.2f}")
        print(f"Concession     : Rs. {p['concession']:.2f}")
        print(f"Reservation Fee: Rs. {p['reservation']:.2f}")
        print(f"Ticket Fare    : Rs. {p['fare']:.2f}")

        if p["cancelled"]:
            print("Status         : Cancelled")
            print(f"Penalty        : Rs. {p['penalty']:.2f}")
            print(f"Refund         : Rs. {p['refund']:.2f}")
        else:
            print("Status         : Confirmed")
            print(f"Amount Payable : Rs. {p['payable']:.2f}")

        print("-" * 42)

    print(f"Total Booking Amount: Rs. {total_booking:.2f}")
    print("==========================================")
