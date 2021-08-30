import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from PyAstronomy import pyasl
from sklearn import preprocessing
import statistics
cap = cv2.VideoCapture("Untitled.mp4")
mean = list()
tank=0

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
add=list()

flaggg=False

while (cap.isOpened()):
    _, frame = cap.read()
    if _==True:
        loop+=1
        
        if flag==True:
            try:
                os.remove("frame1.jpg")
            except:
                pass
            cv2.imwrite(os.path.join("frame1.jpg"), frame)
            gray_frame = cv2.imread("frame1.jpg", cv2.IMREAD_GRAYSCALE)

            flag=False
        else:
            try:
                os.remove("frame0.jpg")
            except:
                pass
            cv2.imwrite(os.path.join("frame0.jpg"),frame)
            first_gray = cv2.imread("frame0.jpg", cv2.IMREAD_GRAYSCALE)
            
            flag=True
            
        tank=0
        layer1=first_gray
        layer2=gray_frame
        temp=list()
        for p in range(0,4):
            b=list()
            h=layer1.shape[0]
            w=layer1.shape[1]
            for i in range(0, w):
                for j in range(0, h):
                    temp1=layer1[j,i]
                    temp2=layer2[j,i]
                    temp3=abs((int(temp2))-(int(temp1)))
                    b.append(temp3)
            temp.append(statistics.mean(b))
            tank+=statistics.mean(b)
            del b
            layer1=cv2.pyrDown(layer1)
            layer2=cv2.pyrDown(layer2)
        mean.append(temp)
        del temp
        add.append(tank)
    else:
        try:
            os.remove("frame0.jpg")
            os.remove("frame1.jpg")
        except:
            pass
        break
    

print(sum(mean[0]))
print(add[0])

m=max(add)
norm=[float(i)/m for i in add]

r = (pyasl.generalizedESD(norm, 1, 0.05, fullOutput=True))
print("Indices of outliers: ", r[1])
for i in range(r[0]):
    plt.plot(r[1][i], nmisum[r[1][i]], 'rp')

ranges=[i for i in range(0,loop)]
plt.bar(ranges, norm,color="blue")
plt.show()

cap.release()
cv2.destroyAllWindows()

