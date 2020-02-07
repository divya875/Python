str2 = ""


def string_alternative(str):
    for i in range(len(str)):
        # This % will gives us character at even number of the string
        if i % 2 == 0:
            print(str[i], end="")


if __name__ == '__main__':
    str = str(input("Please input the string : "))
    print("The given data :", str)
    string_alternative(str)
