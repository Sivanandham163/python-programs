#get input from user as string
string1,string2 = input().split()

#convert into the integer
diagonal1 = int(string1)
diagonal2 = int(string2)

#use formula to get output
ans = (diagonal1 * diagonal2)//2
print(ans)
