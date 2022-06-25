'''
A python program that checks if a letter exists in a string; if it does
exist, it prints its index; if it does not exist, it prints a message " the letter is
not found"
-Ask the usr to enter the string, and the letter looking for
-use for loop to iterate thru the string

'''
string, letter= input("Enter the string and the letter you are looking for: ").split()

for c in string:
    if letter == c:
        print ("The index of "+letter+" is ",string.index(c))
        break
else: print (letter+" is not in "+string)# else is executed when the for loop continues normally
print ("thanks!")
