# MCtester
Multicast client and server for easy testing of multicast traffic
<pre>
usage: MCtester.exe [-h] [-s] [-c] [-i IP] [-p PORT] [-m MESSAGE]
                    [-n INTERVAL]

Software to test multicast connection. Will send or listen to message sent in
loop until CTRL+C is pressed

optional arguments:
  -h, --help            show this help message and exit
  -s, --server          Start as a server.
  -c, --client          Start as a client.
  -i IP, --ip IP        IP address as a multicast address.Default=239.254.0.1
  -p PORT, --port PORT  Port for multicast. Default=5005
  -m MESSAGE, --message MESSAGE
                        Message to send. Default='Hello World!'
  -n INTERVAL, --interval INTERVAL
                        Interval to send message. Ignored if run as a client.
                        Default=1 sec

</pre>

The binary was compiled using pyinstaller<BR><BR>

#Example
Download from the dist folder the windows executable. Activate two "cmd" windows. Write in one 'MCtester.exe -s -m "Multicast tester"', and in the other 'MCtester.exe -c'
<BR>
'MCtester.exe -s -m "Multicast tester"' output:
<pre>
python.exe MCtester.py -s -m "Multicast tester"
Staring in server mode
Sending message 4
Stopping multicast tester. Thanks for using.
Please visit https://github.com/timgold81/
contact timgold@gmail.com
</pre>
'MCtester.exe -c' output:
<pre>
C:\Users\timg\Documents\Py\MCtester>python MCtester.py -c
Starting in client mode
recieved 16 bytes from ('172.18.110.27', 49745)  b'Multicast tester'
recieved 16 bytes from ('172.18.110.27', 49745)  b'Multicast tester'
recieved 16 bytes from ('172.18.110.27', 49745)  b'Multicast tester'
recieved 16 bytes from ('172.18.110.27', 49745)  b'Multicast tester'
Waiting for message
Stopping multicast tester. Thanks for using.
Please visit https://github.com/timgold81/
contact timgold@gmail.com
</pre>