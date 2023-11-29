import numpy as np
import pandas as pd
import serial
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import cv2


def pos_angel(base_angel,length):
    pt1 = (hight // 2 + int(length * np.sin(np.radians(base_angel))), width + int(length * np.cos(np.radians(base_angel)))) #((width*np.cos(np.radians(base_angel))),(width*np.sin(np.radians(base_angel))))
    return pt1
def put_degree(txt,shift=0,level=0,txt_shift=0,txt_level=0):
    cv2.putText(img, txt, org=pos_angel(int(txt) + 90+txt_shift, 353+txt_level), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5,
                color=(0, 255, 0), thickness=1)  # ,fontFace=cv2.LINE_AA)
    cv2.circle(img, center=pos_angel(int(txt) + 90+shift, 378+level), radius=2, color=(0, 255, 0))


width = 720
hight = 1080
radius = 60
img = np.zeros((width,hight,3))
# cv2.circle(img,(640//2,400+(radius//2)),radius,color=[0,255,0],thickness=3)
for base_angel in range(90,300,30):
    pt1 = (hight // 2 + int(350 * np.sin(np.radians(base_angel))), width + int(350 * np.cos(np.radians(base_angel)))) #((width*np.cos(np.radians(base_angel))),(width*np.sin(np.radians(base_angel))))
    cv2.line(img,pt1=pt1,pt2=(hight//2,width),color=[0,255,0],thickness=2)

for i in range(1,320,78):
    cv2.circle(img,(hight//2,width),i,color=[0,255,0])


put_degree('30')
put_degree('60',-2,-2)
put_degree('90',-4,-13)
put_degree('120',-3.5,-18,2,15)
put_degree('150',-2,-20,2,28)
for n,i in enumerate(range(0,300,78)):
    cv2.putText(img,f'{10*(n+1)}cm',org=pos_angel(90 , 50+i), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5,color=(0, 255, 0), thickness=1)
cv2.imwrite('radar.jpg',img)
new_img = cv2.imread('radar.jpg')
new_img = img
ser = serial.Serial(port='COM26',baudrate=9600)
targets = []
instances = []
features = []
entered_key = -1
counter = 0
num_classes = 2
num_samples = 150
prev_class=0
while counter <= (180*num_samples*num_classes):
    clas = counter//(180*num_samples)
    cv2.putText(img, f"{(counter//180)%num_samples} counts in Class no: {clas} ", org=(320, 320),
                fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0), thickness=2)

    try:
        data = ser.readline().decode().split()[0].split(',')
        distance, angle = int(data[0]) , int(data[1])+90
        distance = 50 if int(data[0]) == 0 or int(data[0]) > 200 else distance
        print(distance, angle)
        if angle == 90:
            img=cv2.imread('radar.jpg')
            if len(instances) >1:
                if np.sum(instances) == 0 :
                    counter -= 180
                else:
                    # print(instances,'\n====================================\n',instances[::int(np.tanh(180-angle))])
                    features.append(instances.copy())
                instances.clear()
                if clas != prev_class:
                    for i in range(5):
                        img = cv2.imread('radar.jpg')
                        cv2.imshow('m', img)
                        cv2.waitKey(100)
                        cv2.putText(img, f"Change to the next class!!", org=(320, 320),
                                    fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0), thickness=2)
                        cv2.imshow('m', img)
                        cv2.waitKey(100)
                    img = cv2.imread('radar.jpg')
                prev_class = clas
        if distance < 40:
            instances.append(distance)
            distance = np.interp(distance,[0,40],[0,350])
            pt1 = (hight // 2 + int(distance * np.sin(np.radians(angle))), width + int(distance * np.cos(np.radians(angle))))
            targets.append(pt1)
            cv2.line(img, pt1=(
                hight // 2 + int(350 * np.sin(np.radians(angle))), width + int(350 * np.cos(np.radians(angle)))),
                     pt2=pt1, color=(0, 0, 255), thickness=2)
            pt2 = (hight // 2, width)
            color = (0, 255, 0)
            cv2.line(img, pt1=pt1, pt2=pt2, color=color, thickness=1)
        else:
            instances.append(0)
            cv2.line(img, pt1=(
                hight // 2 + int(350 * np.sin(np.radians(angle))), width + int(350 * np.cos(np.radians(angle)))),
                     pt2=(hight // 2, width), color=(0, 255, 0), thickness=1)
    except:
        pass
    cv2.imshow('m', img)
    entered_key=cv2.waitKey(10)
    counter += 1

print(len(targets))
print(features)
feat = np.array(features)
np.save(f'Radar_Data0_{num_classes}_{num_samples}.npy',feat)
print(feat)
print(feat.shape)
y_coords, x_coords = zip(*targets)
heatmap, xedges, yedges = np.histogram2d(x_coords, y_coords, bins=(50, 50), range=[[0, img.shape[0]], [0, img.shape[1]]])
heatmap = heatmap / np.max(heatmap)
cmap = plt.get_cmap('jet')
plt.imshow(heatmap, cmap=cmap,extent=[yedges[0], yedges[-1], xedges[-1], xedges[0]])
plt.imshow(new_img, extent=[0,img.shape[1], img.shape[0],0],alpha=0.8)
plt.colorbar()
plt.savefig('resulting_image_NEW3.png', bbox_inches='tight', pad_inches=0)
plt.show()
