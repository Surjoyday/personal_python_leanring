class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b


    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def mutiply(self):
        return self.a * self.b
    
    def divide(self):
        if(self.b == 0):
            raise ValueError("Cannot divide by zero.")
        return self.a / self.b



