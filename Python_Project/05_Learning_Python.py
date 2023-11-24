from email import message
from socket import timeout
import time
from turtle import title

from numpy import meshgrid
from plyer import  notification
count=0
if __name__=="__main__":
    while True:
        notification.notify(
            title="Time to learn python with codeWithHarry",
            message="developing websites and software, task automation, data analysis, and data visualization. ",
            timeout=5
        )
        count+=1
        time.sleep(60*60)
        if(count==5):
            break