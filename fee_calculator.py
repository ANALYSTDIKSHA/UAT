def fee_calc(amount):
    if amount <= 1000:
        return amount * 0.1
    elif amount > 1000 and amount <= 5000:
        return amount * 0.15
    else:
        return amount * 0.2

amounts = [100, 500, 999, 1000, "a", 1500, 3000, 5000, "b",7000, 12000]

for i in amounts:
    try:
        print("Amount is : ", i)
        print("Fee is : ",fee_calc(i))

    except TypeError:
        print("Invalid data")
