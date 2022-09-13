from pprint import pprint

sentence = "Thims is a common intervmmiew quesmtion"
string = sentence
char_frq = {}
for char in string:
    if char in char_frq:
        char_frq[char] += 1

    else:
        char_frq[char] = 1

#pprint(char_frq, width=2)

char_frq_sort = sorted(
    char_frq.items(),
    key=lambda key_var: key_var[1],
    reverse=True)
print(char_frq_sort[1])
