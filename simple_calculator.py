class Calculator:
    def add(self, a,b):
        return a + b
    
    def substract(self, a, b):
        return a - b
    
    def divide(self, a, b):
        return a/b

if __name__ =="__main__":
    calc = Calculator()
    print("Addition: ", calc.add(10,5))
    print("Substraction: ", calc.substract(10,5))
    print("Division: ", calc.divide(10,5))