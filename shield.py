import time
import re
import psutil
import pyperclip

# 定义常见加密货币地址的特征正则（例如比特币、以太坊地址）
CRYPTO_PATTERNS = {
    "Bitcoin": r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$",
    "Ethereum": r"^0x[a-fA-F0-9]{40}$"
}

def check_clipboard():
    """检查剪贴板内容是否被恶意篡改或包含敏感钱包地址"""
    try:
        content = pyperclip.paste()
        for coin, pattern in CRYPTO_PATTERNS.items():
            if re.match(pattern, content):
                print(f"[+] 检测到复制了 {coin} 地址: {content}")
    except Exception as e:
        print(f"[-] 读取剪贴板出错: {e}")

def monitor_processes():
    """扫描当前运行的进程，寻找可疑或非法的后台程序"""
    print("[*] 正在扫描活跃进程...")
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            proc_name = proc.info['name']
            if proc_name and any(bad_word in proc_name.lower() for bad_word in ['keylog', 'stealer', 'hook']):
                print(f"[!] 警告！发现高可疑进程: {proc_name} (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    print("=== CryptoClipShield 监控脚本已启动 ===")
    print("正在保护剪贴板并监控后台风险进程...")
    
    try:
        while True:
            check_clipboard()
            monitor_processes()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n[*] 监控已由用户安全停止。")
