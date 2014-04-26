import socket
import time

def is_port_open(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        s.close()
    except:
        return False
    return True

def wait_port_open(host, port, num_of_try=10):
    for i in range(num_of_try):
        if is_port_open(host, port):
            return True
        print "Port %s not open on %s. try" % (port, i)
        time.sleep(5)
    print "Timed out, port is closed"
    return False
