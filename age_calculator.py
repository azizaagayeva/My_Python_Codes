import datetime

first_name = input("Enter your first name: ")
last_name = input("Enter your - last name: ")

while True:
    birth_date = input("Date of birth (DD.MM.YYYY): ")
    try:
        birth = datetime.datetime.strptime(birth_date, "%d.%m.%Y").date()
        break
    except ValueError:
        print("That's not a valid date. are u serious enter like ts: 14.03.2000")

today = datetime.date.today()
age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

next_bday = birth.replace(year=today.year)
if next_bday < today:
    next_bday = birth.replace(year=today.year + 1)
days_left = (next_bday - today).days

print(f"\nName: {first_name} {last_name}")
print(f"Age: {age} years old")
if days_left == 0:
    print("Happy Birthday!yayayayyya")
else:
    print(f"Next birthday in {days_left} day(s).")
    