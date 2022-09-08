# instructions: print out "Hello World!"
# create a variable to hold your favorite color, then print out that variable with a string beforehand that says "My favorite color is: "
# create a variable to hold your birthday (NO SLASHES, JUST THE DIGITS) and then print out "My birthday is: " with the variable

#I needed to change the name of the function because there was a conflict with main because they both are under the assignment 1 file
def hello_world():
    print("Hello World!")
    fav_color = "purple"
    print("My favorite color is: " + fav_color)
    birthday = 10042003
    print("My birthday is: " + str(birthday))




hello_world()
