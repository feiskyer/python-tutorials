#!/usr/bin/env python
import pexpect

def ssh_cmd(ip, user, passwd, cmd):
	ssh = pexpect.spawn('ssh -p 58422 %s@%s "%s"' %(user, ip, cmd))
	r = ''
	try:
		i = ssh.expect(["root@%s's password:" % ip,
				'Are you sure you want to continue connecting (yes/no)?'])
		if i == 0:
			ssh.sendline(passwd)
		elif i==1:
			ssh.sendline('yes')
	except pexpect.EOF:
		ssh.close()
	else:
		r = ssh.read()
		ssh.expect(pexpect.EOF)
		ssh.close()
	return r

user = "root"
ip = '192.168.0.0.1'
passwd = 'password'
cmd = "uptime;ls -l /"

if __name__ == '__main__':
	print ssh_cmd(ip, user, passwd, cmd)

