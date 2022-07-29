import torch
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True) # モデル読み込み

def object_detection(img):
    results = model(img) # 物体検知
    objects = results.pandas().xyxy[0]  # 検出結果をDataFrameに
    return objects
