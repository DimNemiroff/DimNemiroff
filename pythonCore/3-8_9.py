quantity = 0
discount = 0.0
cost = 0


def cost_delivery(quantity, *_, discount = 0.0):
    """Функція повертає суму за доставлення замовлення.

     Перший параметр quantity - це кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""
    global cost
    cost = (5 + 2 * (quantity - 1)) *(1 - discount)
    print(cost)
    return cost    



cost_delivery(2, 1, 2, 3)
cost_delivery(3, 3)
cost_delivery(1)
cost_delivery(2, 1, 2, 3, discount = 0.5 )
print(cost_delivery.__doc__)
