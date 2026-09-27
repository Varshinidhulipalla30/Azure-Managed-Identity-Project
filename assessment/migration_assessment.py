import csv

with open("assessment/application_inventory.csv", "r") as file:
    reader = csv.DictReader(file)

    print("======================================")
    print("MANAGED IDENTITY ADOPTION ASSESSMENT")
    print("======================================")

    for row in reader:
        print()
        print("Application:", row["Application"])
        print("Current Authentication:", row["Current Authentication"])
        print("Managed Identity Support:", row["Managed Identity Support"])

        if row["Managed Identity Support"] == "Yes":
            print("Recommendation: Migrate to Managed Identity")
        else:
            print("Recommendation: Store secret in Azure Key Vault")
