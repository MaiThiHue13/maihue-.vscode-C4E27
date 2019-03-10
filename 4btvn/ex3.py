print("Answer the following algebra question:")
print("If x=8, then what is the value of 4(x+3)?")
choice={"1":"35", "2":"36", "3":"40", "4":"44"}
print(choice)
for k, v in choice.items():
    print(k,v)

n=int(input("mời nhập câu trả lời: "))

if n==4:
    print("Your choice: ",n)
    print('Bingo')
else:
    print("Your choice: ", n)
    print(":(")