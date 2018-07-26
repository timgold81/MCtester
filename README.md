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

<pre>
