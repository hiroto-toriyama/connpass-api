import requests
import sys
from datetime import date, datetime, timezone, timedelta
import json
import os

def get_connpass_json(ymd: str, count: int = 100, order: int = 2):
    url = "https://connpass.com/api/v1/event/"
    url += "?ymd="+ymd+"&count="+str(count)+"&order="+str(order)
    print(url)

    response = requests.get(url)
    json_data = response.json()

    return json_data


def main():
    JST = timezone(timedelta(hours=+9))
    ymd_today = datetime.now(JST)

    dir_build = 'build/v1/'
    os.makedirs(dir_build, exist_ok=True)

    dir_events = dir_build + 'events/'    
    os.makedirs(dir_events, exist_ok=True)
    for i in range(7):
        dir_day = dir_events + f'{i}/'
        os.makedirs(dir_day, exist_ok=True)
        ymd = ymd_today + timedelta(days=float(i))
        ymd_str = ymd.isoformat().split("T")[0].replace("-", "")
        json_data = get_connpass_json(ymd_str)
        with open(f'{dir_day}/index.html', 'w', encoding="UTF-8") as f:
            json.dump(json_data, f, ensure_ascii=False)    


if __name__ == "__main__":
    main()