class Calculator:
    def modulo(self, a, b):
        return a & b
    

if __name__ == "__main__":
    calc = Calculator()
    print("Modulo: ", calc.modulo(10,5))