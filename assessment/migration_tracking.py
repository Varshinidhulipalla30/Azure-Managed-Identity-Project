import csv

with open("assessment/migration_tracking.csv", "r") as file:
    reader = csv.DictReader(file)

    total = 0
    mi_ready = 0
    legacy = 0

    for row in reader:
        total += 1

        if row["Status"] == "Managed Identity Ready":
            mi_ready += 1
        elif row["Status"] == "Legacy Exception":
            legacy += 1

coverage = (mi_ready / total) * 100

print("====================================")
print("MIGRATION TRACKING REPORT")
print("====================================")
print("Total Applications       :", total)
print("Managed Identity Ready   :", mi_ready)
print("Legacy Exceptions        :", legacy)
print("Migration Coverage       :", f"{coverage:.2f} %")
