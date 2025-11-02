num=int(input("Enter a number:"))
power = len(str(num))
print(power)
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10
if sum == num:
    print(num, "Is a Armstrong number")
else:
    print(num, "Is not a Armstrong number")


