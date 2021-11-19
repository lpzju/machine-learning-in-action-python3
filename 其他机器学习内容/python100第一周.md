跟着python100学习一下

***

100以内的素数

```python
# 输出100以内的所有素数
# 想法：从1到100遍历，假设得到了i=17，那么此时从1到9遍历，如果找到了一个数用17能除尽则跳出循环
# 如果找不到这个数，那么把i输出为素数
for i in range(2,100):
    flag = True
    for k in range(2,int(i/2)+1):
        if i%k == 0:
            flag = False
            break
    if flag:
        print("%d为素数"%i)
```

1000以内完美数

```python
# 找出10000以内的完美数
# 所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身
# 6（$6=1+2+3$）和28（$28=1+2+4+7+14$）

# 思路：从3到10000遍历，如此时找到的数为8，那么把它进行因式分解，用一个列表进行添加。首先是1，1能被8整除，添加
# 然后是2，2也可以被整除，添加，最后添加4，不添加8
# 然后从列表进行遍历，如果所有数字加和是这个数，那么就输出

for i in range(3,10000):
    list1 = []
    for j in range(1,i):
        if i%j == 0:
            list1.append(j)
    sum = 0
    for k in list1:
        sum += k
    if sum == i:
        print(i)
```

斐波那契数列前20个数

```python
# 生成斐波那契数列的前20个数
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# 应该写一个迭代函数fn()，如果是0或者1，则返回1，其余则返回fn(n-1)+fn(n-2)

# fn(1)=1,fn(2)=1
def fn(n):
    if n == 2 or n == 1:
        return 1
    else:
        return fn(n-1)+fn(n-2)
    
for i in range(1,21):
    print("fn(%d):%d"%(i,fn(i)))
```

百钱百鸡

```python
# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for little in range(101):
    for f in range(34):
        for m in range(21):
            if m*5+f*3+little/3 == 100:
                print("公鸡为：%d\n母鸡为：%d\n小鸡为：%d"%(m,f,little))
                print("\n")
```

水仙数

```python
# 寻找水仙数
# 描述：水仙数是三位数，每位数的立方和为数本身
for i in range(100,1000):
    sum1 = 0
    k = str(i)
    for j in k:
        sum1 += int(j)*int(j)*int(j)
    if sum1 == i:
        print(i)
```

公约数

```python
def gongyueshu(m,n):
    num = 0
    total = 1
    if m>n:
        num = n
    else:
        num = m
    while num>=1:
        if m%num == 0 and n%num == 0:
            total = num
            break
        else:
            num -= 1
    print(total)
```

公倍数

```python
def gongbeishu(m,n):
    num = m
    while num%n!=0 or num%m!=0:
        num += 1
    print(num)
```

回文数

```python
# 实现判断一个数是不是回文数的函数
# 给定一个数，获得各位置的数字
# 如743，当743//10不为0，首先743%10获得3，然后743//10获得74，然后均存在列表中
def huiwen(n):
    flag = True
    list1 = []
    while True:
        list1.append(n%10)
        n = n//10
        if n == 0:
            break
    for i in range(len(list1)):
        if list1[i] != list1[len(list1)-i-1]:
            flag = False
            break
    print(flag)
```

生成器和匿名函数

```python
dataSet = [[1, 1, 'yes'],
           [1, 1, 'yes'],
           [1, 0, 'no'],
           [0, 1, 'no'],
           [0, 1, 'no']]

firstLineList = [example[0] for example in dataSet]
tempDict = {}
for value in firstLineList:
    if value not in tempDict:
        tempDict[value] = 0
    tempDict[value] += 1
sortedDict = sorted(tempDict.items(),key=lambda x:x[1],reverse=True)
print(firstLineList)
print(sortedDict)

[1, 1, 1, 0, 0]
[(1, 3), (0, 2)]
```

yield函数

```python
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print(next(g))
```

yield与斐波那契数列

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a,b


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
```

