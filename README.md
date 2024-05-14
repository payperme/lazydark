# LAZYDARK

```
██╗      █████╗ ███████╗██╗   ██╗██████╗  █████╗ ██████╗ ██╗  ██╗
██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝
██║     ███████║  ███╔╝  ╚████╔╝ ██║  ██║███████║██████╔╝█████╔╝
██║     ██╔══██║ ███╔╝    ╚██╔╝  ██║  ██║██╔══██║██╔══██╗██╔═██╗
███████╗██║  ██║███████╗   ██║   ██████╔╝██║  ██║██║  ██║██║  ██╗
╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
```

## Synopsis

Simple script based on Python to dive into darkweb, i read in some Reddit post "_The darkweb is boring all the links are dead_" and maybe it has the reason. So i wrote this code. You only need a bunch of URLs in a text file, sorting line by line or a single URL, and the script will grab "_a href_" and "<title>" and other data, so you will have the status of the web page and its content in an easy way to navigate in some seconds.

## Dependencies

For Debian and its derivatives, you need to install the next dependencies:

```
sudo apt update
sudo apt install python3-bs4 python3-pymongo python3-requests mongodb-org-server mongosh
sudo systemctl start mongod.service
```

