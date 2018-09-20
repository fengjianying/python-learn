###列表(可变)
py_type = ["string","number","list","tuple","dictionary"]
print(py_type);
human = ["body","head"];
human.append("leg"); ##列表末尾增加
human.insert(1,"arm"); ##在第0个后面增加
print(human)
del human[0] ##删除第0个元素
print(human)
poped_human = human.pop(); ##删除最后一个元素并使用它(括号内可添加元素对应的序号值)
print(poped_human)
human.remove("arm"); ##根据值直接删除元素
print(human)

learn = ['javascript','python','java','php']
print(sorted(learn)) #临时性正排序
print(learn);
learn.sort();#永久正排序
print(learn);
learn.reverse();#永久倒排序
print(learn)
print(len(learn))#列表长度

for x in learn: #for循环
    print(x)
print("for is end!")

for x in range(0,len(learn)):#常用for循环遍历列表
    print(learn[x]);

nums = list(range(1,6));#创建一个从1开始到小于6的列表
print(nums)
nums1 = list(range(0,15,2))#创建一个从0开始到小于15每个相差2的列表
print(nums1);

squares = []   #创建列表
for x in list(range(1,11)):
    squares.append((x**2))
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
#列表解析
squares = [value**2 for value in range(1,11)]
print(squares)
##demo test
#1数到20
nums = [value for value in range(1,21)]
print(nums)
#计算1-1000000的总和
lists = [value for value in range(1,1000001)]
print(min(lists))
print(max(lists))
print(sum(lists))
#1-20之内的奇数
lists = list(range(1,20,2))
print(lists)
#3-30内3的倍数
newList = [value for value in range(0,31,3)]
print(newList)
#--------------------------------------------
###元组(不可修改)
dimensions = (200,50)
print(dimensions)