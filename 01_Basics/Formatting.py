# x = 1
# y = 8
# var = [1, 2, 3, 4, 5]
# for val in var:
#     print(val)

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
    print("Disable")
