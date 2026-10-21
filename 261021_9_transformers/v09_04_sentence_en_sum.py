from transformers import pipeline
# pip install transformers==5.20.2
# 버전 문제로 안됨 
# pip uninstall transformers
# 다운그레이드
# pip install transformers==4.46.3

# 1. 요약 파이프라인
summarizer = pipeline("summarization", model="t5-small")

# 2. 요약할 원문 (영어 단락)
text = """
The Netherlands — The position of NATO Secretary General is a curious one. On paper, you’re leading the most powerful military alliance in history. In reality, you’re the errand boy of the President of the United States, by far the most powerful member of NATO. It’s no coincidence that the secretaries general are usually politicians from smaller member states. Picture a former French president in such a subservient role.
Former Dutch Prime Minister Mark Rutte wears it easily; in fact, he seems to revel in his role. After Trump dropped bunker busters on Iran, Rutte texted him about this « extraordinary action ». When NATO members seemed to agree on a five percent defense spending target, Rutte texted: « yet another big success ». Trump eagerly shared that private message on his Truth Social network, which would have embarrassed most people — but Rutte?
Were Rutte’s words befitting the Secretary General of NATO, at a moment when the radical-right Trump was subjecting one NATO ally after another to the whims of his tariff policy and putting pressure on democracy at home? At the conference, Rutte went even further by calling Trump « Daddy ». The criticism grew louder: Whose side was Rutte really on?
"""

# 3. 요약 실행 (길이 옵션 지정)
# (왜) 기본값은 모델마다 다름 → 명시 지정해야 결과 길이 예측 가능
summary = summarizer(
    text,
    min_length=20,   # 최소 토큰 수 → 너무 짧은 요약 방지
    max_length=100,   # 최대 토큰 수 → 길이 폭주 방지
    do_sample=False  # 결정적(greedy) 생성 → 매번 동일 결과
)  # 반환: [{'summary_text': str}] 리스트pd

# 4. 결과 텍스트 추출 → 출력
sum_text = summary[0]['summary_text']  # 첫 결과의 'summary_text' 키 → 요약 문자열
print(f"요약된 문장 : {sum_text}")

# 요약된 문장 : former french president wears it easily; in fact, he seems to revel in his role . after Trump dropped bunker busters on Iran, Rutte texted him about this "extraordinary action"