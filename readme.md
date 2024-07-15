# 環境構築
```sh
git clone https://github.com/ibis-ssl/AutoBringupCM4.git
cd AutoBringupCM4
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

# 実行
```sh
python3 sshConnectAuto.py --hostname "192.168.20.101" 
```

## コマンドライン引数
```python
parser.add_argument('--hostname',type=str, required=True)
parser.add_argument('--port', type=int, default=22)
parser.add_argument('--username', type=str, default='ibis')
parser.add_argument('--password', type=str, default='ibis')
parser.add_argument('--command', type=str, default="~/Orion_CM4/ai_cmd_v2.out -s 2000000\n")
```