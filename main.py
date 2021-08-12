from detector import YOLO

yolo = YOLO("yolo", 0.5, 0.3)
yolo.detect("images/human.jpeg")
