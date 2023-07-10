sudo docker run -d --name websocket_server -p 8008:8008 -v /etc/timezone:/etc/timezone:ro -v /etc/localtime:/etc/localtime:ro -v /home/nut/ajinomoto/Ajinomoto/websocket/:/workspace/:rw ws:server

sudo docker start container
