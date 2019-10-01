# sum_n.py
# Nolaundron 'Ray' Harris

def sum_n():
    #Tell the user what this program does.
    
    print("This program finds and prints the sum of the")
    print("first n whole numbers, 1 to n, where n is a")
    print("natural number")
    print()
    
    #Ask user for input.
    
    nInput = eval(input("Please enter a natural number: "))
    
    sum = 0
    n = nInput + 1
    for i in range(1, n):
        sum = sum + i

    #Give the sum of the number 1 to n.
        
    print()       
    print("The sum of the numbers 1 to ",nInput," equals ",sum,".", sep = "")
    
sum_n()
