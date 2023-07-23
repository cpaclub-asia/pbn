#sudo apt-get update
#sudo apt-get install tor torsocks

#tor -f torrc.1
#exit 0


#sudo service tor start
nohup tor -f torrc.1 >> data/logs/torrc.1 &
nohup tor -f torrc.2 >> data/logs/torrc.2 &
nohup tor -f torrc.3 >> data/logs/torrc.3 & 
nohup tor -f torrc.4 >> data/logs/torrc.4 &
nohup tor -f torrc.5 >> data/logs/torrc.5 &
nohup tor -f torrc.6 >> data/logs/torrc.6 &
nohup tor -f torrc.7 >> data/logs/torrc.7 &
nohup tor -f torrc.8 >> data/logs/torrc.8 &

