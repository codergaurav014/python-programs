print("Welcom to gaurav's calculater")

first_num = input("Enter first number:")
operator = input("Enter operator +,-,*,/,%:")
second_num = input("Enter second number:")

first_num = int(first_num)
second_num = int(second_num)

if operator == "+":
    print(first_num + second_num)

elif operator == "-":
    print(first_num - second_num)

elif operator == "*":
    print(first_num * second_num) 

elif operator == "/":
    print(first_num / second_num)  

elif operator == "%":
    print(first_num % second_num)    

else :
    print("Invelid Operation")