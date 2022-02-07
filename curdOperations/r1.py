num = int(input("enter number"))
a = 0
b = 1
x = [2, 5, 4, 8, 10]
for i in range(0, num):
    print(x[a])
    nth = a + b
    a = b
    b = nth
if __name__ == '__main__':
    print(pow(2, 4))
