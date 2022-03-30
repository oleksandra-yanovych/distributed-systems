import subprocess
import os


def login(text):
    text = text.split()
    str = "Success" if(text[1] == "login" and text[2] == "password") else "fail"
    print(str)

def echo(text):
    print(text)

def file(text):
    text = text.split()
    print(text[2] + " was sent to " + text[1])

def list(text):
    print(os.listdir("."))
    
def msg(text):
    text = text.split()
    print(text[2] + " was sent to " + text[1])
    
def ping(text):
    pin = subprocess.getoutput(f"ping 192.168.1.1")
    print(pin)

def exit(text):
    os._exit(0)

commands={
    "echo": echo,
    "ping": ping,
    "login": login,
    "list": list,
    "msg": msg,
    "file": file,
    "exit": exit
    }

while(True):
    try:
        text = input("Enter command: ")
        commands[text.split()[0]](text)
    except:
        print("Wrong command")