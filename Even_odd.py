n = int(input("Enter your id: "))
sum = 0
while (n > 0):
  dig = n%10
  sum = sum + dig
  n = n//10
print("The total sum of digits is : ",sum)
if (sum % 2 == 0):
  print((sum),"Is A Even Number")
else:
    print((sum),"Is A odd Number")
flag = False

if sum > 1:
    for i in range(2, sum):
        if (sum % i) == 0:

            flag = True
            break

if flag:
    print(sum, "is not a prime number")
else:
    print(sum, "is a prime number")