from transformers import pipeline

# 1. 감정 분석 파이프라인 생성
# (왜) 기본 모델은 영어 전용 → 한국어 감정(11가지)으로 학습된 KcELECTRA 모델 지정
classifiier = pipeline("sentiment-analysis", model="nlp04/korean_sentiment_analysis_kcelectra")

# 2. 분석 문장 입력
# 2-1 긍정 문장
# text = "오늘 날씨가 너무 좋아"
# 2-2 부정 문
# text = "그 광경이 굉장히 찝찝했어"
# 2-3 부정 단어
text = "죽음"
# 3. 문장 분석
results = classifiier(text)

# 4. 결과 확인
# 이 모델은 긍정/부정이 아니라 11가지 감정 중 하나로 나옴
# 기쁨(행복한), 고마운, 설레는(기대하는), 사랑하는, 즐거운(신나는), 일상적인,
# 생각이 많은, 슬픔(우울한), 힘듦(지침), 짜증남, 걱정스러운(불안한)
print(f"감정 분석 결과 : {results[0]['label']}")
# 1에 가까울 수록 확신도가 높음
print(f"감정 분석 점수 : {results[0]['score']:.4f}")

# text = "오늘 날씨가 너무 좋아"
# 감정 분석 결과 : 기쁨(행복한)
# 감정 분석 점수 : 0.6940

# text = "마음이 너무 무거워."
# 감정 분석 결과 : 슬픔(우울한)
# 감정 분석 점수 : 0.9880

# text = "죽음"
# 감정 분석 결과 : 슬픔(우울한)
# 감정 분석 점수 : 0.6340


# ============================================================
# 한국어 감정 분석 모델 비교 (같은 단어·문장 7개로 테스트)
# 부정 4개: "눈물", "죽음", "마음이 너무 무거워.", "오늘따라 그녀가 너무 조용한것같아."
# 긍정 3개: "행복", "오늘 날씨가 너무 좋아", "사랑"
# ※ 샘플이 7개뿐이라 순위 확정이 아니라 경향 파악용
# ============================================================
#
# [1] nlp04/korean_sentiment_analysis_kcelectra   → 7/7 (최종 선택)
#     라벨: 11가지 감정 (기쁨, 고마운, 설레는, 사랑하는, 즐거운, 일상적인,
#           생각이 많은, 슬픔, 힘듦, 짜증남, 걱정스러운)
#     눈물 -> 슬픔(우울한) (0.687) / 죽음 -> 슬픔(우울한) (0.634)
#     마음이 너무 무거워. -> 슬픔(우울한) (0.988)
#     오늘따라 그녀가 너무 조용한것같아. -> 슬픔(우울한) (0.948)
#     행복 -> 기쁨(행복한) (0.796) / 오늘 날씨가 너무 좋아 -> 기쁨(행복한) (0.694)
#     사랑 -> 기쁨(행복한) (0.619)
#
# [2] cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual   → 6/7
#     라벨: negative / neutral / positive
#     눈물 -> negative (0.606) / 죽음 -> negative (0.667)
#     마음이 너무 무거워. -> negative (0.919)
#     오늘따라 그녀가 너무 조용한것같아. -> positive (0.473)  ← 틀림
#     행복 -> positive (0.579) / 오늘 날씨가 너무 좋아 -> positive (0.975)
#     사랑 -> positive (0.523)
#
# [3] WhitePeak/bert-base-cased-Korean-sentiment   → 5/7
#     라벨: LABEL_0(부정) / LABEL_1(긍정)
#     눈물 -> LABEL_0 (0.922) / 죽음 -> LABEL_0 (0.992)
#     마음이 너무 무거워. -> LABEL_0 (0.987)
#     오늘따라 그녀가 너무 조용한것같아. -> LABEL_1 (0.951)  ← 틀림
#     행복 -> LABEL_1 (0.691) / 오늘 날씨가 너무 좋아 -> LABEL_1 (0.980)
#     사랑 -> LABEL_0 (0.632)  ← 틀림
#
# [4] tabularisai/multilingual-sentiment-analysis   → 5/7
#     라벨: Very Negative / Negative / Neutral / Positive / Very Positive
#     눈물 -> Neutral (0.353)  ← 애매 / 죽음 -> Very Negative (0.746)
#     마음이 너무 무거워. -> Negative (0.504)
#     오늘따라 그녀가 너무 조용한것같아. -> Positive (0.586)  ← 틀림
#     행복 -> Positive (0.406) / 오늘 날씨가 너무 좋아 -> Positive (0.528)
#     사랑 -> Positive (0.566)
#
# [5] circulus/koelectra-sentiment-v1   → 3/7 (사용 불가)
#     라벨: LABEL_0 / LABEL_1
#     입력과 상관없이 7개 전부 LABEL_1 (눈물 0.978, 죽음 0.578, 행복 0.952 ...)
#
# [6] Copycats/koelectra-base-v3-generalized-sentiment-analysis   → 3/7 (사용 불가)
#     라벨: 0 / 1
#     입력과 상관없이 7개 전부 1 (눈물 0.921, 죽음 0.579, 행복 0.933 ...)
#
# [7] matthewburke/korean_sentiment   → 3/7 (사용 불가, 처음 쓰던 모델)
#     라벨: LABEL_0 / LABEL_1
#     입력과 상관없이 7개 전부 LABEL_1 (눈물 0.960, 죽음 0.605, 행복 0.951 ...)
#     영화 리뷰(NSMC)로만 학습 → 단어/일상 감정 표현에 약함
#
# [8] nlpmhp/korean_sentiment_classification   → 3/7 (사용 불가)
#     라벨: 0 / 1
#     입력과 상관없이 7개 전부 1 (눈물 0.921, 죽음 0.579, 행복 0.933 ...)
#
# [9] Chamsol/koelctra-sentiment-classification   → 3/7 (사용 불가)
#     라벨: LABEL_0 ~ LABEL_3 (4분류)
#     입력과 상관없이 7개 전부 LABEL_1 (눈물 0.939, 죽음 0.673, 행복 0.929 ...)
#
# [10] withU/Koelectra-five-sentiment-classification   → 로드 실패
#     AutoModelForSequenceClassification으로 모델을 불러오지 못함
#
# [11] matthewlee85/ko-sentiment-classification   → 확인 불가
#     Hugging Face에서 찾을 수 없음 (없거나 비공개)
#
# 결론: 긍정/부정만 필요하면 [2] cardiffnlp, 감정 종류까지 필요하면 [1] nlp04 사용
# ※ 토크나이저는 정상(한국어 정상 분리) → 3/7 모델들은 모델 자체 문제로 판단