###if语句
car = 'Subaru'
print(car == 'harfe')
print(car == car.lower())
#根据年龄判断价格
ages = [0,10,15,20]
for x in ages:
    if x<4:
        print("Your admission cost is $0.")
    elif x<18:
        print("Your admission cost is $5.")
    else:
        print("Your admission cost is $10.")
        