

print("===== HOSPITAL BILLING SYSTEM =====")

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
category = input(
    "Enter patient category (General/Senior): "
).strip().lower()

consultation = float(input("Enter consultation charges: Rs. "))
diagnostic = float(input("Enter diagnostic charges: Rs. "))
treatment = float(input("Enter treatment charges: Rs. "))

if (
    not name.strip()
    or age <= 0
    or category not in ["general", "senior"]
    or min(consultation, diagnostic, treatment) < 0
):
    print("\nError: Invalid patient details or charges.")

elif category == "senior" and age < 60:
    print("\nError: Senior category requires age 60 or above.")

else:
    
    total_bill = consultation + diagnostic + treatment

    
    if age >= 60:
        concession_rate = 10
    elif total_bill >= 10000:
        concession_rate = 5
    else:
        concession_rate = 0

    concession = total_bill * concession_rate / 100
    final_amount = total_bill - concession

    # Patient classification
    if total_bill < 5000:
        classification = "Low-cost patient"
    elif total_bill <= 15000:
        classification = "Medium-cost patient"
    else:
        classification = "High-cost patient"


    print("\n========== HOSPITAL INVOICE ==========")
    print(f"Patient Name       : {name}")
    print(f"Patient Age        : {age}")
    print(f"Patient Category   : {category.title()}")
    print("--------------------------------------")
    print(f"Consultation       : Rs. {consultation:.2f}")
    print(f"Diagnostics        : Rs. {diagnostic:.2f}")
    print(f"Treatment          : Rs. {treatment:.2f}")
    print("--------------------------------------")
    print(f"Total Bill         : Rs. {total_bill:.2f}")
    print(f"Concession         : {concession_rate}%")
    print(f"Concession Amount  : Rs. {concession:.2f}")
    print(f"Final Amount       : Rs. {final_amount:.2f}")
    print(f"Classification     : {classification}")
    print("======================================")
