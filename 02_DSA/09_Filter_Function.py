items = [
    ("Product1", 10),
    ("Product2", 100),
    ("Product3", 1),
]

x = list(filter(lambda item: item[1] >= 10, items))  # -->> FILTER FUNCTION
print(x)
#  x = list(map(lambda item: item[1], items))# -->> MAP FUNCTION
