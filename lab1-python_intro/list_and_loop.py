class_list = []

class_count = input("how many classes are you taking? ")

for i in range(int(class_count)):
    class_list.append(input("> "))

print("\nyou are taking:")
for i, class_name in enumerate(class_list):
    print(f"{i + 1} {class_name}")
