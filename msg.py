import requests, os, sys, time

print("\033[41mCoded by https://github.com/ProfessorCipher\033[0m")

print("\033[96m Version 2.0 \033[0m")

print("\033[32m checking server... \033[0m")

time.sleep(2)

os.system("bash rq.sh")

def menu() :

    print("\033[96m1.\033[0m \033[92mSend anonymous sms\033[0m")

    print("\033[96m2.\033[0m \033[92mCheck status of sms\033[0m")

def control() :

    ctrl = input("\033[100mWhat you want to do : \033[0m")

    if ctrl == "1" :

        sms()

    elif ctrl == "2" :

        status()

    else :

        print("\033[91mInvalid number\033[0m")

def sms() :

   phone_no = input("\033[34menter phone number : \033[0m")

   msg = input("\033[34mmessage to send : \033[0m")

   resp = requests.post('https://textbelt.com/text',{

	'phone' : phone_no,	'message' : msg ,

	'key' : 'textbelt'

   })

   print(resp.text)

   if '"success" : true' in resp.text :

       print('Msg delivered! ')

   if '"success" : false' in resp.text :

       print("\033[34mfailed to send msg!\n Sorry!! Try again!! ")

def status() :

  textID = input("Enter textID of sms : ") 

  os.system(f"curl https://textbelt.com/status/{textID}")

os.system("clear")

os.system("toilet -f mono12 -F gay GALAXY- ")

print("\033[5m.\033[41mCoded by github.com/ProfessorCipher")

print("\033[33m.\033[33mRe-updated tool by 445H4N or also known as PROF.CIPHER :)")

menu()

control()
