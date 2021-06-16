def armstrong_number(num):
    sum = 0
    temp = num
    while(temp>0):
        digits = temp%10
        sum = sum + (digits**3)
        temp = temp//10
    if num == sum:
        print(f"(num) is an armstrong number ")
    else:
        print(f"(num) is not an armstrong number ")
num = int(input("Enter a number "))
armstrong_number(num)