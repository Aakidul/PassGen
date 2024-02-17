import random

def main():
# Main logic
      while True:
        user_input = input("ENTER ANY 'KEY' TO CREATE PASSWORD: ")
        a = len(user_input)
        if (a>0):
            hash = ["12qwErTy8", "Pas32*)#6", "O18NZPgajYw", "@2837#Hdjso(37", "He(72@)", "qwe#629("]
            numbers = ["15362", "838282", "950172", "1121"]
            symbol = ["@", "#", "$", "&", "+", "(", "¢", "%", "(", "/"]
            a1 = random.choice(hash)
            a2 = random.choice(numbers)
            a3 = random.choice(symbol)
            print(a1 + a2 + a3 + user_input)


        else:
            print("PLEASE ENTER ANY KEY! :)")


main()
