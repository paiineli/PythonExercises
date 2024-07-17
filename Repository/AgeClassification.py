# 01 - create the variable

age = input("how old are you? ")
# since it's in "", the value is str
if int(age) < 16:
    print("minor")
elif int(age) > 18:
    print("adult")
else:
    print("emancipated")

# 02 - get the swimmer's age and classify in the table:

age = input("hello swimmer! how old are you? ")

if int(age) > 4 and int(age) < 8:
    print("infant a")
elif int(age) > 7 and int(age) < 11:
    print("infant b")
elif int(age) > 10 and int(age) < 14:
    print("youth a")
elif int(age) > 13 and int(age) < 18:
    print("youth b")
else:
    print("you do not belong to the swimming group")
