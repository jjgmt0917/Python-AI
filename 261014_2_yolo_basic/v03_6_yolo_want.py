from ultralytics import YOLO

model = YOLO("yolo11n.pt")

model(
    "261014_2_yolo_basic/input_want.jpg",
    save=True,
    # conf=0.2,   # 신뢰도 20% 이상만 감지
    # max_det=1,  # 최대 탐지 개수 설정
    # save_crop=True, # 탐지 영역 이미지 저장
    # save_txt=True,   # 좌표 텍스트 저장
    classes=[55],
)

# cake만 탐지될 수 있도록 설정