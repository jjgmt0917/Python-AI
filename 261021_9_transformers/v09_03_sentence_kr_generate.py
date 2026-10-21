from transformers import pipeline

# 1. 텍스트 새성 파이프 라인 생성
generator = pipeline("text-generation", model="gpt2") # 최초 1회 모델 다운로드 필요

# 2. 시드 문장 입력 (이어 쓸 첫 부분)
q = input("이어서 쓸 첫 문장을 입력해 주세요: ")

# 3. 텍스트 생성 실행
result = generator(
    q,
    max_new_tokens=50,  # 추가 생성할 토큰 수 (길수록 추론 시간도 길어짐)
    num_return_sequences=1, # 반환 문장 1개로 설정
)

# 4. 결과 출력
print(result[0]["generated_text"])

# 이어서 쓸 첫 문장을 입력해 주세요: it's very wet.
# it's very wet. It's all of you."

# "Alright, I'll give you that."