# 1. 1~100 能被7整除的数
print("1. 1~100能被7整除的数：")
for i in range(1,101):
    if i %7 ==0:
        print(i, end=" ")
print("\n")

# 2. continue跳过偶数，输出奇数
print("2. 1~100奇数：")
for i in range(1,101):
    if i %2 ==0:
        continue
    print(i, end=" ")
print("\n")

# 3. break到50停止
print("3. 到50停止循环：")
for i in range(1,101):
    if i ==50:
        break
    print(i, end=" ")
print("\n")

# 4. 输出1~100质数
print("4. 1~100质数：")
prime_list = []
for n in range(2,101):
    flag = True
    for j in range(2, int(n**0.5)+1):
        if n % j ==0:
            flag = False
            break
    if flag:
        prime_list.append(n)
print(prime_list)
print("质数和：", sum(prime_list))

# 5. 1~100奇数和
s = 0
for i in range(1,101):
    if i%2 ==1:
        s +=i
print("\n5. 1~100奇数和：", s)
