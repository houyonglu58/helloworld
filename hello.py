print("hello world")

#foramt.PY              作用：后面跟参数，替换到格式{}所在位置
age=20
name="Rose"
print("{0} was {1} years old when he wrote this book".format(name, age))
print("why is {0} playing witht that python".format(name))

# 将字符串参数化成{0}和{1} 或者直接{}不加数字也可以（python最小是0不是1）
print("{0:_^11}".format("hello"))

# 用^定义"___hello___" 字符串长度为11

#print.PY              会自动换行，若不想换行想连续打，用end="",若想空格，则end=" "
print("a", end="")
print("b", end="")
#ab
print("a", end=" ")
print("b", end=" ")
print("c")
#a b c

#用\表示含有单引号'的字符串，防止系统混淆''的开始于结尾 (\\适用于双引号")
print('what\s your name?')
print("what\\s my name?")

#用\n换行，用\表示不换行，继续
print("this is Rose\nthis is Mary")
s="this is Rose.\
 this is Mary."
s="this is a string.\
this should be continued. "
print(s)

# 变量 运算 =表达式 等于变量=变量 运算 表达式
a=2
a=a*3
a*=3 #结果是一样的


#if.PY                   条件命令
number= 23
token_my = int(input("Enter an integer:")) #input把输入的东西带回到原本的代码
if token_my ==number:      #小心不要忘了冒号
    print("Congratulations, you won a big prize")
    print("And you will be contacted soon")
elif token_my < number:    #也是不要忘了冒号
    print("Sorry, better luck next time")
else:                      #不要忘了冒号
    print("Hey, you will have a small prize")
print("Done!")


#while.PY                  重复循环，比if好在于，不断run直到猜中为止，if每次猜测都要重新运行程序
number=23
count=1
while (count<=10) :
    token_my=int(input("Enter an integer"))
    if token_my==number:       #小心不要忘了冒号
        print("Congratulations, you won a big prize")
        print("And you will be contacted soon")
    elif token_my<number:
        print("Sorry, better luck next time")
    else:
        print("Hey, you will have a small prize")
    count=count+1


#break.PY                         终止循环
while True:
    s=input("Enter something")
    if s == "quit":
        break
    print("Length of the string is", len(s))
print("Done")

#continue.PY               跳过当前循环的剩下步骤，进入新的一轮重复
while True:
    s=input("Enter something")
    if s=="quit":      #特意不处理"quit"这个单词
        break
    if len(s)<3:        #如果字符小于3，输入"too small"且不做处理
        print("too small")
        continue           #若没有continue则len<3的会同时出现"too small"和"input is of sufficient length"
    print("input is of sufficient length")     #只有满足上面两个条件，才可以打出这句话


#for.PY
for i in range(1, 5):
    print(i)
else:
    print("Done!")



#def.PY                            用来自定义函数,记得有逗号
def print_max(a,b):
    if a>b:
        print("the max is",a)
    elif a==b:
        print(a,"is equal to",b)
    else:
        print("the min is", b)

a=3
b=4
print_max(a,b)


#global.PY                            global表示x的变化影响主代码中x的值
x=50
def func():
    global x
    print("x is",x)
    x=3
    print("changed global x to",x)

func()
print("value of x is", x)

# 答案是：x is 50;changed global x to 3; value of x is 3 (若没有global，则value of x is 50)



#return.PY            返回某一数值
def minimun (a,b):
    if a>=b:
        return b
    elif a == b:
        print ("they are equal")
    else:
        return a
print(minimun(a,b))

