from tkinter import *
import tkinter as tk
import serial
import pygame
from tkinter import messagebox as m_box
import face_recognition as f
import os
import cv2
from twilio.rest import Client
from PIL import ImageTk,Image
import random
pygame.init()
def play():#play please select your bank
    pygame.mixer.music.load("C:\\Users\\dell\\Downloads\\psb.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
def play1():#play please select your bank
    pygame.mixer.music.load("C:\\Users\\dell\\Downloads\\syf.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
def play2():#play please select your bank
    pygame.mixer.music.load("C:\\Users\\dell\\Downloads\\wtoatm.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device    

z=random.randint(100000,999999)
master = tk.Tk()
#master.configure(bg="Blue2")
play()
master.title('ATM SECURITY SYSTEM')
image = Image.open('D://hd.gif')
photo_image = ImageTk.PhotoImage(image)
label = tk.Label(master, image = photo_image)
label.grid()
master.geometry('1500x1000')
#pygame.init()
Label(master, text="Please Select Your Bank ",font=("Times New Roman",60)).place(x=405, y=0)
var1 = IntVar()
Checkbutton(master, text="State Bank of india ",font=("Times New Roman",20), variable=var1).place(x=0,y=100)
var2 = IntVar()
Checkbutton(master, text="Bank Of India ",font=("Times New Roman",20), variable=var2).place(x=0,y=150)
var3 = IntVar()
Checkbutton(master, text="Central Bank of India ",font=("Times New Roman",20), variable=var3).place(x=0,y=200)
var4 = IntVar()
Checkbutton(master, text="Punjab National Bank	 ",font=("Times New Roman",20), variable=var4).place(x=0,y=250)
var5 = IntVar()
Checkbutton(master, text="Oriental Bank of Commerce ",font=("Times New Roman",20), variable=var5).place(x=0,y=300)
var6 = IntVar()
Checkbutton(master, text="Bhartiya Mahila Bank",font=("Times New Roman",20), variable=var6).place(x=0,y=350)
var7 = IntVar()
Checkbutton(master, text="Paytm Payment Bank",font=("Times New Roman",20), variable=var7).place(x=0,y=400)
var8 = IntVar()
Checkbutton(master, text="Andhra bank  ",font=("Times New Roman",20), variable=var8).place(x=0,y=450)
var9 = IntVar()
Checkbutton(master, text="Allahabad Bank ",font=("Times New Roman",20), variable=var9).place(x=0,y=500)
var10 = IntVar()
Checkbutton(master, text="Kotak Mahindra Bank",font=("Times New Roman",20), variable=var10).place(x=0,y=550)
var11 = IntVar()
Checkbutton(master, text="Axis Bank ",font=("Times New Roman",20), variable=var11).place(x=0,y=600)
var12 = IntVar()
Checkbutton(master, text="Central Bank Of India",font=("Times New Roman",20), variable=var12).place(x=0,y=650)

def window2():#2nd window open
 window = tk.Tk() 
 window.configure(bg="cornflowerblue")
 play1()
 window.resizable(1,1)
 
 window.title("Welcome to advance security system")
 window.geometry('1500x1000')
 otp = Label(window,text = "Enter Your otp",font=("Times New Roman",15)).place(x = 400,y = 300)  
 e2 = Entry(window)
 e2.place(x = 600, y = 300) 
 
 



 def otp(): 
   
    account_sid = "AC4b25e6f4e3b63e09b930618608bc74e4"
    auth_token = "c9f103d1eb32d4c8d858d52df38d2c87"
    client = Client(account_sid, auth_token)

    client.messages.create(
            body='The otp for authentication of atm banking system is '+str(z),
         from_='++12052731328',
         to='+918757460985'
                )
 def otp1(): 
    account_sid = "AC3a2a62303c4325514a1a98f3c744fbd7"
    auth_token = "1f2f5eadd64c7073d12038ca303886b2"
    client = Client(account_sid, auth_token)

    client.messages.create(
         body='The otp for authentication of atm banking system is '+str(z),
         from_='++12052731328',
         to='+918969066899'
                )
 def otp2(): 
 
    account_sid = "AC3a2a62303c4325514a1a98f3c744fbd7"
    auth_token = "1f2f5eadd64c7073d12038ca303886b2"
    client = Client(account_sid, auth_token)

    client.messages.create(
         body='The otp for authentication of atm banking system is'+str(z),
         from_='++12052731328',
         to='+918969066899'
                )   
 def fingerprint():
    
     ser1 = serial.Serial("COM7",9600,timeout=1)
     while True:
      arduinodata = ser1.read().decode('ascii')
      print(arduinodata) 
      
      print(arduinodata)    
      if arduinodata == '1':
          label9 = Label(window,text="Thank You mohit Otp sent to your registered mobile no",font=("Arial Bond",20)).place(x=800,y=200)
          otp2()
          break;
      elif arduinodata == '2':
          label8 = Label(window,text="Thank You mayank Otp sent to your registered mobile no",font=("Arial Bond",20)).place(x=800,y=200)
          otp1()
          break;
      elif arduinodata == '5':
          label7 = Label(window,text="Thank You kunal Otp sent to your registered mobile no",font=("Arial Bond",20)).place(x=800,y=200)
          otp()
          break;
      elif arduinodata == '0':
          label6 = Label(window,text="Try Again Fingerprint not recognized",font=("Arial Bond",20)).place(x=800,y=200)   
          break;
     

 def face():
     
         noofimages=len([name for name in os.listdir('D:/face') if os.path.isfile(name)])
         name={0:'Prince',1:'Kunal',2:'Mohit',3:'Mayank'}
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
             klabel = Label(window, text="Hello  mohit otp  was sent to your Registered mobile no").place(x=800,y=300)
             otp()
         elif match[1]:
             print(name[1])
             klabel = Label(window, text="Hello  Kunal otp  was sent to your Registered mobile no").place(x=600,y=400)
             otp()
         elif match[2]:
             print(name[2])
             klabel = Label(window, text="Identified as Mayank Otp  was sent to your Registered mobile no").place(x=800,y=300)
             otp1()
         else:
             label6 = Label(window, text="Face not recognized").place(x=800,y=400)
         
         

 
 def on_button():
    #e1 = Entry(window).place(x = 170, y = 50)
    pass


 def on_button1():
    #e1 = Entry(window).place(x = 170, y = 50)
    print(type(e2))
    a=e2.get()
    print(type(a))
    if int(a) == z:
        slabel = Label(window, text="You Have Succesfully Authenticated",font=("Arial Bond",20),bg='peachpuff').place(x=600,y=700)
        button2window = Button(window,text="ENTER",width=30,bg='indianred1', command=new1window)
        button2window.place(x=600,y=500)
    else:
        tlabel = Label(window, text="Sorry PLease re enter your otp ").place(x=800,y=450)      
        tlabel = Label(window, text="3 unsuccesfull try will Block your account !!!").place(x=800,y=500)      


 button = Button(window,text="Scan Your Face",font=("Arial Bond",30),bg='mediumpurple4',command=face)
 button.place(x=200,y=25)
 button = Button(window,text="Scan Your Fingerprint",font=("Arial Bond",30),bg='mediumpurple4',command=fingerprint)
 button.place(x=850,y=25)  
 button = Button(window,text="Enter",width=30,bg='mediumpurple1', command=on_button1)
 button.place(x=800,y=300)
 

 def new1window():
     new1window = Tk()
     new1window.configure(bg="cornflowerblue")
     play2()
     
     Label(new1window, text="Welcome To Our ATM Service",font=("Times New Roman",60)).place(x=200,y=100)
     new1window.geometry('1500x1000')

     def clicked():
         lbl1=Label(text="Button was clicked !!")

     def withdrawal():
         withdrawal = Tk() 
         withdrawal.configure(bg="purple1")
         withdrawal.geometry('1500x1000')
         lbl2 = Label(withdrawal, text="Please enter your amount for withdrawal",font=("Arial Bond",15)).place(x=600,y=30)
         z = Entry(withdrawal)
         z.place(x=600,y=130)
         def on_button4():
             lbl2 = Label(withdrawal, text="Amount of Rs %s succesfully Withdrawan From your bank account" % (z.get()),font=("Arial Bond",15)).place(x=600,y=330)
    
         but = Button(withdrawal,text="Enter", command=on_button4)
         but.place(x=600,y=230)
         account_sid = "AC4b25e6f4e3b63e09b930618608bc74e4"
         auth_token = "c9f103d1eb32d4c8d858d52df38d2c87"
         client = Client(account_sid, auth_token)

         client.messages.create(
              body='Amount of %s is sussecfully withdrawan from your bank account' % (z.get()),
              from_='++12052731328',
              to='+918757460985'
                )

 
    
         withdrawal.mainloop()
    
    
     def balance():
      

         balance = Tk() 
         balance.configure(bg="purple1")
         balance.geometry('1500x1000')
         lbl3 = Label(balance, text="Your balance is 50000 rupees",font=("Arial Bond",15)).place(x=600,y=30)
         account_sid = "AC4b25e6f4e3b63e09b930618608bc74e4"
         auth_token = "c9f103d1eb32d4c8d858d52df38d2c87"
         client = Client(account_sid, auth_token)

         client.messages.create(
              body='The balance in your account is 50000 ',
              from_='++12052731328',
              to='+918757460985'
                )
         balance.mainloop()
    

     def Statement():
         Statement = Tk() 
         Statement.configure(bg="purple1")
         Statement.geometry('1500x1000')
         lbl2 = Label(Statement, text=" 5000  is withdrawal from your account on 10/10/19 ",font=("Arial Bond",20)).place(x=600,y=30)
         Statement.mainloop()
    
    
     def Fund_Transfer():
         Fund_Transfer = Tk() 
         Fund_Transfer.configure(bg="purple1")
         Fund_Transfer.geometry('1500x1000')
         lbl2 = Label(Fund_Transfer, text="Please enter your amount for Transfer",font=("Arial Bond",15)).place(x=600,y=30)
         z = Entry(Fund_Transfer)
         z.place(x=600,y=130)
         def on_button6():
             lbl3 = Label(Fund_Transfer, text="Amount of Rs %s succesfully Transfer to another account" % (z.get()),font=("Arial Bond",15)).place(x=600,y=330)
        
         but5 = Button(Fund_Transfer,text="Enter", command=on_button6)
         but5.place(x=600,y=230)
         account_sid = "AC4b25e6f4e3b63e09b930618608bc74e4"
         auth_token = "c9f103d1eb32d4c8d858d52df38d2c87"
         client = Client(account_sid, auth_token)

         client.messages.create(
              body='Amount of %s is succesfuly transfer to another bank acount' % (z.get()),
              from_='++12052731328',
              to='+918757460985'
                )

         Fund_Transfer.mainloop()
    
     def Deposit():
         Deposit = Tk()
         Deposit.configure(bg="purple1")
         Deposit.geometry('1500x1000')
         lbl2 = Label(Deposit, text="Please enter your amount for deposit",font=("Arial Bond",15)).place(x=600,y=30)
         x = Entry(Deposit)
         x.place(x=600,y=130)
         def on_button5():
             x1=x.get()
             lbl2 = Label(Deposit,text=" Amount of Rs %s succesfully Deposit to your bank account" % (x1),font=("Arial Bond",15)).place(x=600,y=330)
      
         but1 = Button(Deposit,text="Enter", command=on_button5)
         but1.place(x=600,y=230)
         account_sid = "AC4b25e6f4e3b63e09b930618608bc74e4"
         auth_token = "c9f103d1eb32d4c8d858d52df38d2c87"
         client = Client(account_sid, auth_token)

         client.messages.create(
              body='Amount of %s is succesfully deposit to your bank account' % (x.get()),
              from_='++12052731328',
              to='+918757460985'
                )

         Deposit.mainloop()
         

    
     
     btn =Button(new1window,text="Set preferences",font=("Arial Bond",18),bg="Cyan",fg="red",command=clicked)
     btn1 =Button(new1window,text="Withdrawal",font=("Arial Bond",18),bg="Cyan",fg="red",command=withdrawal)
     btn2 =Button(new1window,text="Balance",font=("Arial Bond",18),bg="Cyan",fg="red",command=balance)
     btn3 =Button(new1window,text="Mini statement",font=("Arial Bond",18),bg="Cyan",fg="red",command=Statement)
     btn4 =Button(new1window,text="Fund Transfer",font=("Arial Bond",18),bg="Cyan",fg="red",command=Fund_Transfer)
     btn5 =Button(new1window,text="Deposit",font=("Arial Bond",18),bg="Cyan",fg="red",command=Deposit)
     btn.place(x=200,y=300)
     btn1.place(x=200,y=400)
     btn2.place(x=200,y=500)
     btn3.place(x=950,y=300)
     btn4.place(x=950,y=400)
     btn5.place(x=950,y=500)
     
 window.mainloop()
 

def newwindow():
    if var1.get()==1 or var2.get()==1 or var3.get()==1 or var4.get()==1 or var5.get()==1 or var6.get()==1 or var7.get()==1 or var8.get()==1:
        window2()
    else:
        m_box.showerror('Error','Please Select an entry')


btn = Button(master, text='Enter',width=30,bg="mediumpurple4",fg="white" ,command=newwindow).place(x=1200, y=500)
master.mainloop()


