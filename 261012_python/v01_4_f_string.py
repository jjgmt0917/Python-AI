name = "King"
age = 00

# # 기존 방식 (불편함)
# print("저는", name, "입니다. 나이는", age, "살입니다.")
# # 저는 King 입니다. 나이는 0 살입니다.

# # f-string 방식(권장)
# print(f"저는 {name}입니다. 나이는 {age}살입니다.")
# # 저는 King입니다. 나이는 0살입니다.

# 표현식
# a = 1
# b = 3
# print(f"{a} + {b} = {a + b}")
# print(f"소수점 2자리: {3.141419:.2f}")

# { } 자리에 순서대로 채움
print("저는 {}입니다. 나이는 {}입니다.".format(name, age))
# 저는 King입니다. 나이는 0입니다.