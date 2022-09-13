# IF WE OPEN UP A FILE THEN WE SHOULD ALWAYS CLOSE IT
# FOR THAT WE USE CLOSE COMMAND WE SHOULD USE IT IN FINALLY STATEMENT
try:
    file = open("Friends.S01E09.720p.BluRay.x264.200MB-PAHE.in.mkv")
    age = int(input("Age : "))
    div = 100/age
except (ValueError, NameError):
    print("Not a valid value ")
else:
    print("NO exception were thrown")

finally:
    file.close()
    # THIS IS STATEMENT WILL BE EXCUTED NO MATTER WHAT
