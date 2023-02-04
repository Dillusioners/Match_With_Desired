#Author:- Dynamax

x = int(input("Enter the number:- "))
n = int(input("Enter the number of terms:- "))
i = ((x+n)**2)/(x**2 - n**2)
S = 0
print("S =", end=" ")
for j in range(0, n):
    S += (((( n+i/x+i+j )*( n+j+i/x**(j + 2) )) **(j + 2) ) ) / i
    if j != n-1:
        print(f'(((( {n}+{i}/{x}+{i}+{j} )*( {n}+{j}+{i}/{x}^({j} + 2) )) ^ ({j} + 2) ) ) / {i} + ', end=" ")
    else:
        print(f'(((( {n}+{i}/{x}+{i}+{j} )*( {n}+{j}+{i}/{x}^({j} + 2) )) ^ ({j} + 2) ) ) / {i} = {S}', end=" ")
