#first of all, breathe
#don't let this intimidate you. break it down a part at a time. You've done all of these separately and now we're just combining them.
'''
Instructions: Create a list with at least 8 numbers, and make sure you have a raandom dispersement between 0-50
Create a loop (which loop would be best given we know how long we're going [the length of the list]?) that runs through the entire list
Inside of your loop, have an if/elif/else that checks AT EACH INDEX OF THE LIST:
if the number is greater than 35: print ("greater than 35")
elif the number is between 20-35: print ("between 20-35")
elif the number is between 5-20: print ("between 5 and 20")
else (the number is less than 5)
'''

def main():
    numbers = [20, 37, 4, 12, 49, 25, 7, 10]
    for x in range(len(numbers)):
        if numbers[x] > 35:
            print(numbers[x], "is greater than 35")
        elif numbers[x] >= 20 and numbers[x] <= 35:
            print(numbers[x], "is between 20 and 35")
        elif numbers[x] >= 5 and numbers[x] < 20:
            print(numbers[x], "is between 5 and 20")
        else:
            print(numbers[x], "is less than 5")
    
main()
