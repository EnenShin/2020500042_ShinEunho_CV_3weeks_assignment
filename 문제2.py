import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img_file = "img/Lenna.png" # 표시할 이미지 경로 ---①
    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE) # 회색으로 읽기
    img_color = cv2.imread(img_file, cv2.IMREAD_COLOR) # 컬러영상 읽기
    plt.subplot(2, 2, 1)
    plt.imshow(img)
    plt.subplot(2, 2, 2)
    plt.imshow(img_color)

if img is not None:
    plt.subplot(2, 2, 3)
    plt.imshow(img, cmap='gray')
    #plt.show()

    img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
    plt.subplot(2, 2, 4)
    plt.imshow(img_rgb)
    plt.show()
else:
    print('No image file.')