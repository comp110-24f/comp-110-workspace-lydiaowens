# def total_cost(price: int, tax_rate: float):
# print(price + (price * tax_rate))


# print(total_cost(price=100, tax_rate=0.07))


def total_cost(price: int, tax_rate=float):
    return price + (price * tax_rate)


print(total_cost(price=100, tax_rate=0.07))
