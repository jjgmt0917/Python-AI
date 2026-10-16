from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. CCTV 스트림 주소
stream_url = "https://cctvsec.ktict.co.kr/6572/G4K8/J1Z+jkF45854aYp6abEDLk5tLb0gIfYiF67bccDCzlO5B8Pw7bnJaNJhpaQ"
cap = cv2.VideoCapture(stream_url)

# 3. 실시간 프레임 처리
while cap.isOpened():  # 스트림이 정상 열려있는 동안 반복
    success, frame = cap.read()
    if not success:
        print("CCTV URL 또는 웹캠을 확인해주세요.")
        break
    
    # 스트림 잘 읽어왔을 때 처리
    # 3-1. 모델 추론
    results = model(frame, conf=0.5)
    
    # 3-2. 탐지 결과가 그려진 프레임 얻기
    annotated_frame = results[0].plot()
    
    # 3-3. 윈도우 창 그리기
    cv2.imshow("CCTV_YOLO", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료")
        break
    
# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()