import csv
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    print("Students:")
    for row in reader:
        if row["Status"].strip().lower() == "pass":
            print(row["Name"])


#student.csv
#Name,Grade,Status
#Abhhi,A,Pass
#Shiv,B,PassS
#Shashi,F,Fail
