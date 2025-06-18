import cv2
a = cv2.QRCodeDetector()
retval, points, straight_qrcode = a.detectAndDecode(cv2.imread("C:\Users\ATHARVA\Desktop\new.jpg"))
print(retval)