class Calculator() :
    def add(num1 ,num2):
        sum = num1 + num2
        print("Sum of " , num1 ,  "and" , num2 , "is : " , sum)

    def multiply(num1 ,num2):
        prod = num1 * num2
        print("prod of " , num1 ,  "and" , num2 , "is : " , prod)

    def divide(num1 ,num2):
        quo = num1/num2
        print("Quotient of " , num1 ,  "and" , num2 , "is : " , quo)

    def subtract(num1 ,num2):
        sub = num1 - num2
        print("Difference of " , num1 ,  "and" , num2 , "is : " , sub)

class UseCalculator(Calculator):
    def __init__(self, num1 , num2) :
        self.num1 = num1
        self.num2 = num2
        

calc1 = UseCalculator.add(50, 50)
calc1 = UseCalculator.multiply(50, 50)
calc1 = UseCalculator.divide(50, 50)
calc1 = UseCalculator.subtract(50, 50)



