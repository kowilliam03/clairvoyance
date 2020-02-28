import requests


def sendLineNotify(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {"message": msg}
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=payload)

    if r.status_code == 401:
        print("Invalid access token")
    if r.status_code == 500:
        print("Failure due to server error")
