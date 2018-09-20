###字典
alien_0 = {
    'color':'green',
    'point':5
}
print(alien_0['color'])
#增加键值
alien_0['live'] = 3;
print(alien_0);
#删除键值
del alien_0['live']
print(alien_0)
people = {
    'first_name':'Li',
    'last_name':'ming',
    'age':20,
    'height':175
}
#遍历所有的键-值对
for key,value in people.items():
    print(key)
    print(value)
#遍历所有的键
for key in people.keys():
    print(key)
#遍历所有的值
for value in people.values():
    print(value)
#input
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

age = input("how old are you")