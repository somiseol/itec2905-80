from datetime import date

# INPUTS
name = input("what's your name?: ")
dob_month = int(input("what's your birth month in number form?: "))

# PROCESS
name_len = len(name)
curr_month = date.today().month

# OUTPUTS
print(f"hello, {name}")
if curr_month == dob_month:
    print("happy birth month")
print(f"there are {name_len} numbers in your name")
