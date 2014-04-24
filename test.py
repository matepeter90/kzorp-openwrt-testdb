import pexpect
import sys

exit_code = 0

child = pexpect.spawn('qemu-system-mips -kernel bin/malta/openwrt-malta-be-vmlinux.elf -nographic -m 64 -no-reboot')

#wait for boot
child.timeout=40
child.logfile = sys.stdout

prompt = child.compile_pattern_list('root@.*:/#.*')
regexp = child.compile_pattern_list('.*entered forwarding state.*')

for x in range(2):
    child.expect(regexp)

child.sendline()
child.expect(prompt)
child.sendline("date")

child.expect(prompt)
child.sendline("kzorp -d")
try:
    child.expect(prompt)
    if child.before == '':
        pass
    else:
        print 'kzorp -d did not return empty, returned %s' % child.before
        exit_code = 1
except pexpect.TIMEOUT:
        print 'kzorp -d timed out' 
        exit_code = 1
        pass
sys.exit(exit_code)
