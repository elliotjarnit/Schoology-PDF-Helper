from functions import *


class Login:
    def __init__(self):
        if platform == "darwin":
            ChromeDriver = os.getcwd().replace("/PDFHelper", "") + "/ChromeWebDrivers/chromedriver"
        elif platform == "win32":
            ChromeDriver = os.getcwd().replace("\\PDFHelper", "") + "\ChromeWebDrivers\chromedriver.exe"

        print(ChromeDriver)
        try:
            driver = webdriver.Chrome(ChromeDriver)
        except:
            clear()
            printError("Please update google chrome to latest version")
            time.sleep(5)
            exit()

        driver.get("https://klschools.schoology.com/api")

        try:
            WebDriverWait(driver, 120).until(EC.url_matches("https://klschools.schoology.com/api" or "https://klschools.schoology.com/api#"))
        except:
            printError("Took too long")
            time.sleep(5)
            exit()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "edit-current-key")))
        self.publicKey = driver.find_element_by_id("edit-current-key").get_attribute("value")
        self.secretKey = driver.find_element_by_id("edit-current-secret").get_attribute("value")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='_1SIMq _2kpZl _3OAXJ _13cCs _3_bfp _2M5aC _24avl _3v0y7 _2s0LQ _3ghFm _3LeCL _31GLY _9GDcm _1D8fw util-height-six-3PHnk util-pds-icon-default-2kZM7 Header-header-button-active-state-3AvBm Header-header-button-1EE8Y Z_KgC fjQuT uQOmx']")))
        button1 = driver.find_element_by_xpath("//button[@class='_1SIMq _2kpZl _3OAXJ _13cCs _3_bfp _2M5aC _24avl _3v0y7 _2s0LQ _3ghFm _3LeCL _31GLY _9GDcm _1D8fw util-height-six-3PHnk util-pds-icon-default-2kZM7 Header-header-button-active-state-3AvBm Header-header-button-1EE8Y Z_KgC fjQuT uQOmx']")
        button1.click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Your Profile']")))
        prof_button = driver.find_element_by_xpath("//a[normalize-space()='Your Profile']")
        user_id = prof_button.get_attribute("href")
        self.userID = str(user_id).replace("https://klschools.schoology.com/user/", "").replace("/info", "")
        driver.quit()