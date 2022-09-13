browsing_session = [1, 2, 3]
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
print(browsing_session)
for page in browsing_session:
    last = browsing_session.pop()
    print(last)
    # print(browsing_session)
    if browsing_session:
        print("Redirecting to website", browsing_session[-1])
