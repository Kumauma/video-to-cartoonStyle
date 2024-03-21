import cv2 as cv
import numpy as np


# 만화 스타일을 위한 함수
def img_to_Cartoon(image):
    # Bilateral Filter
    image_Cartoon = cv.bilateralFilter(image, d=9, sigmaColor=150, sigmaSpace=2.4)

    # Canny Edge Detector
    # 이미지를 그레이스케일로 변환
    gray = cv.cvtColor(image_Cartoon, cv.COLOR_BGR2GRAY)
    # Canny 엣지 검출
    edges = cv.Canny(gray, threshold1=500, threshold2=1200, apertureSize=5)
    # 팽창을 위한 커널 정의
    kernel = np.ones((2, 2), np.uint8)
    # 팽창 적용
    edges_dilated = cv.dilate(edges, kernel, iterations=1)
    # 가장자리 이미지를 반전시켜 검은색 가장자리 얻음.
    edges_inv = cv.bitwise_not(edges_dilated)
    # 가장자리 반전 이미지를 컬러 이미지로 변환하여 채널 수 맞춤.
    edges_inv_colored = cv.cvtColor(edges_inv, cv.COLOR_GRAY2BGR)
    # 이미지에 가장자리 추가
    # 여기서는 비트와이즈 연산을 사용하여 검은색 가장자리를 유지하면서 원본 이미지에 추가
    image_Cartoon = cv.bitwise_and(image_Cartoon, edges_inv_colored)

    # K-Means Clustering
    # 이미지를 float32 자료형으로 변환하고 2차원 배열로 재구성
    Z = image_Cartoon.reshape((-1, 3))
    Z = np.float32(Z)
    # k-평균 알고리즘 적용
    # k는 사용자가 정하는 대표 색상의 수
    k = 8
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv.kmeans(Z, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    # 대표 색상으로 이미지 재구성
    res = center[label.flatten()]
    image_Cartoon = res.reshape((image_Cartoon.shape))

    return image_Cartoon


# 만화 스타일이 아니기 위한 함수
def img_to_notCartoon(image):
    # Gaussian Blur
    # 이미지에 가우시안 블러 적용
    img_notCartoon = cv.GaussianBlur(image, (3, 3), 0)

    # Unsharp Masking
    # 원본 이미지와 블러 처리된 이미지의 차이 계산
    img_notCartoon = cv.addWeighted(img, 1.5, img_notCartoon, -0.5, 0)

    # CLAHE
    # 이미지를 LAB 컬러 스페이스로 변환
    lab = cv.cvtColor(img_notCartoon, cv.COLOR_BGR2LAB)
    l, a, b = cv.split(lab)
    # L 채널에 CLAHE 적용
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l_clahe = clahe.apply(l)
    # 수정된 L 채널을 다시 LAB 이미지와 결합
    lab_clahe = cv.merge((l_clahe, a, b))
    # LAB 컬러 스페이스에서 BGR로 이미지 변환
    img_notCartoon = cv.cvtColor(lab_clahe, cv.COLOR_LAB2BGR)

    return img_notCartoon


# 비디오 파일 이름
video_file = "your_video_path.mp4"

target_format = "mp4"
target_fourcc = "DIVX"

# 비디오를 읽어옴
video = cv.VideoCapture(video_file)
assert video.isOpened(), "Cannot read the given video, " + video_file

# 파라미터 설정
target1 = cv.VideoWriter()
target2 = cv.VideoWriter()

while True:
    # 'video'에서 이미지를 읽어옴
    valid, img = video.read()
    if not valid:
        break
    img_Cartoon = img_to_Cartoon(img)
    img_notCartoon = img_to_notCartoon(img)

    if not target1.isOpened():
        # 타깃 비디오 파일 열기
        target_file1 = video_file[: video_file.rfind(".")] + "_Cartoon." + target_format
        fps = video.get(cv.CAP_PROP_FPS)
        h, w, *_ = img.shape
        is_color = (img.ndim > 2) and (img.shape[2] > 1)
        target1.open(
            target_file1,
            cv.VideoWriter_fourcc(*target_fourcc),
            fps,
            (w, h),
            is_color,
        )
    if not target2.isOpened():
        # 타깃 비디오 파일 열기
        target_file2 = (
            video_file[: video_file.rfind(".")] + "_notCartoon." + target_format
        )
        target2.open(
            target_file2,
            cv.VideoWriter_fourcc(*target_fourcc),
            fps,
            (w, h),
            is_color,
        )

    # 'target'에 이미지를 쓰기
    target1.write(img_Cartoon)
    target2.write(img_notCartoon)

target1.release()
target2.release()

cv.destroyAllWindows()
