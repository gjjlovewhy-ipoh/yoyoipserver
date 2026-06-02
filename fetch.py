
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

URL = "https://pan.szfx.top/down.php/1c58c619bf9bf3537671fb9d36d6c453.txt"
WAIT = 8
OUT = "result.txt"

def run():
    opt = Options()
    opt.add_argument("--headless=new")
    opt.add_argument("--no-sandbox")
    opt.add_argument("--disable-dev-shm-usage")
    opt.add_argument("--disable-gpu")

    serv = Service(ChromeDriverManager().install())
    dr = webdriver.Chrome(service=serv, options=opt)
    try:
        dr.get(URL)
        time.sleep(WAIT)
        now_url = dr.current_url
        txt = dr.find_element("tag name", "body").text
        data = f"抓取:{datetime.now()}\n源链接:{URL}\n跳转:{now_url}\n===========\n{txt}"
        with open(OUT,"w",encoding="utf-8") as f:
            f.write(data)
    except Exception as e:
        with open("error.log","w",encoding="utf-8") as f:
            f.write(str(e))
    finally:
        dr.quit()

if __name__ == "__main__":
    run()
