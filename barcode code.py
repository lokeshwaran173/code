# let's read a barcode like the machine (product scanner in super market )


# using packages 
# pip install opencv-python 
# pip install pydub 
# pip install pyzbar 

import cv2 
from pyzbar.pyzbar import decode
from pydub import AudioSegment
from pydub.playback import play


# capture webcam 
cap = cv2.VideoCapture(0)

song = AudioSegment.from_wav("D:\desk\Downloads\barcode\store-scanner-beep-90395.mp3")

while cap.isOpened():
    success,frame = cap.read()
    # flip the image like mirror image 
    frame  = cv2.flip(frame,1)
    # detect the barcode 
    detectedBarcode = decode(frame)
    # if no any barcode detected 
    if not detectedBarcode:
        print("No any Barcode Detected")
    
    # if barcode detected 
    else:
        # codes in barcode 
        for barcode in detectedBarcode:
            # if barcode is not blank 
            if barcode.data != "":
                cv2.putText(frame,str(barcode.data),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                play(song)
                cv2.imwrite("code.png",frame)


    cv2.imshow('scanner' , frame)
    if cv2.waitKey(1) == ord('q'):
        break