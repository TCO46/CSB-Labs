deposit = float(input("Deposit: "))

year1 = deposit * 105/100
year2 = deposit * pow(105/100, 2)
year10 = deposit * pow(105/100, 10)

print(f"Account after 1 year: {year1}\nAccount after 2 year: {year2}\nAccount after 10 year: {year10}")