num = int(input('Digite um número: '))
print(f'O número digitado foi {num} e sua tabuada é:')
for c in range(1, 11):
    print(f'{num} * {c} = {num * c}')
