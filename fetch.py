
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

URL = "https://pan.szfx.top/down.php/1c58c619bf9bf3537671fb9d36d6c453.txt"
WAIT_TIME = 8
SAVE_FILE = "result.txt"

def get_html_text():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    # 关闭证书弹窗
    opts.add_argument('--ignore-certificate-errors')

    # 自动下载匹配驱动，解决驱动缺失报错
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)
    try:
        driver.get(URL)
        time.sleep(WAIT_TIME)
        final_url = driver.current_url
        # 获取页面纯文本，保留换行
        page_text = driver.find_element("tag name", "body").text

        content = (
            f"抓取时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"源地址：{URL}\n"
            f"跳转后地址：{final_url}\n"
            "========================================\n"
            f"{page_text}"
        )
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("抓取成功，已保存result.txt")
    except Exception as e:
        with open("error.log", "w", encoding="utf-8") as f:
            f.write(f"{datetime.now()}: {str(e)}")
        print(f"异常：{str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    get_html_text()
