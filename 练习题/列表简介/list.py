name_list = ['滨滨', '丽丽']
for name in name_list:
    print(name)
    print(f"{name}，早上好！")

dinner_namelist = ['爸爸', '妈妈', '我']
for name in dinner_namelist:
    print(f"{name}，来吃饭啦！")
cantcome = "爸爸"
print(f"{cantcome}无法赴约")
dinner_namelist[0] = "姑姑"
for name in dinner_namelist:
    print(f"{name}，来吃饭啦！")

print("我找到了张大桌子")
dinner_namelist.insert(0, '爷爷')
dinner_namelist.insert(1, '奶奶')
dinner_namelist.append('外婆')
print(dinner_namelist)
for name in dinner_namelist:
    print(f"{name}，来吃饭啦！")

print("只能邀请两位")
n = int(len(dinner_namelist))
print(n)
while n > 2:
    go_name = dinner_namelist.pop()
    print(f"{go_name}，你不用来了，对不起")
    n = n-1
for people in dinner_namelist:
    print(f"{people}，你还是可以来")
while n > 0:
    del dinner_namelist[-1]
    n = n - 1
print(dinner_namelist)

trip_list = ['a', 'b', 'c', 'd', 'e']
print(trip_list)
print(trip_list.sorted())
