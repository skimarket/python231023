#DemoDict.py
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print(phone)
print(len(phone))
print(phone["kim"])
#include의 약자(멤버쉽)
print("park" in phone)
print("kang" not in phone)

#항상 객체의 참조가 전달된다.
p=phone
print(p)
print(phone)
print(id(phone), id(p))

#장비 관리
device = {"아이폰":5, "아이패드":10}
print(device["아이폰"])
#입력
device["맥북"] =15
#수정
device["아이폰"]=6
print(device)
#삭제
del device["아이폰"]
print(device)

for item in device.items():
    print(item)

for item in device.keys():
    print(item)

for item in device.values():
    print(item)

print("bool(0)" , bool(0))
print("bool(3)", bool(3))
print("bool("")", bool(""))
print("bool(test)",bool("test"))
print("bool([])", bool([]))
print(bool([1,2,3]))
print("---논리식---")
print("1<2 : ", 1<2)
print("1!=2 : ", 1!=2)
print("1==2 : " , 1==2)
print("True and True and True : ", True and True and True)
print("True and True and False : ", True and True and False)
print("True and False and False : ", True and False and False)
print("5/2 : " , 5/2)
print("5//2 : " , 5//2)
print("5%2 : " , 5%2)

