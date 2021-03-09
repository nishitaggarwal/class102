import time 
import cv2
import dropbox
import random

start_time = time.time()
#print(start_time)

def take_snapshot():
    number = random.randint(1,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"  + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False
    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_Token  = "sl.AsscF0jomIx7A6KZS1hA0Cd1jRCbmEJywhKDccR5zbP8mfyRfKET_0k39xRYpYCNvNQG86fvHB66MIItyhvujYRH1Jo5VulrXpwuxd6ycsemnguUKbAWqFcgkHr1skdAzt6oT1w"
    file = img_name
    file_from = file
    file_to = "/Python/" + (img_name)
    dbx = dropbox.Dropbox(access_Token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while True:
        if((time.time() - start_time)>= 10 ):
            name = take_snapshot()
            upload_file(name)
            
main()