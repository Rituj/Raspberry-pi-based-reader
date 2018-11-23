import cv2
import sys
import pytesseract
from gtts import gTTS
import os
if __name__=='__main__':
    if len(sys.argv)<2:
        print('USAGE:python ocr.py image.jpg')
        sys.exit(1)
    impath=sys.argv[1]
    config=('-l eng --oem 1 --psm 3')
    im=cv2.imread(impath,cv2.IMREAD_COLOR)
    text=pytesseract.image_to_string(im,config=config)
    print(text)
    try:
    	tts=gTTS(text,lang='en')
    except AssertionError:
    	sys.exit()
    tts.save('/home/pi/Desktop/text.mp3')
    os.system('cvlc --play-and-exit /home/pi/Desktop/text.mp3')
            