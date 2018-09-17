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