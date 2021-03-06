import csv
from pathlib import Path


loan_costs = [500, 600, 200, 1000, 450]

print("Number of Loans: ", len(loan_costs))
print("Total of Loans: ", sum(loan_costs))
print("Average: ", sum(loan_costs) / len(loan_costs))


loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
future_value = loan.get("future_value")
print("Future Value: ", future_value)
remaining_months = loan.get("remaining_months")
print("Remaining Months: ", remaining_months)

present_value = future_value / (1 + 0.20/12)**remaining_months
print("Present Value: ", present_value)

if present_value >= loan.get("loan_price"):
    print("The loan is worth the cost to buy")
else:
    print("The loan is too expensive")

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
present_value = new_loan.get("future_value") / (1 + 0.20/12)**new_loan.get("remaining_months")
print(present_value)

annual_discount_rate = 0.20

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]
inexpensive_loans = []
for loany in loans:
    if loany.get("loan_price") <= 500:
        inexpensive_loans.append(loany)
        print("Inexpensive Loans List: ", inexpensive_loans)


header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]


output_path = Path("inexpensive_loans.csv")
print("Saving to file...")


with open(output_path, "w") as output_file:
    csvwriter = csv.writer(output_file)

    csvwriter.writerow(header)

    for inexpensive_loan in inexpensive_loans:
        csvwriter.writerow(inexpensive_loan.values())

print(f"Inexpensive loans were saved to {output_path.absolute()}")
