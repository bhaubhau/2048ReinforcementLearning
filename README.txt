#Host OS: Ubuntu18.04.2 inside VM

#use commands below only which are required to setup the necessary libraries on OS
sudo apt-get update
sudo apt-get -f dist-upgrade
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -f -y
sudo dpkg -i google-chrome-stable_current_amd64.deb
chmod 600 .ssh/id_rsa 
chmod 700 .ssh
sudo apt install python-pip
sudo apt install python3-pip
sudo pip3 install selenium
sudo pip3 install numpy

#download, unzip and place relevant chromedriver compatible with chrome version from below link and do chmod+x on it
https://chromedriver.chromium.org/

#To run the code cd to project directory and run the command
$ python3 driver.py