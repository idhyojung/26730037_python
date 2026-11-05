#List

a = 1,2,3     #<--turple
a = list(a)
print(type(a))

#set(고유한 값을 갖는다, 순서가 없다)

b = [1,2,3,1,2,3,1,2,3]
a = set
print(*a)

#len() 개수 반환
fruits = {"apple","banana","grape"}
size = len(fruits)
print(size)

#in포함되는지

fruits = {"apple","banana","grape"}
if"apple" in fruits:
    print("apple 있습니다.")
else:
    print("없습니다")

#출력 순서가 없다

fruits = {"apple","banana","grape"}
print(fruits)

#add()요소 추가

fruits = {"apple","banana","grape"}
fruits.add("kiwi")
print(fruits)
fruits.discard("o")#remove()
print(fruits)
fruits.clear()
print(fruits)



