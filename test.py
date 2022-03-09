import cv2
import os
f=open("data.txt",'r',encoding='utf-8')
points0=[]
points1=[]
dic=[
    "nose",
    "l_ey_i",
    "l_ey",
    "l_ey_o",
    "r_ey_i",
    "r_ey",
    "r_ey_o",
    "l_er",
    "r_er",
    "mth_l",
    "mth_r",
    "l_sh",
    "r_sh",
    "l_ew",
    "r_ew",
    "l_ws",
    "r_ws",
    "left pinky",
    "right pinky",
    "left index",
    "right index",
    "left thumb",
    "right thumb",
    "left hip",
    "right hip",
    "left knee",
    "right knee",
    "left ankle",
    "right ankle",
    "left heel",
    "right heel",
    "left foot index",
    "right foot index",
]

for i,line in enumerate(f):
    if i==0 or i==34: continue
    line=line.strip()
    line=line.split(' ')
    if(float(line[2])<0.5): continue
    #print(i)
    if(i<34):
        points0.append((float(line[0]),float(line[1]),dic[i-1]))
        print(dic[i-1])
    else:
        points1.append((float(line[0]),float(line[1]),dic[i-35]))
        print(dic[i-35])
    

img0=cv2.imread('img0.jpg',1)
img1=cv2.imread('img1.jpg',1)

for i,point in enumerate(points0):
    cv2.circle(img0, (int(point[0]*640),int(point[1]*480)), 1, (0, 0, 255), 4)
    cv2.putText(img0, point[2], (int(point[0]*640),int(point[1]*480)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

for i,point in enumerate(points1):
    cv2.circle(img1, (int(point[0]*640),int(point[1]*480)), 1, (0, 0, 255), 4)
    cv2.putText(img1, point[2], (int(point[0]*640),int(point[1]*480)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

cv2.imshow("img0",img0)
cv2.imshow("img1",img1)
cv2.waitKey(0)


