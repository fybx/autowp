#!/usr/bin/env python
#
#       Ferit Yiğit BALABAN,        <fybalaban@fybx.dev>
#       send_wp.py                  2023
#
import time
from time import sleep
from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

API_FORMAT = "https://web.whatsapp.com/send?phone={}&text={}"
SLEEP_SECS = 10
ASK_CONFRM = True


def read_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied to read the file: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {file_path}. Error: {e}")
    return ""


def get_targets(targets_file_path: str) -> [str]:
    with open(targets_file_path, "r") as f:
        content = f.readlines()
        f.close()
    return [t.replace("\n", "").strip() for t in content]


def init_browser(options: Options = Options()) -> WebDriver:
    """
    Initializes a browser object with given options class
    :param options:
    :return: Returns the initialized browser object
    """
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get("https://web.whatsapp.com")
    return browser


def main():
    xpath_tb = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span'
    xpath_sb = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]'
    first = True

    message = read_file("message.txt")
    targets = get_targets("targets.txt")
    browser = init_browser()

    # you have 15 seconds to link your device on whatsapp web
    sleep(15)

    message = quote_plus(message)
    waiting = WebDriverWait(browser, SLEEP_SECS)

    start = time.time()
    for target in targets:
        browser.get(API_FORMAT.format(target, message))

        # wait until the message is present in textbox
        textbox = waiting.until(ec.presence_of_element_located((By.XPATH, xpath_tb)), "Textbox was not found")
        if textbox.text != "":
            # get the send button and click on it
            send_button = browser.find_element(By.XPATH, xpath_sb)
            send_button.click()
            print(f"Sent to +{target}")

        if first and ASK_CONFRM:
            print("WARNING: You have to confirm that you want to continue sending messages.")
            print("After accepting, the automation will run until end of targets is reached.")
            ask = input("Want to continue? (y/N): ").strip().lower()
            if ask != "y":
                break
            else:
                first = False

        # sleep as a padding before switching to next target
        sleep(1)

    end = time.time()
    print(f"reporting: over in {(end - start) // 1} secs")


if __name__ == "__main__":
    main()
