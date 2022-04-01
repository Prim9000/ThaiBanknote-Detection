import torch
#from gtts import gTTS
from io import BytesIO
import cv2
import os

vid = cv2.VideoCapture(0)
framecount = 0

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='final-best.pt')  # local model

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    #cv2.imshow('frame', frame)
    
    framecount+=1
    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if framecount%20 == 0:
        # Inference
        #results = model(frame)
        results = model(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), size=400)
        #results.show()
        df = results.pandas().xyxy[0]
        df = df[df['confidence'] > 0.5].dropna()
        # Speak the labels
        text = ""

        for label in df['name']:
          if label == 'twenty':
            os.system('mpg123 twenty.mp3')
          elif label == 'fifty':
            os.system('mpg123 fifty.mp3')
          elif label == 'onehundred':
            os.system('mpg123 onehundred.mp3')
          elif label == 'fivehundred':
            os.system('mpg123 fivehundred.mp3')
          elif label == 'thousand':
            os.system('mpg123 thousand.mp3')
          else :
            text += label + " "
cv2.destroyAllWindows()
