# Copyright (c) 2024 ibis-ssl
# 
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

import paramiko
import threading
import sys
import termios
import tty
import select
import argparse
import time

def send_ctrl_c(channel):
    # Ctrl+Cを送信する
    channel.send('\x03')

def interactive_shell(channel, command):
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        channel.settimeout(0.0)
        
        channel.send(command)

        while True:
            # キーボード入力を読み取る
            if channel.recv_ready():
                x = channel.recv(1024).decode('utf-8')
                if len(x) == 0:
                    break
                sys.stdout.write(x)
                sys.stdout.flush()

            if channel.recv_stderr_ready():
                x = channel.recv_stderr(1024).decode('utf-8')
                if len(x) == 0:
                    break
                sys.stdout.write(x)
                sys.stdout.flush()

            if channel.exit_status_ready():
                break

            # キーボード入力を読み取る
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                x = sys.stdin.read(1)
                if len(x) == 0:
                    break
                if x == '\x03':  # Ctrl+C
                    send_ctrl_c(channel)
                else:
                    channel.send(x)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

def ssh_connect(hostname, port, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=username, password=password)

    channel = client.invoke_shell()
    
    interactive_shell(channel, command)

    channel.close()
    client.close()

if __name__ == "__main__":
    # time.sleep(10)
    parser = argparse.ArgumentParser()
    parser.add_argument('--hostname',type=str, required=True)
    parser.add_argument('--port', type=int, default=22)
    parser.add_argument('--username', type=str, default='ibis')
    parser.add_argument('--password', type=str, default='ibis')
    parser.add_argument('--command', type=str, default="~/Orion_CM4/ai_cmd_v2.out -s 2000000\n")
    args = parser.parse_args()
    hostname = args.hostname
    port = args.port
    username = args.username
    password = args.password
    command = args.command
    ssh_connect(hostname, port, username, password, command)