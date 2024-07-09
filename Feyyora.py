import os
import sys
import time
from fuzzywuzzy import fuzz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khai báo các biến màu sắc
yellow = "\033[0;33m"
maufullxduong = "\033[1;47;34m"
maufulldo = "\033[1;47;31m"
end = "\033[0m"
whiteb = "\033[1;37m"
ress = "\033[0;32m"
res = "\033[0;33m"
red = "\033[0;31m"
green = "\033[0;37m"
yellow = "\033[0;33m"
white = "\033[0;33m"
Bxnhac = "\033[1;96m"
den = "\033[1;90m"
do = "\033[1;91m"
luc = "\033[1;92m"
vang = "\033[1;93m"
xduong = "\033[1;94m"
hong = "\033[1;95m"
trang = "\033[1;97m"
nenden = "\033[40m"
xanhd = "\033[0;36m"
nendo = "\033[41m"
nenxanh = "\033[42m"
nenvang = "\033[43m"
nenblue = "\033[44m"
nenPurpe = "\033[45m"
nenCyan = "\033[46m"
nentrang = "\033[47m"
UGreen = "\033[4;32m"
BGreen = "\033[1;32m"
maufullluc = "\033[1;47;32m"
maufullxnhac = "\033[1;47;36m"
maufullden = "\033[1;47;30m"
maufullvang = "\033[1;47;33m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = "\033[1;35m"
xnhac = "\033[1;36m"
trang = "\033[1;37m"
hong = "\033[1;95m"
trang = "\033[1;97m"
ress = "\033[0;32m"
res = "\033[0;33m"
red = "\033[0;31m"
green = "\033[0;37m"
nau = "\033[38;5;94m"
white = "\033[0;33m"
res = "\033[0m"
red = "\033[1;31m"
white = "\033[1;37m"
whiteb = "\033[1;37m"
redb = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cam = "\033[1;33m"
test = "\033[1;33m"
greenb = "\033[1;32m"
lam = "\033[1;34m"
tmi = "\033[1;34m"
hong = "\033[1;35m"
imt = "\033[1;35m"
cyan = "\033[1;36m"
syan = "\033[1;36m"
xnhac = "\033[1;96m"
den = "\033[1;90m"
do = "\033[1;91m"
luc = "\033[1;92m"
vang = "\033[1;93m"
xduong = "\033[1;94m"
hong = "\033[1;95m"
trang = "\033[1;97m"
vang = "\033[1;93m"
do = "\033[1;91m"
BBlack = "\033[1;30m"
BRed = "\033[1;31m"
BGreen = "\033[1;32m"
BYellow = "\033[1;33m"
BBlue = "\033[1;34m"
BPurple = "\033[1;35m"
BCyan = "\033[1;36m"
BWhite = "\033[1;37m"
lime = "\033[1;32m"
red = "\033[1;31m"
xanh = "\033[1;32m"
cyan = "\033[1;36m"
yellow = "\033[1;33m"
turquoise = "\033[1;34m"
maugi = "\033[1;35m"
white = "\033[1;37m"
BCyan = "\033[1;36m"
trang = "\033[1;37m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
luc = "\033[1;92m"
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"

class Earn_PEPE:
    def __init__(self, MAIL, PASS) -> None:
        self.MAIL = MAIL
        self.PASS = PASS
        self.COUNT = 1

        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--lang=en-US')
        options.add_argument('--log-level=0')
        options.add_argument('--log-level=1')
        options.add_argument('--log-level=2')
        options.add_argument('--log-level=3')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-first-run')
        options.add_argument("--disable-webgl")
        options.add_argument('--disable-logging')
        options.add_argument('--disable-infobars')
        options.add_extension('./giaicaptcha.crx')
        options.add_argument('--disable-dev-tools')
        options.add_argument('--no-service-autorun')
        # options.add_argument('--disable-extensions')
        options.add_argument('--disable-web-security')
        options.add_argument('--password-store=basic')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-notifications')
        options.add_argument('--device-scale-factor=1')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-plugins-discovery')
        options.add_argument('--disable-gpu-shader-disk-cache')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--disable-browser-side-navigation')
        options.add_argument('--enable-main-frame-before-activation')
        options.add_argument('--display-capture-permissions-policy-allowed')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        prefs = {
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False,
            'profile.default_content_setting_values.notifications': 2,
            'download_restrictions': 3
        }

        options.add_experimental_option('prefs', prefs)
        options.add_experimental_option('detach', True)
        options.add_experimental_option('useAutomationExtension', False)

        sevices = Service('./chromedriver.exe')
        self.driver = webdriver.Chrome(service=sevices, options=options)

    def Login(self):
        try:
            self.driver.get('chrome://newtab')
            self.driver.execute_script('window.open("https://feyorra.site/member/faucet", "_blank")')
            print(f'{do}[ {vang}KhoaTool {do}] {trang}</> {green}Bắt Đầu Khởi Động', end='\r')
            time.sleep(15)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.execute_script('window.open("https://feyorra.site/login", "_blank")')
            print(f'{do}[ {vang}KhoaTool {do}] {trang}</> {green}Bắt Đầu Đăng Nhập', end='\r')
            time.sleep(10)
            self.driver.switch_to.window(self.driver.window_handles[2])
            NHAPMAIL = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@type="email"]'))
            )
            NHAPMAIL.send_keys(self.MAIL)

            NHAPPASS = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]'))
            )
            NHAPPASS.send_keys(self.PASS)

            SIGNIN = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[@id="loginBtnText"]'))
            )
            SIGNIN.click()

            CHECKLOGIN = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="toast-message"]'))
            ).text

            if CHECKLOGIN == 'Login Success! Redirect to member area in 3 seconds.':
                print(f'{do}[ {vang}KhoaTool {do}] {trang}</> {green}Đăng Nhập Thành Công...', end='\r')
            elif CHECKLOGIN == 'Invalid Captcha':
                self.driver.switch_to.window(self.driver.window_handles[2])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.close()
                print(f'{do}[ {vang}KhoaTool {do}] {trang}</> {green}Giải Captcha Không Thành Công...')
            elif CHECKLOGIN == 'Wrong email or password.':
                self.driver.switch_to.window(self.driver.window_handles[2])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.close()
                print(f'{do}[ {vang}KhoaTool {do}] {trang}</> {green}Nhập Sai Tài Khoản Hoặc Mật Khẩu...')
            else:
                self.driver.switch_to.window(self.driver.window_handles[2])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.close()
                print(f'{do}[ {vang}KhoaTool {do}] {trang}</> {green}Lỗi Gì Đó Hãy Thử Lại !!!')
        finally:
            try:
                self.driver.switch_to.window(self.driver.window_handles[2])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.get('https://feyorra.site/member/faucet')
                self.driver.implicitly_wait(10)
                while True:
                    self.CAPTCHA()
            except:
                pass

    def CAPTCHA(self):
        try:
            CAPTCHAGOC = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@id="captcha-container"]/div[position()=1]'))
            ).get_attribute('class')

            CAPTCHA1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@id="icon-options"]/i[position()=1]'))
            ).get_attribute('class')

            CAPTCHA2 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@id="icon-options"]/i[position()=2]'))
            ).get_attribute('class')

            CAPTCHA3 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@id="icon-options"]/i[position()=3]'))
            ).get_attribute('class')

            CAPTCHA4 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@id="icon-options"]/i[position()=4]'))
            ).get_attribute('class')

            # Định dạng chuỗi captcha
            CLASS_LIST = [CAPTCHA1, CAPTCHA2, CAPTCHA3, CAPTCHA4]

            if not all(CLASS_LIST):
                raise ValueError("Không thể lấy thuộc tính văn bản từ các phần tử captcha")

            # Tìm chuỗi giống nhất bằng thư viện fuzzywuzzy
            STRING = max(CLASS_LIST, key=lambda x: fuzz.ratio(CAPTCHAGOC, x))

            CLICKCAPTCHA = self.driver.find_element(By.XPATH, '//*[contains(@class, "' + STRING + '")]')
            CLICKCAPTCHA.click()

            time.sleep(1)
            CHECK = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@id="captcha-container"]'))
            ).text

            if 'Verified!' in CHECK:
                CLAIM_BUTTON = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]'))
                )
                CLAIM_BUTTON = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
                )
                CLAIM_BUTTON.click()

                CHECKTBAO = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[@class="toast-message"]'))
                ).text

                print(f'{do}[ {vang}KhoaTool {do}] {trang}[{self.COUNT}] {green}{CHECKTBAO}')
                self.COUNT += 1
            else:
                self.driver.refresh()

        except:
            self.driver.refresh()

def main():
    try:
        os.system("cls" if os.name == "nt" else "clear")
        MAIL = str(input(f'{green}Nhập Email: {trang}'))
        PASS = str(input(f'{green}Nhập Password: {trang}'))

        os.system("cls" if os.name == "nt" else "clear")
        Chrome = Earn_PEPE(MAIL, PASS)
        Chrome.Login()

    except:
        pass


if __name__=='__main__':
    try:
        main()
    except:
        pass