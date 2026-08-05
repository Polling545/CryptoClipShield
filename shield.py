import time
import re
import os
import shutil
from pathlib import Path
import psutil
import pyperclip

# 定义常见加密货币地址的特征正则（例如比特币、以太坊地址）
CRYPTO_PATTERNS = {
    "Bitcoin": r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$",
    "Ethereum": r"^0x[a-fA-F0-9]{40}$"
}

# 定义本地隔离区路径
QUARANTINE_DIR = Path("./quarantine_zone")
QUARANTINE_DIR.mkdir(exist_ok=True)

def check_clipboard():
    """检查剪贴板内容是否被恶意篡改或包含敏感钱包地址"""
    try:
        content = pyperclip.paste()
        for coin, pattern in CRYPTO_PATTERNS.items():
            if re.match(pattern, content):
                print(f"[+] 检测到复制了 {coin} 地址: {content}")
    except Exception as e:
        print(f"[-] 读取剪贴板出错: {e}")

def quarantine_file(file_path):
    """将可疑文件安全隔离到隔离区，等待用户处置"""
    try:
        target_path = QUARANTINE_DIR / Path(file_path).name
        shutil.move(file_path, target_path)
        print(f"[!] 已成功将可疑文件隔离至: {target_path}")
        
        # 互动选择环节
        choice = input("[?] 请选择操作 - 输入 [d] 永久删除，输入 [r] 恢复文件，或直接回车跳过: ").strip().lower()
        if choice == 'd':
            if target_path.exists():
                target_path.unlink()
                print("[-] 文件已被永久销毁。")
        elif choice == 'r':
            original_dir = Path(file_path).parent
            original_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(target_path, file_path)
            print("[+] 文件已恢复至原路径。")
        else:
            print("[*] 文件保持在隔离区中。")
    except Exception as e:
        print(f"[-] 隔离操作失败: {e}")

def monitor_processes():
    """扫描当前运行的进程，寻找可疑或非法的后台程序，并支持对带有关联文件路径的进程进行隔离处理"""
    print("[*] 正在扫描活跃进程...")
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            proc_name = proc.info['name']
            proc_exe = proc.info['exe']
            if proc_name and any(bad_word in proc_name.lower() for bad_word in ['keylog', 'stealer', 'hook']):
                print(f"[!] 警告！发现高可疑进程: {proc_name} (PID: {proc.info['pid']})")
                if proc_exe and os.path.exists(proc_exe):
                    print(f"[!] 正在处理可疑文件源: {proc_exe}")
                    try:
                        p = psutil.Process(proc.info['pid'])
                        p.terminate()  # 先终止进程，防止文件被占用
                        p.wait(timeout=3)
                    except Exception:
                        pass
                    quarantine_file(proc_exe)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    print("=== CryptoClipShield 增强版（带隔离机制）已启动 ===")
    print("正在保护剪贴板并监控后台风险进程...")
    
    try:
        while True:
            check_clipboard()
            monitor_processes()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n[*] 监控已由用户安全停止。")
