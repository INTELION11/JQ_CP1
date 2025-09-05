# JQ 1st Idiot Proof
fisrt_name = input("Whats your first name? ").strip().title()
last_name = input("Whats your last name? ").strip().title()
phone_number = str(float(input("Whats your phone number? ")))
gpa = float(input("Whats your GPA? "))
full_name = fisrt_name + " " + last_name
print(full_name)
phone1 = phone_number[0:3]
phone2 = phone_number[3:6]
phone3 = phone_number[6:10]
print(full_name)
print (f"phone number: {phone1} {phone2} {phone3}")
print(f"{gpa:.1f}")