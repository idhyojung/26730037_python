#리스트 요소 값중에 홀수만 출력
nums = [1,2,3,4,5,6,7,8,9,10]
for i in nums:
   if i%2==1:
       print(i,end="")

# 리스트 요소 중에 홀수만 출력
nums = [1, 2, 3, 5, 6, 7, 8, 9, 10]
# 리스트 컴프리헨션
result =[n for n in nums if n%2 == 1]

#join 메서드
#삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

# split 메서드 문자열 -> 리스트
string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
interest1 = string.split("/")
print(interest1)

# split 메서드 문자열 -> 리스트
string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
interest1 = string.split("/")
print(interest1)

# 리스트 정렬 ->리스트이름.sort() (오름차순, 내림차순)
data = [2, 4, 3, 1, 5, 10, 9]
data.sort(reverse=False) # 오름차순 sort()
data.sort(reverse=True) # 내림차순
print(data)

#sorted(리스트이름(-> sorted(리스트이름,reverse=True) <-내림
nums = [5,3,1,4,2]
result = sorted(nums,reverse=True)
print(result)
#별 표현식
a,b,*c = 0,1,2,3,4,5
print("a:",a,"b:",b,"c:",c)

#딕셔너리
a = {}
b = set() #집합

# 딕셔너리 key : value
# 추가 -> dic이름["key"] = value
ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
ice["죠스바"] = 1200
ice["월드콘"] = 1500
print(ice)

#key에 해당하는 value를 찾는다.
#print(ice["key"])

#딕셔너리 요소 삭제
#del ice["key"]

# 딕셔너리 인덱싱 -> 메로나 가격 출력
inventory = {"메로나": [300, 20],
             "비비빅": [400, 3],
             "죠스바": [250, 100]}
print("메로나 가격 :",inventory['메로나'][0]) # 가격
print("메로나 재고 :",inventory['메로나'][1]) # 재고

# 딕셔너리 keys()->key에 집합
print(inventory.keys()) #리스트 변환하려면 리스트 형변환

# 딕셔너리 values()-> value의 집합
print(inventory.values()) #리스트로 반환

# 딕셔너리에 다른 딕셔너리를 추가할때 update
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500}
new_product = {'팥빙수': 2700, '아맛나': 1000}
icecream.update(new_product)
print(icecream)

































       

       
