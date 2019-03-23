
number=23
count=1
while (count<=2) :
    token_my=int(input("Enter an integer"))
    if token_my==number:       #小心不要忘了冒号
        print("Congratulations, you won a big prize")
        print("And you will be contacted soon")
        break
    elif token_my<number:
        print("Sorry, better luck next time")
    else:
        print("Hey, you will have a small prize")
    count=count+1 #count++将count递增，count--将count递减
else:
    print("This is the end")
print("A")
