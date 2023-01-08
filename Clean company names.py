import csv

# Location of raw company names
raw_names = "C:/Users/ADMIN/OneDrive - Cardiff Metropolitan University/Project semester/Python codes/raw_names.csv"

# Read the names from the CSV file
with open(raw_names, 'r') as f:
    reader = csv.reader(f)

    # Extract the company names
    company_names = []
    for row in reader:
        company_name = row[0].split("PLC")[0]
        company_name = company_name.split("ORD")[0]
        company_names.append(company_name)

# Write the company names to a CSV file
with open("cleaned_names.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([[name] for name in company_names])