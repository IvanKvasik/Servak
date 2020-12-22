import os
from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Servak")

conf_commands=[
    "apt install nginx", "ufw allow https comment 'Open all to access Nginx port 443'", "ufw allow http comment 'Open access Nginx port 80'", 
    "ufw allow ssh comment 'Open access OpenSSH port 22'", "ufw enable", "chown -R 755 /etc/hosts"
]
def Configure():
    for i in conf_commands:
        os.system(i)
    os.chdir('/home')
    os.system('mkdir domains')
    Label(root, text="Now Nginx server is installed. Would you like to create your first project?").grid(row=1, column=0, columnspan=2)

def Create():
    name = pr_name.get()
    os.chdir("/home/domains/")
    os.system("mkdir " + name)
    os.chdir("/etc/nginx/sites-available/")
    conf = open(str(name), 'w')
    conf.write("server {\n    listen      80;\n    server_name " + name + ";\n    root /home/domains/" + name + "/;\n    index index.html index.htm index.php;\n}")
    conf.close()
    os.chdir("/etc/nginx/sites-enabled/")
    os.system("ln -v -s /etc/nginx/sites-available/" + name)
    hosts = open('/etc/hosts', 'a')
    hosts.write("127.0.0.1\t" + name + "\n")
    hosts.close()
    os.system("sudo systemctl reload nginx")
    Label(root, text="Success! Go to the /home/domains/" + name + '/ and create your first site file!').grid(row=4, columnspan=3)
def Enter():
    # conf.destroy()
    # create.destroy()
    global pr_name
    Label(root, text="Enter project name:").grid(row=1, column=0, columnspan=2)
    pr_name = Entry(root)
    pr_name.grid(row=2, column=0)
    Button(root, text = "Enter", command=Create).grid(row=2, column=1)
    Label(root, text="Warning! Don't create project before basic configuration!").grid(row=3, columnspan=5)

conf = Button(root, text="Basic configuration", command=Configure)
conf.grid(row=0, column=0)

create = Button(root, text="Create project", command=Enter)
create.grid(row=0, column=1)

root.mainloop()
