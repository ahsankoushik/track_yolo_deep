import cv2


img = cv2.imread("/home/koushik/Pictures/Screenshot_20231028_195627.png")

img = cv2.resize(img,(400,800))

cv2.imshow("test",img)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()