"""
mkay so
I talked a lot about helping but not fixing the problem
In this code, if you run this and enter not an integer, it throws an error, as we're aware, as you solved this problem in the debug file
can you google a way to help or even fix this problem that isn't the way we were doing it before?
hint: there's try/catch statements that i didn't teach but is somewhat straightforward to try. There's a thing called regex, etc.
You can also go much, much simpler if you want to, I just want you guys to keep practicing your google skills
and ofc, if you're stuck, don't hesitate to email
"""


def main():
    # user is prompted to enter an integer. If it is an integer, it will cast their input
    # into an int and store that in the variable 'int_input'
    try:
        int_input = int(input("Enter an integer:"))
        print("Good job! That is an integer", int_input)

    # if the user inputs anything that is not an integer, a ValueError will be found.
    # instead of giving an error, this will catch it and print that their input was not a
    # valid integer
    except ValueError:
        print("No, that is not an integer.")


main()
