This is first use 
#!/bin/sh
#color

dir=/data/data/com.termux/files/home
server=/data/data/com.termux/files/usr/share/apache2/default-site/htdocs

1- cd $dir
 chmod +700 do_push/*
clear
apt-get update -y
clear
apt upgrade -y
clear
pkg install figlet -y
clear
figlet -f small installation
sleep 1
figlet -f small '0f'
sleep 1
figlet -f small do_push 
sleep 1
figlet -f small Framwork
sleep 1
echo $W "Installing requirements........"$G
apt-get install curl -y
apt-get install tor -y
apt-get install perl -y
apt-get install git -y
apt-get install hydra -y
apt-get install python -y
apt-get install python2 -y
apt-get install php -y
apt-get install nmap -y
apt-get install apache2 -y 
apt-get install cowsay -y
apt-get install ruby -y
echo "Pleas accept........"
sleep 3
termux-setup-storage
sleep 4
mkdir /sdcard/do_push
mkdir do_push-results
cd $dir
pip install -r do_push/.modules/.Infoga/requirements.txt
clear
sleep 1
pip2 install -r do_push/.modules/.recon-ng/REQUIREMENTS
clear
sleep 1
pip install PySocks
clear
sleep 1
python3 do_push/.modules/.slowloris/setup.py build
clear
python3 do_push/.modules/.slowloris/setup.py install
clear
clear
echo " Downloding start up .................."
sleep 1
echo " " $G
pip install --upgrade pip
pip install wordlist
mkdir $PREFIX/share/apache2/default-site/htdocs/rofaaee
cd $dir
rm -rf $server/index.html
mv do_push/.modules/Rofaaee.gif $server/
mv do_push/.modules/index.html $server/
rm -rf do_push/.modules/index.html 
rm -rf do_push/.modules/Rofaaee.gif
cat do_push/.modules/rofaaee.tar.gza* > do_push/rofaaee.tar  
tar -zxvf do_push/rofaaee.tar
mv rofaaee.txt do_push/.modules/
cd $dir
gcc do_push/.modules/.xerxes/xerxes.c -o xerxes 
mv do_push/xerxes do_push/.modules/.xerxes/
chmod +x do_push/*
chmod +x do_push/.modules/.*
chmod +x do_push/.modules/*
chmod +x do_push/.modules/.Infoga/*
chmod +x do_push/.modules/.theHarvester/*
chmod +x do_push/.modules/.CMSeeK/*
chmod +x do_push/.modules/.RED_HAWK/*
chmod +x do_push/.modules/.metagoofil/*
chmod +x do_push/.modules/.recon-ng/*
chmod +x do_push/.modules/.Python-Hash-Cracker/*
chmod +x do_push/.modules/.torshammer/*
chmod +x do_push/.modules/.slowloris/*
chmod +x do_push/.modules/.xerxes/*
chmod +x do_push/.modules/.sqlmap/*
chmod +x do_push/.modules/.theHarvester/*
chmod +x do_push/.modules/.metagoofil/*
chmod +x do_push/.modules/.Hash*
cd $dir
rm -rf do_push/rofaaee.tar
rm -rf do_push/rofaaee.tar.gza*
rm -rf do_push/.modules/rofaaee.tar.gza*
mv -f do_push/rofaaee.txt do_push/.modules/
mv -f do_push/do_push $PREFIX/bin/
mv -f do_push $PREFIX/share/
cd $dir
rm -rf $HOME/do_push
sleep 3
clear
figlet -f small "   DONE!"
echo "Now Type in new terminal ————>  do_push"
sleep 3

cd $dir
