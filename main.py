deck = {'2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
inputs = []
for i in range(6):
    key = input()
    if key in deck:
        inputs.append(deck[key])
req = sum(inputs) / 6
print(req)
