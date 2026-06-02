from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

# 配置
URL = "https://pan.szfx.top/down.php/1c58c619bf9bf3537671fb9d36d6c453.txt"
WAIT_TIME = 8  # 等待跳转秒数5~10，这里8秒
SAVE_FILE = "result.txt"

def get_html_text():
    opts = Options()
    # 云端无头必备参数
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=opts)
    try:
        driver.get(URL)
        time.sleep(WAIT_TIME)
        final_url = driver.current_url
        # 获取页面全部文本（页面可见文本，保留换行格式）
        text = driver.find_element("tag name", "body").text

        content = (
            f"抓取时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"源地址：{URL}\n"
            f"跳转后地址：{final_url}\n"
            "========================================\n"
            f"{text}"
        )
        # 写入本地文件（云端容器内的文件，之后actions自动提交入库）
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("抓取完成，已写入result.txt")
    except Exception as e:
        with open("error.log", "w", encoding="utf-8") as f:
            f.write(f"{datetime.now()}:{str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    get_html_text()
