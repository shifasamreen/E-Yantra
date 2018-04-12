import numpy as np
import cv2
img_rgb = cv2.imread('demo.jpg',0)
template=[ 0 for i in range(0,12) ]
w=[ 0 for i in range(0,12) ]
h=[ 0 for i in range(0,12) ]
m = 7
n = 7
grid_map = [ [ 0 for i in range(0,n-1) ] for j in range(0,m-1) ]
for i in range(0,10):
    imgpath='digits/'+str(i)+'.jpg'
    template[i]=cv2.imread(imgpath,0)
template[10]=cv2.imread('digits/minus.jpg',0)
template[11]=cv2.imread('digits/plus.jpg',0)
for i in range(0,12):
    w[i], h[i] = template[i].shape[::-1]
    res = cv2.matchTemplate(img_rgb,template[i],cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    threshold = max_val-0.001
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
	    m=(pt[1]/100)
	    n=(pt[0]/100)
	    if (grid_map[m][n]==0 or i==6) and (n==3 or n==4):
		    if i<10:
		        grid_map[m][n]=i
                    else:
                        if i==10:
                            grid_map[m][n]='-'
                        else:
                            grid_map[m][n]='+'
                            
print(grid_map)
