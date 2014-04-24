import pexpect
import sys

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
