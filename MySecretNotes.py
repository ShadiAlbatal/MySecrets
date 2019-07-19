
import datetime
import os

print ("feel free to tell anyting in your heart")

def search(username, password):
    for line in open("userlist.txt","a+").readlines():
            login_info = line.split()
            if username == login_info[0] and password == login_info[1]:
                return True
    return False

def verify(username):
    for line in open("userlist.txt","r").readlines():
            login_info = line.split()
            if username == login_info[0]:
                return True
    return False


with open('userlist.txt', 'a+') as my_file:
    while True:
        Greet = input("warm welcome to your app my secrets, type:  \ny to login \nc to create \n ")
        if Greet == 'y':
            print("Welcomeback Dear")
            break
        elif Greet == 'c':
            while True:
                create_user = input("Please type your new-username:  " "\n")
                create_pass = input("Please select a password:  " "\n")
                if verify(create_user):
                    print("username is already taken, try again")
                else:
                    my_file.write(' '.join([create_user, create_pass])+ "\n")
                    create_secret= create_user + create_pass + ".txt"
                    open(create_secret,"a+")
                    print("Your username has been created.\nyou will be directed to the start page. ")
                    break
        else:
            print(" did not understand, try again please ")


with open('userlist.txt', 'a+') as my_file:
   while True:
        username = input("Type in your Username:  " "\n")
        password = input("Type in your Password:  " "\n")
        if search(username, password):
            while True:
                print ("your notes: \n")
                open_nte_RBI= username + password + ".txt"
                LHMDL_read_secrets= open(open_nte_RBI,"a+").read()
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
                    open(open_nte_RBI, "w").close()
                elif choice == "q":
                    quit()
                else:
                    print("didnt understand")
        else:
            print("try again")
