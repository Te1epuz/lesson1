def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

price=56.24
result = format_price(price)

print(result)