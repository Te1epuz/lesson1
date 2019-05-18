def get_summ(one, two, delimiter='&'):
    return str(one) + delimiter + str(two)

one='Learn'
two='python'

result = get_summ(one,two,)
print(result)

print(f'{result.upper()}')