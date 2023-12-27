payment = [-585.85,252.25,456.00,27.35,-40.5]
total = 0.0


def amount_payment(payment):
    global total
    for sum in payment:
        if sum > 0.0: 
            total = total + sum
    return total


amount_payment(payment)
print(total)
print(payment)
