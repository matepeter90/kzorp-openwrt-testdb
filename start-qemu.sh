#!/bin/bash

sudo qemu-system-mips -kernel bin/malta/openwrt-malta-be-vmlinux.elf -nographic -m 64 -no-reboot -net nic -net tap
