#practice question

# PQ 3: WAF to find the factorial of n . (n is the parameter)

def calc_fact(n):
    fact =1
    for i in range(1, n+1):
        fact*=i
    print(fact)
    
calc_fact(5)


# PQ 4: WAF to convert USD to INR.

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(1)


# PQ : Do your self : check even odd

def check_num(num):
    if(num % 2 == 0):
        print("Even")
    else:
        print("Odd ")

check_num(4)