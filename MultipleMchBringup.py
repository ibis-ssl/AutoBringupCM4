import argparse
import os

if __name__ == "__main__":
    # 現在のスクリプトのディレクトリを取得
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 実行したいPythonスクリプトのパス
    script_to_run = os.path.join(current_dir, "sshConnectAutoWrapper.py")

    parser = argparse.ArgumentParser()
    parser.add_argument('--hostnames',type=str,required=True, nargs="*")
    parser.add_argument('--port', type=int, default=22)
    parser.add_argument('--username', type=str, default='ibis')
    parser.add_argument('--password', type=str, default='ibis')
    # parser.add_argument('--command', type=str, default="~/Orion_CM4/ai_cmd_v2.out -s 2000000\n")
    args = parser.parse_args()
    arg_list = [f"--hostnames {' '.join(args.hostnames)}", f"--port {args.port}", f"--username {args.username}", f"--password {args.password}"]
    arg_str = " ".join(arg_list)
    ag = ["gnome-terminal", "--", f"sh -c \'python3 {script_to_run} {arg_str}\'"]
    print(" ".join(ag))
    os.system(" ".join(ag))
    os.system()