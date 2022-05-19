def simpleInterest(A, N, I):
    SI = (A * N * I) / 100
    return SI


A = float(input("Enter the principal amount : "))

N = float(input("Enter the number of years : "))

I = 2

# calculate simple interest by using this formula
SI = simpleInterest(A, N, I)

# print
print("Simple interest : {}".format(SI))