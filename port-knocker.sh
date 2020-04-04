##Created by micosec

for x in {1..3}; do nmap -Pn --max-retries 0 -p $x 192.168.5.14; done
