def split_x(x):
    lst=[]
    cnt=0
    for i in range(len(x)):
        if x[i] == '-' or x[i]=='*' or x[i]=='+':
            lst.append(int(x[cnt:i]))
            lst.append(x[i])
            cnt=i+1
    lst.append(int(x[cnt:]))
    return lst

def oper_xy(x,y,z):
    if z == '*':
        return x*y
    elif z == '+':
        return x+y
    elif z == '-':
        return x-y

def oper_num(x,o_num,num):
    oper_lst = [['*','-','+'],['*','+','-'],['+','*','-'],['+','-','*'],['-','+','*'],['-','*','+']]
    lst=[]
    cnt=0

    for i in range(len(x)):
        if x[i] == oper_lst[o_num][num]:
            for j in range(cnt,i-1):
                lst.append(x[j])
            lst.append(oper_xy(x[i-1],x[i+1],x[i]))
            cnt = i+2
            break
    for j in range(cnt,len(x)):
        lst.append(x[j])
    
    return lst

def oper_all(x,o_num):
    while True:
        if x == oper_num(x,o_num,0):
            break
        else:
            x=oper_num(x,o_num,0)
    while True:
        if x == oper_num(x,o_num,1):
            break
        else:
            x=oper_num(x,o_num,1)
    while True:
        if x == oper_num(x,o_num,2):
            break
        else:
            x=oper_num(x,o_num,2)
    if x[0] > 0:
        return x[0]
    else:
        return x[0]*-1
        
    
def solution(expression):
    expression = split_x(expression)
    lst=[]
    for i in range(0,6):
        lst.append(oper_all(expression,i))
    return max(lst)