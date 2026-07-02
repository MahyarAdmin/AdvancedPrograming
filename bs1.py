def Clamp(Min, Data, Max) : #Defined a function that limits the data between two given numbers
    if Data < Min : #Returns the min defined value if the data is less than min
        return Min
    elif Data > Max : #Returns the max defined value if the data is more than max
        return Max
    else :
        return Data #Returns the data if non of the above statments are true
def Abs(Data) : #Defined a function to return the absolote value of a given varible
    if Data >= 0 : #Returns the data if the data is possitive
        return Data
    else :
        return -Data #Returns -1*(data) if data is negative
def NewLine(N) : #Defined a function that prints new lines in the times specified by user(via N), you can implement this using the Call-Back method like the class
    for i in range(N) :
        print("") #Prints a emty line witch reprsents a new line in print function and python
MAX = 50 #Defined a variable to use in clamp function(cannot find a const defenition like C++, witch is more practical
MIN = -89 #Same as the privios line
print("Here we ask for a input from user(this system cannot accept and procces strings, you should only enter number)")
print("After the input we will clamp the data between", MAX, "and", MIN)
print("Enter number between", MIN, "and", MAX, ':')
x = input() #Getting a user input
print("Your number is:", Clamp(MIN, int(x), MAX)) #using clamp function(int cast is happening in string to make it work with numbers
del(x, MIN, MAX) #Deleting the variables to free memory(I don't know what it does, just assumed it would work like this)
print("Here we add 3 new lines")
NewLine(3) #Using NewLine function with : N = 3
print("Here we return and print the numbers: '548' and '-98':")
print(Abs(548), Abs(-98)) #Using Abs function two times in print with values : 548 & -98
