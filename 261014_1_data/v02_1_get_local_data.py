import cv2      # 카메라를 다루는 도구
import os       # 폴더를 만드는 도구
from datetime import datetime   # 지금 시간을 알려주는 도구

# [1단계] 사진을 저장할 폴더 준비
save_dir = "./captured_images"
os.makedirs(save_dir, exist_ok=True)    # 폴더가 없으면 자동으로 생성

# [2단계] 카메라를 켭니다 (0 = 내 컴퓨터의 첫 번째 카메라)
cap = cv2.VideoCapture(0)

#[3단계] 사진 한 장 찍음
success, frame = cap.read()     # success=True면 성공, frame=찍힌 이미지
if success:
    # 사진 파일명: 찍은 시간을 쓰면 여러 장을 찍어도 이름이 겹치지 않음
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")    # ex)20261014_095043
    file_path = os.path.join(save_dir, f"result_{timestamp}.jpg")
    
    # 파일로 저장
    cv2.imwrite(file_path, frame)
    print(f"사진이 저장되었습니다.: {file_path}")
    
else:
    print("카메라를 찾을 수 없습니다.")
    
# [4단계]  카메라를 끈다 (사용 후 반드시 해제)
cap.release()

# cv2.VideoCapture(0) — 카메라를 켜는 코드 (0은 내 컴퓨터의 첫 번째 카메라)
# cap.read() — 카메라에서 사진 한 장을 가져옴
# cv2.imwrite() — 사진을 파일로 저장