import eel
import os

@eel.expose
def Configure(password):
    conf_commands=[
        "echo "+password+"| echo y | sudo -S apt install nginx".format(password), "sudo ufw allow https comment 'Open all to access Nginx port 443'", "sudo ufw allow http comment 'Open access Nginx port 80'", 
        "sudo ufw allow ssh comment 'Open access OpenSSH port 22'", "sudo ufw enable", "sudo chown -R 755 /etc/hosts", "sudo add-apt-repository universe",
        "echo y | sudo apt install php7.2-cli php7.2-xml php7.2-mysql"
    ]
    path = os.path.abspath(__file__)
    fname = path.find('main.py')
    for i in conf_commands:
        os.system(i)
    os.chdir('/home')
    os.system('echo '+password+'|sudo -S mkdir domains'.format(password))
    os.chdir(path[:fname])

@eel.expose
def Create(name, password):
    path = os.path.abspath(__file__)
    fname = path.find('main.py')
    if(os.path.exists('/home/domains/' + name)==False):
        os.chdir("/home/domains/")
        os.system("mkdir " + name)
        os.system("chmod -R 777 " + name)
        os.chdir(path[:fname])
    if(os.path.exists('/etc/nginx/sites-enabled/' + name)==False):
        os.chdir("/etc/")
        os.system("sudo chmod -R 777 nginx")
        os.chdir("nginx/sites-available/")
        conf = open(str(name), 'w')
        conf.write("server {\n    listen      80;\n    server_name " + name + ";\n    root /home/domains/" + name + "/;\n    index index.html index.htm index.php;\n        location / {\n            try_files $uri $uri/ /index.php?q=$uri&$args;\n    }\n    location ~ \.php$ {\n            include snippets/fastcgi-php.conf;\n            fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;\n    }\n    location ~ /\.ht {\n            deny all;\n    }\n}")
        conf.close()
        os.chdir("/etc/nginx/sites-enabled/")
        os.system("echo "+password+"|sudo -S ln -v -s /etc/nginx/sites-available/" + name)
        os.chdir(path[:fname])
    if (not name in open('/etc/hosts', 'r').read()):
        os.chdir(path[:fname])
        os.system("echo "+password+"|sudo -S python3 hosts_edit.py "+name)
    os.system("echo "+password+"|sudo -S systemctl reload nginx")
    os.chdir(path[:fname])
eel.init('web')
eel.start('index.html')