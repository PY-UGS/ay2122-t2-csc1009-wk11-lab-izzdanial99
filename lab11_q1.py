class Calculator:
    def __init__(self,input1,input2):
        self.input1 = input1
        self.input2 = input2
    
    def adder(self,input1,input2): #addition
        print("Addition of the 2 numbers: " + str(self.input1 + self.input2))
        return

    def subtractor(self,input1,input2): #subtraction
        print("Subtraction of the 2 numbers: " + str(self.input1 - self.input2))
        return

    def multiplier(self,input1,input2): #multiplication
        print("Multiplicataion of the 2 numbers: " + str(self.input1 * self.input2))
        return

    def divider(self,input1,input2): #division
        print("Division of the 2 numbers: "+ str(self.input1/self.input2))
        return
    
    def clear(self): #set both numbers to 0
        self.input1 = 0
        self.input2 = 0
        print("CLEARED!\nInput1 = ",self.input1,"\nInput2 = ",self.input2)

def main():
    input1 = float(input("Enter first number: ")) #take user input for first number
    input2 = float(input("Enter second number: "))#take user input for second number
    calc = Calculator(input1,input2) #create new calculator object called calc
    calc.adder(input1,input2)
    calc.subtractor(input1,input2)
    calc.multiplier(input1,input2)
    calc.divider(input1,input2)
    calc.clear()


if __name__ == "__main__":
    main()