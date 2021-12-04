import os
from os.path import join, dirname, exists
import requests
from typing import List

# Get your input automatically!
def get_input(date: int) -> List[str]:
    script_dir = dirname(__file__)
    data_dir = join(script_dir, "data")
    os.makedirs("data", exist_ok=True)

    script_path = join(data_dir, f"{date}.in")
    if exists(script_path):
        return open(script_path, "r").read().split("\n")
    
    try:
        cookies_dict = {"session": open("cookie.txt").read()}
    except:
        print("cookie.txt does not exist!")
    response = requests.get(
        f"https://adventofcode.com/2021/day/{date}/input", cookies=cookies_dict
    )
    
    data = response.content.decode().strip()
    with open(script_path, 'w') as f:
        f.write(data)
    
    return data.split('\n')