import os

# Taking input from the user
Mon = [
    "",
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC",
]
while True:
    month = int(input("Enter Month (1-12):\n"))
    if month < 1 or month > 12:
        print("Invalid Month\n")
    else:
        break

user_input = Mon[month] + " "

while True:
    day = int(input("Enter Day (1-31):\n"))
    if day < 1 or day > 31:
        print("Invalid Day\n")
    else:
        break

Day = str(day)
if day < 10:
    Day = "0" + Day

user_input += Day

# Writing the input to a file
with open("components/Date.txt", "w+") as file:
    file.write(user_input)
