import torch
import sys
import os
sys.path.insert(0,'./facelib/detection/yolov5face')
model = torch.load('facelib/detection/yolov5face/yolov5n-face.pt', map_location='cpu')['model']
torch.save(model.state_dict(), os.path.join(os.environ['COMFYUI_MODELS_PATH'], 'facedetection'))