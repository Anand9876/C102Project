import cv2
import dropbox
import time
import random

start_time= time.time()

def take_snapshot():
    number=random.randint(0,100)

    videoCaptureObject=cv2.VideoCapture(0)
    result = True
    while(result):

        ret,frame = videoCaptureObject.read()
        img_name='Image'+str(number)+'.jpeg'
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print('Just now the snapShot has taken successful!')

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token='sl.BDBVqwAURilCihiMUd-Zn50e_Bx1aTMBdDZrqLWI0uSBzaID9eWQseKHVOSz3ByEpdrPcCAISSzClhgxYUL9EA7XnNtCZQp_M3E5F5OKI-dQeaXn8Df9XkBEourRl3cBfJ8RRdZo'
    file=img_name 
    file_origin=file
    file_to='/DropBox Folder'+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_origin,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')

def main():
    while((True)):
         if((time.time()-start_time)>=10):
             name=take_snapshot()
             upload_file(name)
main()

