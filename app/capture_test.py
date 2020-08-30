import numpy as np 
from PIL import ImageGrab 
import time 
import cv2 
from direct_keys import PressKey, ReleaseKey, W, A, S, D 

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 3)
    except:
        pass
def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1 = 100 , threshold2 = 200)
    processed_img = cv2.GaussianBlur(processed_img, (5,5), 0)
    vertices = np.array([[10, 500], [10, 300], [300, 200], [500,200], [800,300], [800,500]])
    processed_img = roi(processed_img,[vertices]) 
    # processed_img is edges
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 20, 15)
    draw_lines(processed_img, lines)
    return processed_img



while(True):

    screen = ImageGrab.grab(bbox = (0, 40, 800, 640))
    
    new_screen = process_img(np.array(screen))
    
    
    cv2.imshow('window', new_screen)
    # cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB ))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows() 
        break

