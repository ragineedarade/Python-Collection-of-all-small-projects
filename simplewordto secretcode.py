def encode(massage):
    massage = list(massage)
    massage.append(massage[0])
    massage.remove(massage[0])
    str1 = ""
    for i in massage:
        str1 += i
        return "jar"+str1+"raj"

    def decoder(message):
        str1 = massagestr1 = str1[3:]
        m = str1[-1]
        str1 = str1[:-1]
        str1 = m+str1
        return str1
    massage = input(" enter the message")
    print(" press e for endoder and d for docder")
    choice = input()
    print(encode(massage)) if choice == "e" else print(decoder(massage))
