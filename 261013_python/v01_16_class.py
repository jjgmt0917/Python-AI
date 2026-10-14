# class Dog:                          # 클래스 정의 — 강아지 설계도(틀)
#     def __init__(self, name, age):  # 생성자 — 객체 생성 시 자동 실행
#         self.name = name            # 속성 name 저장
#         self.age = age              # 속성 age 저장

#     def bark(self):                 # 메서드 정의 — 짖기
#         print(f"{self.name}: 멍멍!")

# # 객체 생성 — 같은 틀로 강아지 두 마리 만들기
# dog1 = Dog("뽀삐", 3)
# dog2 = Dog("초코", 5)

# dog1.bark()       # 메서드 호출 — 뽀삐: 멍멍!
# dog2.bark()       # 메서드 호출 — 초코: 멍멍!
# print(dog2.age)   # 속성 접근 — 5

# 강아지 1
dog1_name = "뽀삐"      # 객체 1의 정보가
dog1_age = 3            # 따로따로 변수로 흩어짐

# 강아지 2
dog2_name = "초코"
dog2_age = 5

def bark(name):         # 짖기는 외부 함수 (매번 이름을 받아야 함)
    print(f"{name}: 멍멍!")

bark(dog1_name)         # 뽀삐: 멍멍!
bark(dog2_name)         # 초코: 멍멍!
print(dog2_age)         # 5

# 클래스를 쓰는 이유:
#	불편	이유
# 1	변수 폭발	강아지마다 따로 — 100마리면 200개, 1000마리면 2000개
# 2	묶음 표시 없음	dog1의 name·age가 한 통인지 접두어로만 짐작
# 3	이름을 매번 전달	bark(dog1_name) — dog1.bark() 처럼 자기 행동이 안 됨
# 4	속성 추가가 번거로움	새 속성(예: 색깔)을 모든 강아지 변수에 일일이 추가
# 5	추적 어려움	함수(bark)와 데이터(dog1_name)가 분리 — 길어지면 연결 파악 곤란
# 클래스는 이 모든 불편을 한 번에 해결 — 정보(속성)와 행동(메서드)을 한 통(설계도)에 묶어 두니, 1마리든 1000마리든 같은 틀로 깔끔하게 관리