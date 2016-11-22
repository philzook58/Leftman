echo "serving video on port 2222"
raspivid -t 0 -w 640 -h 480 -hf -ih -fps 20 --rotation 180 -o - | nc -k -l 2222
