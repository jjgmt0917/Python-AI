from ultralytics import YOLO
import cv2
# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 추론
results = model("261014_2_yolo_basic/input_video.mp4")

# 3. 결과 시각화
results_image = results[0].plot()

# 4. 결과 이미지 저장
cv2.imwrite("261014_2_yolo_basic/output_video_n.mp4", results_image)

print("결과 이미지 잘 저장 되었습니다.")