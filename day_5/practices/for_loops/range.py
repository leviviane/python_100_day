#using the range function
for num in range(1,10): #this will print all the numbers from 1-10 but not including 10
    print(num)

#step range
for num in range(1, 11, 3): #this will print the numbers in step by 3
    print(num)

#getting the range of 1-100
sum = 0
for num in range(1, 101):
    sum += num
print(sum)

#adding the range of num from 1-1000 using even numbers only
target = int(input())

sum = 0
for num in range(2, target + 1, 2):
    sum += num
print (num)

#second way to do this

target = int(input())
sum = 0
for num in range(1, target + 1):
    if num % 2 == 0:
        sum += num
print(num)
