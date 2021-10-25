import retinaface
from retinaface import RetinaFace
img = "i.jpg"
obj = RetinaFace.detect_faces(img)
print(len(obj.keys()))
