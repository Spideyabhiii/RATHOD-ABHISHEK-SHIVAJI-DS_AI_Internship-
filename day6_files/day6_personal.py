name = input("Enter your name: ")
goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    file.write("Name: ")
    file.write(name)
    file.write(", Daily Goal: ")
    file.write(goal)
    file.write("\n")
print("Entry saved successfully.")
