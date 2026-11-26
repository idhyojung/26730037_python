# 리스트 + 연산 (리스트 + 리스트), 중복허용
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2

print(langs)

# 최대값 -> max(), 최소값 -> min(), 개수 -> len()

nums = [1, 2, 3, 4, 5, 6, 7]
print("최대값 :", max(nums), "최소값 :", min(nums), "개수 :", len(nums))
# 리스트 합 -> sum()
print("리스트 요소의 합 :", sum(nums))

#리스트 중복을 허용<-> set()
#중복된 데이터는 한번만 표시하세요
lang1 = [1,2,3,4]
lang2 = [1,2,3]
langs = set(lang1+lang2)
print(*langs)
