#loop : iteration : repetition
'''
#1 to 10, 10 + 1 = 11
for x in range(1,11):
    print(x,"hello")


#2) display table of N, N = 3, 3 x 1 =3, 3x2=6

N=int(input("Enter N : "))
for i in range(1,11):
    print(N,'x',i,'=',N*i)



#3) display factors of N, 28: 1,2,4,7,14,28 : 1 to 28, N: 1 to N

c=0
N=int(input("Enter N : "))
for i in range(1, N+1):
    if N%i ==0:
        print(i,"is factor of",N)
        c+=1
print(c)
if c==2:
    print(N,"is prime number")
else:
    print(N,"is composite number")


#3) summation of N natural numbers

sum=0
N=int(input("Enter N : "))
for i in range(1,N+1) :
    sum = sum + i
print(sum)


'''
for i in range(1,4):
    for j in range(0,6): #for each value of i,j's loop will run fully
        print('+',end=' ')
    print()