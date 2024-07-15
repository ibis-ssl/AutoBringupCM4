import os
import argparse

if __name__ == "__main__":
    # 現在のスクリプトのディレクトリを取得
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 実行したいPythonスクリプトのパス
    script_to_run = os.path.join(current_dir, "sshConnectAuto.py")
    parser = argparse.ArgumentParser()
    parser.add_argument('--hostnames',type=str,required=True, nargs="*")
    parser.add_argument('--port', type=int, default=22)
    parser.add_argument('--username', type=str, default='ibis')
    parser.add_argument('--password', type=str, default='ibis')
    # parser.add_argument('--command', type=str, default="~/Orion_CM4/ai_cmd_v2.out -s 2000000\n")
    args = parser.parse_args()
    # 新しいターミナルウィンドウの新しいタブでスクリプトを実行
    for hostname in args.hostnames:
        arg_list = [f"--hostname {hostname}", f"--port {args.port}", f"--username {args.username}", f"--password {args.password}"]
        arg_str = " ".join(arg_list)
        ag = ["gnome-terminal", "--tab", "--title", hostname, "--", f"sh -c \'python3 {script_to_run} {arg_str}\'"]
        print(" ".join(ag))
        os.system(" ".join(ag))