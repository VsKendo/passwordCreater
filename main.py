from generate import init, generate

table = init(True, False, False, False)
print(table)
result = generate(20, table)
print(''.join(result))
