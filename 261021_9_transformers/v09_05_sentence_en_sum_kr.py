from transformers import pipeline

# 1. 요약 파이프라인
summarizer = pipeline("summarization", model="t5-small")

# 2. 요약할 원문 (영어 단락)
text = """
A special 25th anniversary edition of the extraordinary
international bestseller... Santiago's journey teaches us about
the essential wisdom of listening to our hearts...
"""

# 3. 요약 실행 (길이 옵션 지정)
# (왜) 기본값은 모델마다 다름 → 명시 지정해야 결과 길이 예측 가능
summary = summarizer(
    text,
    min_length=20,   # 최소 토큰 수 → 너무 짧은 요약 방지
    max_length=100,   # 최대 토큰 수 → 길이 폭주 방지
    do_sample=False  # 결정적(greedy) 생성 → 매번 동일 결과
)  # 반환: [{'summary_text': str}] 리스트

# 4. 결과 텍스트 추출 → 출력
sum_text = summary[0]['summary_text']  # 첫 결과의 'summary_text' 키 → 요약 문자열
print(f"요약된 문장 : {sum_text}")

# 5. 영어 요약 → 한국어 번역
# (왜) t5-small은 영어→한국어 번역을 학습하지 않음 → 다국어 번역 모델(NLLB) 사용
translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M",
    src_lang="eng_Latn",  # 원문 언어: 영어
    tgt_lang="kor_Hang"   # 번역 언어: 한국어
)
kr_text = translator(sum_text, max_length=200)[0]['translation_text']  # 반환: [{'translation_text': str}]
print(f"번역된 문장 : {kr_text}")
