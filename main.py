from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from data import *
from time import sleep


def main():
    # setting necessary options
    options = ChromeOptions()
    # options.add_argument("--headless=new")  # comment if you want to use gui version of chrome
    driver = webdriver.Chrome(options=options) # I have used chrome web driver, you can use any driver you want.
    driver.maximize_window()
    driver.implicitly_wait(2)    

    # the loop is used to repeat the action by big range of accounts
    for key in accounts:
        # opening instagram.com login page
        driver.get("https://instagram.com/")

        # preparing account details buttons
        login, passwd = driver.find_elements(by=By.TAG_NAME, value="input")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
            
        # sending username and password the the necessary fields
        login.send_keys(key)
        passwd.send_keys(accounts[key])
        submit_button.click()
        
        # loggin in to an account
        try:
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="x9f619 x3nfvp2 xr9ek0c xjpr12u xo237n4 x6pnmvc x7nr27j x12dmmrz xz9dl7a xn6708d xsag5q8 x1ye3gou x80pfx3 x159b3zp x1dn74xm xif99yt x172qv1o x10djquj x1lhsz42 xzauu7c xdoji71 x1dejxi8 x9k3k5o xs3sg5q x11hdxyr x12ldp4w x1wj20lx x1lq5wgf xgqcy7u x30kzoy x9jhf4c"]')))
        except TimeoutException:
            print("\tTimed out while logging in")
            print(f"Username: {key}, password: {accounts[key]}")
            continue

        driver.get("https://instagram.com/"+target_user)

        # selection the options button
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'svg[aria-label="Options"]')))
        except TimeoutException:
            print("\tTimed out while opening target account")
            print(f"Username: {key}, password: {accounts[key]}")
            print(f"Target: ", target_user)
            exit(1)
        opt = driver.find_element(by=By.CSS_SELECTOR, value='svg[aria-label="Options"]')
        opt.click()

        # selecting the report button from options
        try:
            report_btn = driver.find_elements(by=By.CSS_SELECTOR, value="._a9--._ap36._a9-_")[2]
        except NoSuchElementException:
            print("\tCould not access the report button in options")
            exit(1)
        report_btn.click()

        # selecting "report account"
        try:
            report_account_btn = driver.find_elements(by=By.CSS_SELECTOR, value="._abn2")[1]
        except NoSuchElementException:
            print("\tCould not access the report account button")
            exit(1)
        report_account_btn.click()
        sleep(2)

        # selecting "pretending someone" option button
        pretending_sm_btn = driver.find_elements(by=By.CSS_SELECTOR, value="button._abn2")
        pretending_sm_btn[1].click()
        sleep(2)

        # selecting "pretending me" option button
        pretending_me = driver.find_elements(by=By.CSS_SELECTOR, value="span.x17adc0v")
        pretending_me[0].click()
        
        # focusing on floating the window to select necessary elements
        layer = driver.find_element(by=By.CSS_SELECTOR, value="div[class='x1qjc9v5 x9f619 x78zum5 xdt5ytf x1iyjqo2 xl56j7k']")
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(layer).perform()
        driver.switch_to.active_element
        
        # last part, submitting the report
        submit_btn = driver.find_element(by=By.CSS_SELECTOR, value="button._acan._acap._acas._aj1-._ap30")
        submit_btn.send_keys(Keys.ENTER)
        print("Reported")
        driver.quit()

main()