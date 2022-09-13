from pprint import pprint
string = "My Name Is Pratik"
# counter = 0
# for char in string:
#     if char != ' ':
#         counter = counter + 1

# print(counter)

lettersfromstring: str = {}

for character in string:
    if character in lettersfromstring:
        lettersfromstring[character] += 1

    else:
        lettersfromstring[character] = 1

pprint(lettersfromstring, width=1)
char_frq_sort = sorted(
    lettersfromstring.items(),
    key=lambda key_var: key_var[1],
    reverse=True)
print(char_frq_sort[0])
