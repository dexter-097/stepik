number = input()
new_number = number[0: len(number)-5]
new_number += number[len(number)-5:][::-1]
print(new_number)
