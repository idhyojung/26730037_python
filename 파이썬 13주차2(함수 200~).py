# 함수 정의 def
def print_coin():
    print("비트코인")

# 함수 호출 100번
for _ in range(100):
    print_coin()

# 함수 안에 문자열 100번 출력
def print_coin1():
    print("비트"*100)

#함수에 인수를 전달-> 함수이름("인수")
def func(a):
    print(a)

func("helle")

#하나의 문자열을 입력받아 뒤에 :D 이거 붙이시오
def print_smile(string):
    print(string+":D")
print_smile("안녕하세요")

# 세개의 수를 입력받아 가장 큰 값 출력 함수
# 삼항연산자를 사용
def max_val(a,b,c):
    max_v = a
    max_v = b if b > max_v else max_v
    max_v = c if c > max_v else max_v
    return max_v

# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을
# 화면에 출력하는 print_keys 함수를 정의하라.
def print_keys(dic):
    for i in dic.keys():
        print(i)

print_keys({"이름":"김말똥", "나이":30, "성별":0})

def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

# 함수 -> 지역 변수 (그안에서만 live)
def n_plus_1 (n) :
    return n + 1

print(n_plus_1(3))

# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는
# make_list 함수를 정의하라.
def make_list(string):
    return list(string)

print(make_list("abcd"))


