
#write a program to find the reverse of given integer number

no=int(input("Enter the number"))
def rev_no(num):
    rev=0
    while num!=0:
        rev=rev*10+num%10
        num=num//10
    return rev


print("The reversd of the given number",rev_no(no))
