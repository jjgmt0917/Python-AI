import cv2      # 카메라를 다루는 도구
import os       # 폴더를 만드는 도구
from datetime import datetime   # 지금 시간을 알려주는 도구
import schedule

# 사진 캡쳐 간격 설정
interval_time = 5

def capture_image():
    save_dir = "./captured_images"
    os.makedirs(save_dir, exist_ok=True)    # 폴더가 없으면 자동으로 생성

    cap = cv2.VideoCapture(0)
    
    success, frame = cap.read()     # success=True면 성공, frame=찍힌 이미지
    
    if success:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")    # ex)20261014_095043
        file_path = os.path.join(save_dir, f"result_{timestamp}.jpg")
        
        cv2.imwrite(file_path, frame)
        print(f"사진이 저장되었습니다.: {file_path}")
        
    else:
        print("카메라를 찾을 수 없습니다.")
        
    cap.release()
    
# 스케줄의 설정
schedule.every(interval_time).seconds.do(capture_image)

while True:
    schedule.run_pending()  # 예약된 작업 실행
