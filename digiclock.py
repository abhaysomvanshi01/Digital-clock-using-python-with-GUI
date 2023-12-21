from tkinter import *                 #this module is for graphics
import datetime



def date_time():
    time= datetime.datetime.now()     #this is used to get time
    hr= time.strftime('%I')           #it will only give hr 
    mi= time.strftime('%M')
    sec= time.strftime('%S')
    am= time.strftime('%p')           #it gives am pm according to time
    
    

    date= time.strftime('%d')
    month= time.strftime('%m')
    year= time.strftime('%y')
    day= time.strftime('%a')


    lab_hr.config(text=hr)            #to replace text to hr
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)



    
    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)



    lab_hr.after(200,date_time)      #it act like refreshing data in 200 milisecond








#all graphic will start from here upto clock.mainloop()
clock = Tk()                          #tk() is class in tkinter assign to clock object
clock.title('       Digital Clock')   #title 
clock.geometry('1000x500')            #size of box
clock.config(bg='grey')               #to set background color


#label is used to add block type box label(classname,attributes)
lab_hr=Label(clock,text="00",font=('Time New Roman',60,"bold"),
             bg='black',fg='white')
lab_hr.place(x=120,y=50,height=110,width=100) #place is used to define the place of the block

lab_hr_txt=Label(clock,text="Hour",font=('Time New Roman',20,"bold"),
             bg='black',fg='white')
lab_hr_txt.place(x=120,y=190,height=40,width=100)





lab_min=Label(clock,text="00",font=('Time New Roman',60,"bold"),
             bg='black',fg='white')
lab_min.place(x=340,y=50,height=110,width=100)

lab_min_txt=Label(clock,text="Min",font=('Time New Roman',20,"bold"),
             bg='black',fg='white')
lab_min_txt.place(x=340,y=190,height=40,width=100)







lab_sec=Label(clock,text="00",font=('Time New Roman',60,"bold"),
             bg='black',fg='white')
lab_sec.place(x=560,y=50,height=110,width=100)

lab_sec_txt=Label(clock,text="Sec",font=('Time New Roman',20,"bold"),
             bg='black',fg='white')
lab_sec_txt.place(x=560,y=190,height=40,width=100)








lab_am=Label(clock,text="00",font=('Time New Roman',50,"bold"),
             bg='black',fg='white')
lab_am.place(x=780,y=50,height=110,width=100)

lab_am_txt=Label(clock,text="Am/Pm",font=('Time New Roman',20,"bold"),
             bg='black',fg='white')
lab_am_txt.place(x=780,y=190,height=40,width=100)





#for date

lab_date=Label(clock,text="00",font=('Time New Roman',60,"bold"),
             bg='black',fg='white')
lab_date.place(x=120,y=270,height=110,width=100) #place is used to define the place of the block

lab_date_txt=Label(clock,text="Date",font=('Time New Roman',20,"bold"),
             bg='black',fg='white')
lab_date_txt.place(x=120,y=410,height=40,width=100)





lab_mon=Label(clock,text="00",font=('Time New Roman',60,"bold"),
             bg='black',fg='white')
lab_mon.place(x=340,y=270,height=110,width=100) #place is used to define the place of the block

lab_mon_txt=Label(clock,text="Month ",font=('Time New Roman',20,"bold"),
             bg='black',fg='white')
lab_mon_txt.place(x=340,y=410,height=40,width=100)





lab_year=Label(clock,text="00",font=('Time New Roman',60,"bold"),
             bg='black',fg='white')
lab_year.place(x=560,y=270,height=110,width=100) #place is used to define the place of the block

lab_year_txt=Label(clock,text="Year",font=('Time New Roman',20,"bold"),
             bg='black',fg='white')
lab_year_txt.place(x=560,y=410,height=40,width=100)





lab_day=Label(clock,text="00",font=('Time New Roman',40,"bold"),
             bg='black',fg='white')
lab_day.place(x=780,y=270,height=110,width=100) #place is used to define the place of the block

lab_day_txt=Label(clock,text="Day",font=('Time New Roman',20,"bold"),
             bg='black',fg='white')
lab_day_txt.place(x=780,y=410,height=40,width=100)









date_time()
clock.mainloop()
