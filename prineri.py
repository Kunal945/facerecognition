import cv2
import face_recognition as f
import os, os.path

# simple version for working with CWD
noofimages=len([name for name in os.listdir('D:/face') if os.path.isfile(name)])

name={0:'Prince',1:'Kunal',2:'Mohit'}
p=int(input("what u want : "))

if p==1:
    cam = cv2.VideoCapture(0)
    
    cv2.namedWindow("test")
    
    img_counter = 0
        
            
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
    
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32: 
            test = "img{}.png".format(noofimages)
            cv2.imwrite(test, frame)
            print("{} written!".format(test))
            img_counter += 1
            break
    cam.release()
    cv2.destroyAllWindows()
elif p==2:
        
    known_faces=[]  
    
    for i in range(0,len([name for name in os.listdir('D:/face') if os.path.isfile(name)])):
        img = "img{}.png".format(i)
        image = f.load_image_file(img)
        face_locations = f.face_locations(image, model="hog")
        x="face_encoding"+str(i)
        x = f.face_encodings(image, face_locations)[0]
        known_faces.append(x)
    cam = cv2.VideoCapture(0)
    
    cv2.namedWindow("test")
    
    img_counter = 0
        
            
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
    
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32: 
            test = "test.png"
            cv2.imwrite(test, frame)
            print("{} written!".format(test))
            img_counter += 1
            break
    cam.release()
    cv2.destroyAllWindows()
    
    imgtest = cv2.imread('test.png', 0) 
    imgtest = cv2.cvtColor(imgtest, cv2.COLOR_BGR2RGB)
    
    # Find all the faces and face encodings in the current frame of video
    face_locations = f.face_locations(imgtest, model="hog")
    face_encodings = f.face_encodings(imgtest, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known faces
        match = f.compare_faces(known_faces, face_encoding, tolerance=0.60)
        os.remove('test.png')
    if match[0]:
        print(name[0])
    elif match[1]:
        print(name[1])
    elif match[2]:
        print(name[2])
