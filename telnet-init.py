import pexpect
import sys
from utils import wait_port_open

wait_port_open('192.168.1.1', 23)
child = pexpect.spawn('telnet 192.168.1.1 23')

#wait for boot
child.timeout=40
child.logfile = sys.stdout

prompt = child.compile_pattern_list('root@.*:/#.*')
regexp = child.compile_pattern_list('.*entered forwarding state.*')

child.expect(prompt)
child.sendline("passwd")

child.expect('New password: ')
child.sendline("secret")

child.expect('Retype password: ')
child.sendline("secret")

child.expect(prompt)
child.sendline("exit")

if wait_port_open('192.168.1.1', 22, num_of_try=24):
    print 'SSH is ready'

