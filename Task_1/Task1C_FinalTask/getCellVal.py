# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task1C
*  Filename: getCellVal.py
*  Version: 1.0.0  
*  Date: October 13, 2016
*  
*  Author: Jayant Solanki, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
"""
# detectCellVal detects the numbers/operatorsm,
# perform respective expression evaluation
# and stores them into the grid_map 
# detectCellVal(img,grid_map)

# Find the number/operators, perform the calculations and store the result into the grid_map
# Return the resultant grid_map
import cv2
import numpy as np
# comment here
def detectCellVal(img_rgb,grid_map):
	#your code here
        template=[ 0 for i in range(0,12) ]
        w=[ 0 for i in range(0,12) ]
        h=[ 0 for i in range(0,12) ]
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
                        if grid_map[m][n]==-1 or i==4:
                                if i<10:
                                        grid_map[m][n]=i
                                else:
                                        if i==10:
                                                grid_map[m][n]='-'
                                        else:
                                                grid_map[m][n]='+'
        
        for i in range(0,6):
                if(grid_map[i][1]=='-'):
                        c=grid_map[i][0]-grid_map[i][2]
                else:
                        c=grid_map[i][0]+grid_map[i][2]
                if(grid_map[i][3]=='-'):
                        c=c-grid_map[i][4]
                else:
                        c=c+grid_map[i][4]
                grid_map[i][5]=c
       
                        
                
                        
                
	return grid_map
