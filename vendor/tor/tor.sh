#sudo apt-get update
#sudo apt-get install tor torsocks

#sudo service tor start
sudo tor -f torrc.2 >> ../../../log/torrc.2 &
sudo tor -f torrc.3 >> ../../../log/torrc.3 & 
sudo tor -f torrc.4 >> ../../../log/torrc.4 &
sudo tor -f torrc.5 >> ../../../log/torrc.5 &
sudo tor -f torrc.6 >> ../../../log/torrc.6 &
sudo tor -f torrc.7 >> ../../../log/torrc.7 &
sudo tor -f torrc.1 >> ../../../log/torrc.1 &
