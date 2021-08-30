import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from PyAstronomy import pyasl
from tkinter import ttk


def dif(p):
	# print(pp)
	# pp.start()
	cap = cv2.VideoCapture(p)
	mean = list()

	flag=True
	_, first_frame = cap.read()

	count=0
	cv2.imwrite(os.path.join("frame0.jpg"), first_frame)

	first_gray = cv2.imread("frame0.jpg", cv2.IMREAD_GRAYSCALE)

	h=height = first_gray.shape[0]
	w=width = first_gray.shape[1]
	count=h*w

	loop=0
	k=list()

	flaggg=False

	while (cap.isOpened()):
	    b=list()
	    _, frame = cap.read()
	    if _==True:
	        loop+=1
	        if flag==True:
	            try:
	                os.q("frame1.jpg")
	            except:
	                pass
	            cv2.imwrite(os.path.join("frame1.jpg"), frame)
	            gray_frame = cv2.imread("frame1.jpg", cv2.IMREAD_GRAYSCALE)

	            for i in range(0, w):
	                for j in range(0, h):
	                    temp1=first_gray[j,i]
	                    temp2=gray_frame[j,i]
	                    temp3=abs((int(temp2))-(int(temp1)))
	                    b.append(temp3)
	         
	            k.append(b)
	            del b
	            flag=False
	        else:
	            try:
	                os.remove("frame0.jpg")
	            except:
	                pass
	            cv2.imwrite(os.path.join("frame0.jpg"),frame)
	            first_gray = cv2.imread("frame0.jpg", cv2.IMREAD_GRAYSCALE)
	            
	            for i in range(0, w):
	                for j in range(0, h):
	                    temp1=first_gray[j,i]
	                    temp2=gray_frame[j,i]
	                    temp3=abs((int(temp2))-(int(temp1)))
	                    b.append(temp3)

	            k.append(b)
	            del b
	            flag=True
	    else:
	        try:
	            os.remove("frame0.jpg")
	            os.remove("frame1.jpg")
	        except:
	            pass
	        break

	for i in range(0,loop):
	    mean.append(sum(k[i])/count)

	m=max(mean)
	norm=[float(i)/m for i in mean]
	
	r = (pyasl.generalizedESD(norm, 1, 0.05, fullOutput=True))
	# print("Indices of outliers: ", r[1])
	# print(r)

	ranges=[i for i in range(0,loop)]
	# plt.bar(ranges, mean,color="blue")
	# plt.show()

	cap.release()
	# pp.stop()
	# cv2.destroyAllWindows()
	return (r, mean, ranges)




def optical(q):
	import cv2
	import numpy as np
	import os
	import matplotlib.pyplot as plt
	from PyAstronomy import pyasl
	from sklearn import preprocessing
	cap = cv2.VideoCapture(q)
	mean = list()

	flag=True

	_, first_frame = cap.read()
	prvs = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)

	hsv = np.zeros_like(first_frame)
	hsv[...,1] = 255

	ret, frame1 = cap.read()
	next = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)


	flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
	mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
	hsv[...,0] = ang*180/np.pi/2
	hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)

	rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
	cv2.imwrite(os.path.join("frame0.jpg"), rgb)
	rgb = cv2.imread("frame0.jpg", cv2.IMREAD_GRAYSCALE)


	count=0

	h=height = rgb.shape[0]
	w=width = rgb.shape[1]
	count=h*w

	loop=0
	k=list()

	flaggg=False

	while (cap.isOpened()):
	    b=list()
	    _, frame = cap.read()
	    if _==True:
	        loop+=1
	        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	        if flag==True:
	            try:
	                os.remove("frame1.jpg")
	            except:
	                pass
	            
	            prvs=frame
	            
	            flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
	            mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
	            hsv[...,0] = ang*180/np.pi/2
	            hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)

	            rgb1 = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
	            cv2.imwrite(os.path.join("frame1.jpg"), rgb1)
	            rgb1 = cv2.imread("frame1.jpg", cv2.IMREAD_GRAYSCALE)
	            
	            for i in range(0, w):
	                for j in range(0, h):
	                    temp1=rgb[j,i]
	                    temp2=rgb1[j,i]
	                    temp3=abs((int(temp2))-(int(temp1)))
	                    b.append(temp3)
	         
	            k.append(b)
	            del b
	            flag=False
	        else:
	            try:
	                os.remove("frame0.jpg")
	            except:
	                pass

	            next=frame
	            
	            flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
	            mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
	            hsv[...,0] = ang*180/np.pi/2
	            hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)

	            rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
	            cv2.imwrite(os.path.join("frame0.jpg"), rgb)
	            rgb = cv2.imread("frame0.jpg", cv2.IMREAD_GRAYSCALE)
	            
	            for i in range(0, w):
	                for j in range(0, h):
	                    temp1=rgb[j,i]
	                    temp2=rgb1[j,i]
	                    temp3=abs((int(temp2))-(int(temp1)))
	                    b.append(temp3)

	            k.append(b)
	            del b
	            flag=True
	    else:
	        try:
	            os.remove("frame0.jpg")
	            os.remove("frame1.jpg")
	        except:
	            pass
	        break

	for i in range(0,loop):
	    mean.append(sum(k[i])/count)
	    
	m=max(mean)
	norm=[float(i)/m for i in mean]

	r = (pyasl.generalizedESD(norm, 1, 0.05, fullOutput=True))
	# print("Indices of outliers: ", r[1])

	ranges=[i for i in range(0,loop)]
	# plt.bar(ranges, norm,color="blue")
	# plt.show()

	cap.release()
	# cv2.destroyAllWindows()

	return (r, norm, ranges)
