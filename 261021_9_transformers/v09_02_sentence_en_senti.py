from transformers import pipeline

# 1. 감정 분석 파이프라인 생성
classifiier = pipeline("sentiment-analysis")

# 2. 분석 문장 입력
# 2-1 긍정 문장
# text = "i'm feeling really great today"
# 2-2 부정 문
# text = "She is not happy today"
# 2-3 부정 단어
text = "angry"
# 3. 문장 분석
results = classifiier(text)

# 4. 결과 확인
# POSITIVE OR NEGATIVE 둘중 하나로 나옴
print(f"감정 분석 결과 : {results[0]['label']}")
# 1에 가까울 수록 확신도가 높음
print(f"감정 분석 점수 : {results[0]['score']:.4f}")

# text = "i'm feeling really great today"
# 감정 분석 결과 : POSITIVE
# 감정 분석 점수 : 0.9999

# text = "She is not happy today"
# 감정 분석 결과 : NEGATIVE
# 감정 분석 점수 : 0.9997