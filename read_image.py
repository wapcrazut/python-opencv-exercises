import cv2

img = cv2.imread('input/lena.jpg', 0)
print(img)
cv2.imshow('test', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('output/lena_copy.png', img)
    cv2.destroyAllWindows()
