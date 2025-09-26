from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ★設定項目
url = "https://mypage.hubcnavi.net/auth/f56f1eb452104960b93f/S0lVcro9HcaeSZ81KqvKoeESg2oNh8ktJJzfAy0vAARXNWVX1PiPC?fw=edit"
mainarticle_base = "ここが紹介文です。"  # 紹介文ベース（適宜変更）
pattern_a = mainarticle_base + " "  # 空白1つ追加
pattern_b = mainarticle_base        # 空白なし
interval_sec = 5 * 60               # 5分間隔

# ★ログインが必要ならここにID, PWを記載（未記入時はスキップ）
LOGIN_ID = None
LOGIN_PW = None

# Selenium WebDriverの初期化
driver = webdriver.Chrome()

def update_mainarticle(text):
    driver.get(url)
    time.sleep(3) # ページ読み込み待ち
    
    # ログイン処理（必要な場合のみ）
    if LOGIN_ID and LOGIN_PW:
        # 例： driver.find_element(By.NAME, "id").send_keys(LOGIN_ID)
        # 例： driver.find_element(By.NAME, "pw").send_keys(LOGIN_PW)
        # 例： driver.find_element(By.NAME, "login").click()
        time.sleep(2)
    
    # 紹介文 本文を書き換え
    text_area = driver.find_element(By.NAME, "mainarticle")
    text_area.clear()
    text_area.send_keys(text)

    # 保存ボタンを探してクリック（仮ID：'save_button'。実際のIDやclass、xpathに適宜変更）
    try:
        # 例: driver.find_element(By.ID, "save_button").click()
        # 下記は「保存」ボタンがtextの場合の例
        save_button = driver.find_element(By.XPATH, "//button[contains(.,'保存')]")
        save_button.click()
    except Exception as e:
        print("保存ボタンが見つかりません:", e)
    print(f"紹介文を更新: {text}")

try:
    while True:
        update_mainarticle(pattern_a)
        time.sleep(interval_sec)
        update_mainarticle(pattern_b)
        time.sleep(interval_sec)
except KeyboardInterrupt:
    print("停止しました")
finally:
