from ctypes import windll, create_unicode_buffer
import time
def get_Active_Window_Title():
    acw=windll.user32.GetForegroundWindow()
    length=windll.user32.GetWindowTextLengthW(acw)
    buf = create_unicode_buffer(length+1)
    windll.user32.GetWindowTextW(acw, buf, length+1)
    if buf.value:
        return buf.value
    else:
        return None
if __name__ == "__main__":
    prev=None
    while True:
        aw=get_Active_Window_Title()
        if prev!=aw and not aw==None:
            print(aw)
            prev=aw

