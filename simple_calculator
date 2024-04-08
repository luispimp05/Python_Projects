# calculator

#add
def add(n1,n2):
    return n1 + n2

#Substract
def subs(n1,n2):
    return n1 - n2

# multiply
def multi(n1,n2):
    return n1 * n2

# divide
def division(n1,n2):
    return n1 / n2


calculator_dic = {
    
    "+": add,
    "-": subs,
    "*": multi,
    "/": division
    
}


function = calculator_dic["*"]
function(2,3)

num1 = int(input("What's the first number?: "))


for symbol in calculator_dic:    
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")


num2 = int (input("What's the second number?: ")) 
calculation_function = calculator_dic[operation_symbol]
first_answer = calculation_function(num1,num2) 
 


print(f"{num1} {operation_symbol} {num2} = {first_answer}")




operation_symbol = input("Pick another operation : ")

num3 = int (input("What's the next number?: ")) 

calculation_function = calculator_dic[operation_symbol]
second_answer = calculation_function(first_answer, num3)


print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")





