number = input()
new_number = ''
if len(number) == 5:
    new_number = number[::-1]
elif len(number) == 6:
    new_number = number[0]
    for i in range(1, len(number)):
        new_number += number[-i]
print(int(new_number))
