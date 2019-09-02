import cv2
import numpy as np

#img = cv2.imread('input/lena.jpg', 1)  # Load image
img = np.zeros([512, 512, 3], np.uint8)  # Create new image

# Draw!
img = cv2.line(img, (0, 0), (255, 255), (255, 255, 0), 5)  # Simple line
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 255, 0), 5)  # Arrow line
img = cv2.rectangle(img, (255, 255), (300, 300), (255, 0, 0), 10)  # Line rectangle
img = cv2.rectangle(img, (255, 255), (300, 300), (255, 0, 0), -1)  # Filled rectangle
img = cv2.circle(img, (60, 150), 60, (255, 0, 0), 5)  # Outline Circle
img = cv2.circle(img, (150, 150), 60, (255, 0, 0), -1)  # Filled Circle

font = cv2.FONT_HERSHEY_SIMPLEX  # Font type
img = cv2.putText(img, "OpenCV", (20, 400), font, 4, (255, 255, 255), 10, cv2.LINE_8)  # Draw text at bottom

# Show it to me!
cv2.imshow('test', img)
cv2.waitKey(0)

# Done
cv2.destroyAllWindows()