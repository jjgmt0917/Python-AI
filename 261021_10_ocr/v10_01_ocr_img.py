import pytesseract  # OCR 사용
from PIL import Image   # 이미지 처리 도구
import os

# 1. Tesseract 실행 파일 경로 지정
pytesseract.pytesseract.tesseract_cmd = "c:/Program Files/Tesseract-OCR/tesseract.exe"

# 2. 이미지 불러오기
# mage = Image.open("261021_10_ocr/input.jpg")
image = Image.open("261021_10_ocr/input_kr.jpg")

# 3. OCR 수행
results = pytesseract.image_to_string(
    image,
    lang="eng+kor", # 영어는 eng
)

# 4. 결과 출력
print(f"OCR 실행 결과: {results}")

# OCR 실행 결과: LARANASKIN

# 이수진

# 팀장 / 제 품 개발팀

# +123-456-7890
# hello@reallygreatsite.com
# 123 Anywhere St., Any City, ST 12345


## 1. 번호판 이미지 인식
## 2. 다른 OCR과 비교