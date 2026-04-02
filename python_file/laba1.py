'''def my_function(x):
    return 5*x

print(my_function(2))
print(my_function(30))

def my_god(x):
    print(5*x)
my_god(3) 
 

def my_fun(food):
    for x in food:
        print(x)
food=["apple",'orange']
my_fun(food)

'''
'''
class Math:
    def add(self, a, b, c=0):
        return a + b + c

m = Math()
print(m.add(2, 3))     # 5
print(m.add(2, 3, 4))  # 9
'''

import math

class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0
        self.area = 0

    def Set(self):
        self.length = float(input("Enter length: "))
        self.breadth = float(input("Enter breadth: "))

    def Calculate(self):
        self.area = self.length * self.breadth
        print(f"Area of Rectangle: {self.area}")
class Imain:
    @staticmethod
    def main():
        print("Rectangle Calculation:")
        rect = Rectangle()
        rect.Set()
        rect.Calculate()
if __name__ == "__main__":
    Imain.main()
'''


#q no 1
source_file = 'f1.txt'

destination_file = 'f2.txt'

with open(source_file, 'r') as src:
    content = src.read()
   
    words = content.split()

with open(destination_file, 'w') as dest:
    for word in words:
        if word.lower().startswith('r'):
            dest.write(word + '\n')  

print("Words starting with 'r' have been transferred to", destination_file)

'''
''''
# q no 2

a = open("l1.txt","r")
lines=a.readlines()
print('first three lines:\n\n',*lines[:3])
print('last three lines:\n\n',*lines[-3:])


#q no 3



f1="wasp"
f2="swap"
if sorted(f1)==sorted(f2):
    print('these words are anagram')
else:
    print('these are not anagram')
   
'''