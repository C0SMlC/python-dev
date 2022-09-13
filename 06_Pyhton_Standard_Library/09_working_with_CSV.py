import csv  # COMMA SEPARETED VALUE

with open("Data.csv", "w") as file:
    write = csv.writer(file)
    write.writerow(["Roll No", "Name"])
    write.writerow([1, "Pratik"])
