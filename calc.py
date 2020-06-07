class calc:
    def __init__(self):
        self.a = int(input("Enter the first number"))
        self.b = int(input("Enter the second number"))
    def add(self):
        print("result = ", self.a+self.b)
    def sub(self):
        print("result = ",self.a-self.b)
    def mul(self):
        print("result = ", self.a*self.b)
    def div(self):
        print("result = ",self.a//self.b)
c = calc()
op = input("enter the operation (+,-,*,/): ")
if op == "+":
    c.add()
elif op == "-":
    c.sub()
elif op == "*":
    c.mul()
elif op == "/":
    c.div()
else:
    print("invalid syntax!!")


