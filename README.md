Playing around with Scapy. This program discovers devices in your subnet by sending an ARP broadcast.

Example usage: `sudo python3.6 ./discover.py 192.168.1.1/24`

Example output:
```
   IP                    MAC                HOSTNAME
192.168.1.4         51:00:80:f3:12:78       Bobs Desktop
192.168.1.43        20:68:b1:80:cc:90       Bobs iPhone
192.168.1.187       2e:2c:52:0d:32:dd       Alices Desktop
```
