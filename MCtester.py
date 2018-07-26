import socket
import struct
import sys
import signal
import argparse
import time

DEFAULT_IP_ADDRESS="239.254.0.1"
DEFAULT_PORT=5005
DEFAULT_MESSAGE="Hello World!"
DEFAULT_MESSAGE_INTERVAL=1
OPER_MODE_SERVER="SERVER"
OPER_MODE_CLIENT="CLIENT"




def signal_handler(signal, frame):
    conf.operation_status = False
    print("\nStopping multicast tester. Thanks for using.")
    print("Please visit https://github.com/timgold81/")
    print("contact timgold@gmail.com\n")
    sys.exit(-1)

def parse_args():
    parser = argparse.ArgumentParser(description="Software to test multicast connection. Will send or listen\
 to message sent in loop until CTRL+C is pressed ")
    parser.add_argument("-s","--server", help="Start as a server.",action="store_true")
    parser.add_argument("-c","--client", help="Start as a client.", action="store_true")
    parser.add_argument("-i","--ip", help="IP address as a multicast address.Default="+DEFAULT_IP_ADDRESS)
    parser.add_argument("-p","--port", help="Port for multicast. Default="+str(DEFAULT_PORT))
    parser.add_argument("-m","--message", help="Message to send. Default='"+DEFAULT_MESSAGE+"'")
    parser.add_argument("-n","--interval",help="Interval to send message. Ignored if run as a client. Default="+str(DEFAULT_MESSAGE_INTERVAL)+" sec")
    args=parser.parse_args()

    if (args.server and args.client):
        print("Cannot act as a client and as a server")
        return -1
    if (not args.server and not args.client):
        print ("Need to be eather client or server. Try --help to see options")
        return -1
    if (args.server):
        conf.oper_mode=OPER_MODE_SERVER
    if (args.client):
        conf.oper_mode=OPER_MODE_CLIENT
    if (args.interval):
        conf.interval=int(args.interval)
    if (args.message):
        conf.msg=args.message

    return 1

class configuration:
    operation_status=True
    ip_address=""
    port=0
    msg=""
    oper_mode=""
    interval=0
    def __init__(self):
        self.operation_status=True
        self.ip_address=DEFAULT_IP_ADDRESS
        self.port=DEFAULT_PORT
        self.msg="Hello World!"
        self.interval=DEFAULT_MESSAGE_INTERVAL

    def print_params(self):
        print("operation status:"+str(self.operation_status))
        print ("ip address:"+self.ip_address)
        print ("port: "+str(self.port))
        print ("message:"+self.msg)
        print ("operation mode:"+self.oper_mode)
        print ("interval:"+str(self.interval))


def main():
    global conf
    conf = configuration()

    if (parse_args()==1):
        if (conf.oper_mode==OPER_MODE_CLIENT):
            print("Starting in client mode")

            mc_group = conf.ip_address
            srv_addr = ('', conf.port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(srv_addr)

            group = socket.inet_aton(mc_group)
            mreq = struct.pack('4sL', group, socket.INADDR_ANY)
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

            while (conf.operation_status):
                print("Waiting for message", end="\r")
                data, address = sock.recvfrom(1024)

                print("                              ", end="\r")
                print ("recieved %s bytes from %s " %(len(data),address)+" "+str(data))

                time.sleep(1)


        elif (conf.oper_mode==OPER_MODE_SERVER):
            print("Staring in server mode")
            sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            sock.settimeout(0.2)
            ttl=struct.pack('b',64)
            sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,ttl)
            mc_group=(conf.ip_address,conf.port)
            i=0
            while (conf.operation_status):
                try:
                    sent=sock.sendto(conf.msg.encode(),mc_group)
                except:
                    print ("Error sending")
                print("                  " , end="\r")
                print ("Sending message "+str(i)+" ",end="\r")
                i=i+1
                time.sleep(conf.interval)



    else:
        print ("Parameters error")
        sys.exit (-1)




if __name__=="__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
