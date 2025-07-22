list1=[int(input().rstrip()) for _ in range(9)]
maxNum=max(list1)
print(maxNum)
print(list1.index(maxNum)+1)
