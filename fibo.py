def fibo_recursion(n):
    if n<2:
        return n
    else :
        print('내가 호출되고있니?')
        return fibo_recursion(n-1)+fibo_recursion(n-2)
