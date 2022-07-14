import detect_yolov5 as yolo
import cv2


slot_list = []
with open("slot.txt", "r") as f:
    index = 0
    for line in f.readlines():
        if (index != 0):
            if not line.strip():
                continue
            x1, y1, w, h = line.split(" ")
            x1, y1, w, h = int(x1), int(y1), int(w), int(h)
            x2, y2 = x1 + w, y1 + h
            slot_list.append([x1, y1, x2, y2])
        else:
            index = index + 1
            continue
        
img = cv2.imread("images/D35_5.jpg")
# img = cv2.imread("images/person.png")

detection = yolo.Detection()

weight_path = "weights/yolov5s.pt"
classes = [2, 5, 7]
conf = 0.2
imgsz = 640
device = "cpu"

detection.setup_model(weight_path, classes, conf, imgsz, device)

detect_list = detection.detect(img)

global list_busy
global list_empty


list_busy = []
list_empty = []


for slot_box in slot_list:
    x1_slot, y1_slot, x2_slot, y2_slot = slot_box

    index = slot_list.index(slot_box) + 1

    is_busy = False
    for detect_box in detect_list:

        x1, y1, x2, y2, name, conf = detect_box
        center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2
        
        # cv2.circle(img, (center_x, center_y), 5, (0, 0, 255), -1)
        if x1_slot <= center_x <= x2_slot and y1_slot <= center_y <= y2_slot:
            
            title = str(index) + ' ' + str(round(conf, 2))

            is_busy = True
            list_busy.append(index)


            cv2.rectangle(img, (x1_slot, y1_slot), (x2_slot, y2_slot), (0, 0, 255), 2)
            cv2.putText(img, title, (x1_slot, y1_slot), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
            break
    if not is_busy:
        list_empty.append(index)
        cv2.rectangle(img, (x1_slot, y1_slot), (x2_slot, y2_slot), (0, 255, 0), 2)
        cv2.putText(img, str(index), (x1_slot, y1_slot), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)

busy = ''
empty = ''

for i in list_empty:
    empty = empty + str(i) + ' '

with open('list_busy.txt', 'w+') as f:
    list_busy = sorted(list_busy)
    for i in list_busy:
        f.write(str(i) + '\n')
        busy = busy + str(i) + ' '


for i in detect_list:
    print('Models: ', str(i))

print('Các ô đỗ đang rảnh: ', empty)
print('Các ô đỗ đang bận: ', busy)

img = cv2.resize(img, (1280, 540))
cv2.imshow("img", img)
key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destroyAllWindows()
