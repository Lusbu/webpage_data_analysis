import cv2
img = cv2.imread("/Users/lilus/Pictures/WechatIMG19811.jpeg")
if img is None:
    print("Image read Error!")
else:
    cv2.imshow("Hello, Python OpenCV",img);
    cv2.waitKey(0);
    cv2.destroyAllWindows();