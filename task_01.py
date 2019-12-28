#conditional statement
import subprocess
import webbrowser #default browser
import time
import os
options="""
    press 1 to start your default web browser
    press 2 to check your internet connection
    press 3 to check your internet speed
    press 4 to check current date and time
    press 5 to check current temperature in your city
    press 6 to check current public IP
    press 7 to create directory in your os
    press 8 to reboot your system
    press 9 to play song in youtube
    press 10 to search something in google search engine

"""
print(options)
#to accept input from user
choice=input()
#input function will accept in string only
print("You have entered ",choice)
#condition
if choice == '1':
    print("Open browser please wait")
    time.sleep(5)
    #time.sleep()
    webbrowser.open_new_tab('https://www.google.com')


elif choice == '2':
    output=subprocess.getstatusoutput('ping -c 2 8.8.8.8')
    if output[0]==0:
        print("Your internet is working")
    else:
        print("Your Internet is not working");
elif choice=='3':
    webbrowser.open_new_tab('https://fast.com/#')
    #checking internet speed

elif choice =='4':
    print("current time is ",subprocess.getoutput('date'))#time.ctime()that is for current time predefine in time module

elif choice =='5':
    webbrowser.open_new_tab('https://www.google.com')
    

elif choice =='6':
    webbrowser.open_new_tab('https://www.google.com/search?q=what+is+my+ip+address')
    
elif choice == '7':
    #asking for directory name
    dir_name=input("Enter the name of directory")
    #os.system()
    dir_op=subprocess.getstatusoutput("mkdir "+dir_name)
    if dir_op[0]==0:
        print("Your directory "+dir_name+"Successfully created")
    else:
        print("Please choose another directory name")

elif choice =='8':
    print("Restarting the system")
    time.sleep(2)
    os.system('shutdown /r /t 1');
elif choice == '9':
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=TLWy4GKJvbA&list=RDTLWy4GKJvbA&start_radio=1')
elif choice =='10':
    #taking input user
    msg=input("please enter your message to search")
    time.sleep(2)
    #time.sleep()
    webbrowser.open_new_tab('https://www.google.com/search?q='+msg)

else:
    print("wrong choice")
