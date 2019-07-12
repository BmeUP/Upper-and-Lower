def vol(rad):
    return (((rad**3)*4)/3)*3.14
print(vol(2))
#print(f"{num} is in the range between {low} and {high}")
#----------------------------------------------------------------------------------------#
lis = []
def ran_check(num, low, high):
    for i in range(low-1, high+1):
        lis.append(i)
    if num in lis:
        print(f"{num} is in the range between {low} and {high}")
    else:
        print(f"{num} is'nt in the range between {low} and {high}")

num = int(input("Input cheking number here: "))
low = int(input("Input lowest value here: "))
high = int(input("Input highest value here: "))
ran_check(num, low, high)
#----------------------------------------------------------------------------------------#
lower = []
upper = []
def up_low(s):
    for i in s:
        if i.isupper():
            upper.append(i)
        #elif i == [" ", "!", ".", ",", "!"]:
            #return 0
        elif i.islower():
            lower.append(i)
s = input("Input some string: ")
up_low(s)
print(f"""Original String :  {s}
No. of Upper case characters :  {len(upper)}
No. of Lower case Characters :  {len(lower)}

""")
    
    

       
            


