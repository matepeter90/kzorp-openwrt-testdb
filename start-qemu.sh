#!/bin/bash

sudo qemu-system-mips -kernel bin/malta/openwrt-malta-be-vmlinux.elf -nographic -m 64 -no-reboot -net nic,vlan=0 -net tap,vlan=0,script=qemu-ifup.tap0 -net nic,vlan=1 -net tap,vlan=1,script=qemu-ifup.tap1 &
