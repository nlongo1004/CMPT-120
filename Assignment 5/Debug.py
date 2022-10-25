def main():
    #good working example!
    stringInput = input("enter a string")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")
        
    #can you google and find what function you should use to check if it's numeric (an int?)?
    intInput = input("enter an int")
    if intInput.isdigit():
        print("int!")
    else:
        print("not int :(")
    
    #what about if it's both letters and numbers?
    alphIntInput = input("Enter letters and numbers")
    if alphIntInput.isalnum():
        print("Letters and numbers!")
    else:
        print("weird characters :(")
       
    #good working example
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")
        
    #now write code to check if the input was either an asterisk OR an ampersand (&)
    character = input("Enter an asterisk or an ampersand: ")
    if character == "*" or character == "&":
        print("successful")
    else:
        print("wtf no")
        
    #do the live example we did in class: ask user to input an integer, but before you cast it to an int, check that it's an integer before doing your variable = int(variable) command
    number = input("Enter an integer: ")
    if number.isdigit():
        x = int(number)
        print("It is an int", type(x))
    else:
        print("This is not an int")

    # last challenge: find out how to check if the string input has the substring "marist"
    #google this one ;) substring is the key google term
    word = input("Enter a string: ")

    if 'marist' in word:
        print("Marist is included")
    else:
        print("Marist is not included")
    
main()
