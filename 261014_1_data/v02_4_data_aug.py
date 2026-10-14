import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = cv2.imread("puppy.jpg")

# 2. 이미지 증강
img_bright = cv2.convertScaleAbs(img, alpha=1, beta=50)
# alpha : 픽셀에 곱하는 값
# beta : 더할 밝기 (+50 = 밝게, -50 = 어둡게)

img_flip = cv2.flip(img, 1)
# 좌우반전 : 1
# 상하반전 : 0
# 상하좌우반전 : -1(또는 음수)

img_invert = cv2.bitwise_not(img)

#채도
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)
# h : 색상(Hue)       0~179
# s : 채도(Saturation) 0~255
# v : 명도(Value)      0~255

s_up = cv2.add(s, 80)   # 채도 +80 (255를 넘으면 255로 고정)
img_saturate = cv2.cvtColor(cv2.merge([h, s_up, v]), cv2.COLOR_HSV2BGR)

#색상 변경
h_shift = ((h.astype(np.int32) + 60) % 180).astype(np.uint8)   # 색상환을 60만큼 회전 (179를 넘으면 0부터 다시)
img_hue = cv2.cvtColor(cv2.merge([h_shift, s, v]), cv2.COLOR_HSV2BGR)


# 3. 이미지 시각화
fig, ax = plt.subplots(2,3, figsize=(15,7))

# 3-1 원본 이미지
ax[0,0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0,0].axis('off')
ax[0,0].set_title("Original")

# 3-2 밝기 이미지
ax[0,1].imshow(cv2.cvtColor(img_bright, cv2.COLOR_BGR2RGB))
ax[0,1].axis('off')
ax[0,1].set_title("Bright")

# 3-3 좌우반전 이미지
ax[0,2].imshow(cv2.cvtColor(img_flip, cv2.COLOR_BGR2RGB))
ax[0,2].axis('off')
ax[0,2].set_title("Flip")

# 3-4 색채반전 이미지
ax[1,0].imshow(cv2.cvtColor(img_invert, cv2.COLOR_BGR2RGB))
ax[1,0].axis('off')
ax[1,0].set_title("Inverted")

# 3-5 채도 증가 이미지
ax[1,1].imshow(cv2.cvtColor(img_saturate, cv2.COLOR_BGR2RGB))
ax[1,1].axis('off')
ax[1,1].set_title("Saturation")

# 3-6 색상 변경 이미지
ax[1,2].imshow(cv2.cvtColor(img_hue, cv2.COLOR_BGR2RGB))
ax[1,2].axis('off')
ax[1,2].set_title("Hue Shift")

# 4. 이미지 저장 (그림창을 닫기 전에 저장되도록 먼저 실행)
save_dir = "./augmented_images"
os.makedirs(save_dir, exist_ok=True)    # 폴더가 없으면 자동으로 생성

cv2.imwrite(os.path.join(save_dir, "bright_img.jpg"), img_bright)
cv2.imwrite(os.path.join(save_dir, "flip_img.jpg"), img_flip)
cv2.imwrite(os.path.join(save_dir, "invert_img.jpg"), img_invert)
cv2.imwrite(os.path.join(save_dir, "saturate_img.jpg"), img_saturate)
cv2.imwrite(os.path.join(save_dir, "hue_img.jpg"), img_hue)
print(f"증강 이미지가 저장되었습니다.: {save_dir}")

# 5. 그림창 띄우기
plt.show()
