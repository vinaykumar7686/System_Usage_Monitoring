from ctypes import windll, create_unicode_buffer
import pandas as pd
import time,os,sys,datetime

def get_Active_Window_Title():
    '''
    Returns currently active applications' title
    '''
    acw=windll.user32.GetForegroundWindow()
    length=windll.user32.GetWindowTextLengthW(acw)
    buf = create_unicode_buffer(length+1)
    windll.user32.GetWindowTextW(acw, buf, length+1)
    if buf.value:
        return buf.value
    else:
        return None

if __name__ == "__main__":
    #Initialising Previous application Variable as None
    prev=None

    #Running an Infinite Loop 
    while True:
        #Getting active applications' title
        aw=get_Active_Window_Title()

        #True iff previos and current apps are different(To avoid repeated entries)
        if prev!=aw and not aw==None:

            print(aw)
            
            #creating a dictionary that stores the data to be pushed into dataset 
            data={'application':[aw],'stime':[(datetime.datetime.now()).strftime("%X")],'day':[(datetime.datetime.now()).strftime("%A")],
            'date':[(datetime.datetime.now()).strftime("%x")]}
            
            #converting dictionary into dataframe
            df=pd.DataFrame(data, columns=['application', 'stime', 'day', 'date'])

            #appending dataframe to external csv file
            df.to_csv('usagelog.csv', mode='a',header= False,index=False)

            #updating prev to current applications' name
            prev=aw
    

