number = int(raw_input("Enter number: "))
word = str(raw_input("Enter Word: "))

if number == 1:
    print (str(number) + " " + word)

def pluralize(word):
    if word[-3:] == "ife":
        return word[:-3] + "ives"
    elif word[-2:] == "sh" or word[-2:] == "ch":
        return word + "es"
    elif word[-2:] == "us":
        return word[:-2] + "i"
    elif word[-2:] == "ay" or word[-2:] == "oy" or word[-2:] == "ey" or word[-2:] == "uy":
        return word + "s"
    elif word[-1:] == "y":
        return word[:-1] + "ies"
    else:
        return word + 's'


print(str(number) + " " + pluralize(word))
