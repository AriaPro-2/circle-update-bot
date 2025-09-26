from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# 設定項目
url = "https://mypage.hubcnavi.net/auth/f56f1eb452104960b93f/S0lVcro9HcaeSZ81KqvKoeESg2oNh8ktJJzfAy0vAARXNWVX1PiPC?fw=edit"
mainarticle_base = "ここが紹介文です。"  # 紹介文ベース（適宜変更）
pattern_a = mainarticle_base + " "  # 空白1つ追加
pattern_b = mainarticle_base        # 空白なし

# GitHub Secrets からログイン情報を取得
LOGIN_ID = os.getenv("LOGIN_ID")
LOGIN_PW = os.getenv("LOGIN_PW")

# Headless Chrome の設定
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

def update_mainarticle(text):
    driver.get(url)
    time.sleep(3)

    # ログイン処理（必要な場合のみ）
    if LOGIN_ID and LOGIN_PW:
        try:
            driver.find_element(By.NAME, "id").send_keys(LOGIN_ID)
            driver.find_element(By.NAME, "pw").send_keys(LOGIN_PW)
            driver.find_element(By.NAME, "login").click()
            time.sleep(2)
        except Exception as e:
            print("ログイン失敗:", e)

    # 紹介文の更新処理
    try:
        text_area = driver.find_element(By.NAME, "mainarticle")
        text_area.clear()
        text_area.send_keys(text)

        save_button = driver.find_element(By.XPATH, "//button[contains(.,'保存')]")
        save_button.click()
        print(f"紹介文を更新: {text}")
    except Exception as e:
        print("更新失敗:", e)

try:
    update_mainarticle(pattern_a)
    time.sleep(5)
    update_mainarticle(pattern_b)
except KeyboardInterrupt:
    print("停止しました")
finally:
    driver.quit()
