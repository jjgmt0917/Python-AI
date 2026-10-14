# "w" 는 같은 파일이 이미 있으면 기존 내용을 통째로 덮어쓴다. 없으면 새로 만든다.
# with open("memo.txt", "w", encoding="utf-8") as f:
#     f.write("안녕, 파이썬!\n")
#     f.write("with문이 자동으로 닫아줌\n")
# 블록을 빠져나오면 파일은 알아서 닫힘

# 방금 쓴 memo.txt를 통째로 읽어 화면에 출력 — read()는 전체 한 번에, readlines()는 줄 단위 리스트로 받기
# with open("memo.txt", "r", encoding="utf-8") as f:
#     text = f.read()
# print(text)
# 출력:
# 안녕, 파이썬!
# with문이 자동으로 닫아줌

with open("memo.txt", "a", encoding="utf-8") as f:
    f.write("새로운 한 줄 추가\n")
# 기존 내용은 그대로, 끝에만 한 줄이 더 붙음