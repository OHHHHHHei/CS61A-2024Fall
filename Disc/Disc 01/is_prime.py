def is_prime(n):
    if  n < 2:
        return False
    i = 2
    isprime = 1
    while i < n:
        if n % i == 0:
            isprime = 0
            break   # 找到因子后立即退出
        i += 1
    if isprime == 0:
        return False
    else:
        return  True
            
