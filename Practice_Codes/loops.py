# numbers=[1,-2,-3,4,-5,90,-45]
# positive_count=0
# n=4
# for num in range(1,11):
#     if(num==5):
#         continue
#     print(n, "x", num, "=", n*num)


# n=6
# i=2
# sum=0
# while i<n:
#     sum+=i
#     i+=2
# print(sum) 
    
n=23
i=2

while i < int(n/2):
    if n%i ==0:
        print(n," is not a prime number")
        break
    i+=1
if(i==int(n/2)):    
    print(n," is a prime number")

items=[]