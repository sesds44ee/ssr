import threading
import subprocess

def run_file(file):
    subprocess.call(["python3", file])

files = ["bot.py", "while.py"]

for file in files:
    t = threading.Thread(target=run_file, args=(file,))
    t.start()
    print(f"Runing : {file}")