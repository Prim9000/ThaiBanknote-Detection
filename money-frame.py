import torch
from gtts import gTTS
from io import BytesIO
import cv2
import os
import time

vid = cv2.VideoCapture(0)
frame_count = 0
start = time.time()
first = True
frames = []

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    frame_count += 1
    
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='bill-best.pt')  # local model
    if ret:
		  key = cv2.waitKey(1)
		  if frame_count % 60 == 0:
			  end = time.time()
        # Inference
        results = model(frame)

        df = results.pandas().xyxy[0]

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

        if text.isspace():
            continue
        else:
            myOutput = gTTS(text=text, lang='en')
            myOutput.save('talk.mp3')
            os.system('mpg123 talk.mp3')
    cv2.destroyAllWindows()
