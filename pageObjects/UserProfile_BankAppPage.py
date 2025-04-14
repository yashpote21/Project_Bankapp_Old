from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# username = YashTech
# password = YashTech@101

class UserProfile_page:
    # User Registration Page Objects
    link_SignUp_XPATH = "//a[contains(.,' Sign Up')]"
    text_Register_Username_XPATH = "//input[@id='username']"
    text_Register_Password_XPATH = "//input[@id='password']"
    text_Register_Email_XPATH = "//input[@id='email']"
    text_Register_Phone_XPATH = "//input[@id='phone']"
    Btn_CreateUser_XPATH = "//button[@id='createUserButton']"
    Validate_User_Registration_XPATH = "//div[@id='successMessage']"




    # User Login Page Objects
    link_Login_XPATH = "//a[contains(text(),'Login')]"
    text_Login_Username_XPATH = "//input[@name='username']"
    text_Login_Password_XPATH = "//input[@name='password']"
    Btn_Login_XPATH = "//button[@type='submit']"
    Validate_UserLogin_XPATH = "//h2[contains(.,'Dashboard')]"

    def __init__(self, driver):
        self.driver = driver


    # Creating Methods For User Registration.
    def Click_Link_SignUp(self):
        self.driver.find_element(By.XPATH, self.link_SignUp_XPATH).click()

    def Enter_Register_Username(self, register_username):
        self.driver.find_element(By.XPATH, self.text_Register_Username_XPATH).send_keys(register_username)

    def Enter_Register_Password(self, register_password):
        self.driver.find_element(By.XPATH, self.text_Register_Password_XPATH).send_keys(register_password)

    def Enter_Register_Email(self, register_email):
        self.driver.find_element(By.XPATH, self.text_Register_Email_XPATH).send_keys(register_email)

    def Enter_Register_Phone(self, phone):
        self.driver.find_element(By.XPATH, self.text_Register_Phone_XPATH).send_keys(phone)

    def Click_Create_User(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.Btn_CreateUser_XPATH).click()

    def Validate_UserRegister(self):
        try:
            success_msg = self.driver.find_element(By.XPATH, self.Validate_User_Registration_XPATH).text
            return success_msg
        except:
            pass


    # Creating Methods For User Login.
    def Click_Login_Link(self):
        self.driver.find_element(By.XPATH, self.link_Login_XPATH).click()

    def Enter_Username(self, username):
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.NAME, "password")))
        self.driver.find_element(By.XPATH, self.text_Login_Username_XPATH).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.text_Login_Password_XPATH).send_keys(password)

    def Click_LoginButton(self):
        self.driver.find_element(By.XPATH, self.Btn_Login_XPATH).click()

    def Validate_User(self):
        try:
            success_msg = self.driver.find_element(By.XPATH, self.Validate_UserLogin_XPATH).text
            return success_msg
        except:
            pass