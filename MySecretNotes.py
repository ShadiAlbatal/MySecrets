import datetime
import os

print ("feel free to tell anyting in your heart")

def search(username, password):
    for line in open("userlist.txt","a+").readlines():
            login_info = line.split()
            if username == login_info[0] and password == login_info[1]:
                return True
    return False


with open('userlist.txt', 'a+') as my_file:
   Greet = input("Are you a member of us? type:  \ny to login \nn to continue \n ")
   if Greet == 'y':
       print("Welcome Dear")
   else:
        membership = input("Would you like to become a member? type: \ny to create new \npress any key else to exit\n")
        if membership == 'y':
           create_user = input("Please type your new-username:  " "\n")
           create_pass = input("Please type a password:  " "\n")
           my_file.write(' '.join([create_user, create_pass])+ "\n")
           create_secret= create_user + create_pass + ".txt"
           open(create_secret,"a+")
           print("Your username has nw been created.\nlogin please. ")
        else:
           print("thank you for visiting, take care")
           quit()

with open('userlist.txt', 'a+') as my_file:
   username = input("Type in your Username:  " "\n")
   password = input("Type in your Password:  " "\n")
   while True:
       if search(username, password):
           print ("your ntes: \n")
           open_nte_RBI= username + password + ".txt"
           LHMDL_read_secrets= open(open_nte_RBI,"r").read()
           print (LHMDL_read_secrets)
           choice = input("Do you want is in your mind? \nn to add new secret \nd to prune all your secrets (might work only on linux) \nq to quit\n")
           if choice == "n":
                new_nte_LLH = input("Tell me please\n")
                BSMLH_open_= open(open_nte_RBI, "a+")
                HKBR_add_new = new_nte_LLH + "\n" + str(datetime.datetime.now())
                BSMLH_open_.write(HKBR_add_new + "\n\n")
                BSMLH_open_.close()
            ## the d option might work only on linux
           elif choice == "d":
                cwd = os.getcwd()
                os.remove(cwd + '/' + open_nte_RBI)
           elif choice == "q":
                quit()
           else:
                print("didnt understand")