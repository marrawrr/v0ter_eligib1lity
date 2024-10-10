print("Voter Eligibility.")
print("Are you able to vote come next election? Please respond with (y/n).")
age = int(input("Please enter your age: "))

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).lower()
        if response in ["y", "n"]:
            return response
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

citizen = get_yes_no_input("Are you a legal citizen of the US? (y/n): ")
registration = get_yes_no_input("Are you registered to vote? (y/n): ")
incarceration_status = get_yes_no_input("Are you currently incarcerated? (y/n): ")
eligible = False

if age >= 18 and citizen == "y" and registration == "y" and incarceration_status == "n":
    eligible = True

if eligible:
    print("You are eligible to vote! See you this upcoming election season!")
else:
    print("Sorry, you are not eligible to vote.")
