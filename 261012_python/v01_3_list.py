colors = ["red", "green", "blue"]

# print(colors[0])    # red (첫번째)
# print(colors[-1])   # blue (마지막)
# print(colors[0:2])  # ['red', 'green'] (슬라이싱)

# colors[-1] = "black"        # 값 변경
# print(colors)                   # ['red', 'green', 'black']
# colors.append("pink")       # 끝에 추가
# print(colors)                   # ['red', 'green', 'black', 'pink']
# colors.insert(0, "white")   # 특정 위치에 삽입
# print(colors)                   # ['white', 'red', 'green', 'black', 'pink']
# colors.remove("white")      # 값으로 제거
# print(colors)                   # ['red', 'green', 'black', 'pink']

numbers = [8, 5, 3, 2, 7]
numbers.sort()              # 오름차순 정렬
print(numbers)                  # [2, 3, 5, 7, 8]
numbers.sort(reverse=True)  # 내림차순 정렬
print(numbers)                  # [8, 7, 5, 3, 2]
numbers.reverse()           # 순서 뒤집기
print(numbers)                  # [2, 3, 5, 7, 8]
print(2 in numbers)         # True (포함 여부)