katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        num = 1
        line = "The line is currently: "
        for name in katz_deli:
            line += f"{num}. {name}"
            if name != katz_deli[-1]:
                line += " "
            num += 1
        print(line)
            


def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    num = katz_deli.index(new_customer) + 1
    print(f"Welcome, {new_customer}. You are number {num} in line.")

# take_a_number(["ben", "chris"], "ken")
def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
