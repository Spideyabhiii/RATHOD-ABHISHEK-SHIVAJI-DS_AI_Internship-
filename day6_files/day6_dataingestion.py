import csv
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Status"] == "Fail":
            print(row["Name"])

#student.csv
#Name,Grade,Status
#Abhhi,A,Pass
#Shiv,B,Pass
#Shashi,F,Fail
