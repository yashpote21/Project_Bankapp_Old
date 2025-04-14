import allure
import pytest
from allure_commons.types import AttachmentType
from pageObjects.UserProfile_BankAppPage import UserProfile_page
from utilities.logger import Log_Class
from utilities.readProperties import ReadConfigFileData
# import FullPageScreenshot

class Test_BankApp_UserProfile:


    Username = ReadConfigFileData.GetLoginUsername()
    Password = ReadConfigFileData.GetLoginPassword()

    # regUsername = ReadConfigFileData.GetRegUsername()
    # regPassword = ReadConfigFileData.GetRegPassword()
    # regEmail = ReadConfigFileData.GetRegEmail()
    # regPhone = ReadConfigFileData.GetRegPhone()

    Log = Log_Class.log_generator()

    @pytest.mark.Sanity
    def test_Check_URL(self, setup):
        self.Log.info("test_Check_URL test case started")
        self.Log.info("Opening browser")
        self.driver = setup

        self.Log.info("Verifying URL")
        if self.driver.title == "Bank Application1":
            self.Log.info("URL launch On correct page")
            self.Log.info("test_Check_URL test case successfully Passed")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), "test_Check_URL_Fail", attachment_type=AttachmentType.PNG)
            self.Log.info("URL launch On incorrect page")
            self.Log.info("test_Check_URL test case Failed")
            self.Log.info("test_Check_URL test case Execution Completed\n")
            assert False
        self.Log.info("test_Check_URL test case Execution Completed\n")



    @pytest.mark.Sanity
    def test_BankApp_Register(self, setup):
        self.Log.info("test_BankApp_Register test case started")
        self.Log.info("Opening browser")
        self.driver = setup
        self.up = UserProfile_page(self.driver)
        self.Log.info("Clicking on Sign Up link")
        self.up.Click_Link_SignUp()
        self.Log.info(f"Entering Username:- {Generate_Random_Username()}")
        self.up.Enter_Register_Username(Generate_Random_Username())
        self.Log.info(f"Entering Password:- {Generate_Random_Password()}")
        self.up.Enter_Register_Password(Generate_Random_Password())
        self.Log.info(f"Entering Email:- {Genarate_Random_Email()}")
        self.up.Enter_Register_Email(Genarate_Random_Email())
        self.Log.info(f"Entering Phone number:- {Generate_Random_Phone_Number()}")
        self.up.Enter_Register_Phone(Generate_Random_Phone_Number())
        # time.sleep(5)
        self.Log.info("Click On Create User button")
        self.up.Click_Create_User()
#         time.sleep(5)
        self.Log.info("Verifying User Registration")
        if self.up.Validate_UserRegister() == "User created successfully1":
            self.Log.info("User Successfully Registered")
            self.Log.info("test_BankApp_Register test case successfully Passed")
            assert True
        else:
            self.Log.info("User Not Registered")
            self.driver.save_screenshot("D:\CT#19_Repeat\Automation Practices\Project_BankApp\Screenshots\Registration_Fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), "test_BankApp_Register_Fail", attachment_type=AttachmentType.PNG)
            self.Log.info("test_BankApp_Register test case Failed")
            self.Log.info("test_BankApp_Register test case Execution Completed\n")
            assert False
        self.Log.info("test_BankApp_Register test case Execution Completed\n")



    @pytest.mark.Sanity
    def test_BankApp_Login(self, setup):
        self.Log.info("test_BankApp_Login test case started")
        self.Log.info("Opening browser")
        self.driver = setup
        self.lp = UserProfile_page(self.driver)
        self.Log.info("Click on Login link")
        self.lp.Click_Login_Link()
        self.Log.info(f"Entering Username:- {self.Username}")
        self.lp.Enter_Username(self.Username)
        self.Log.info(f"Entering Password:- {self.Password}")
        self.lp.Enter_Password(self.Password)
        self.Log.info("Click on Login button")
        self.lp.Click_LoginButton()
        self.Log.info("Verifying User Login")
        if self.lp.Validate_User() == "Dashboard1":
            self.Log.info("User Successfully logged in")
            self.Log.info("test_BankApp_Login test case successfully Passed")
            assert True
        else:
            self.driver.save_screenshot("D:\CT#19_Repeat\Automation Practices\Project_BankApp\Screenshots\Login_Fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), "test_BankApp_Login_Fail", attachment_type=AttachmentType.PNG)
            self.Log.info("User Not logged in")
            self.Log.info("test_BankApp_Login test case Failed")
            self.Log.info("test_BankApp_Login test case Execution Completed\n")
            assert False
        self.Log.info("test_BankApp_Login test case Execution Completed\n")



import random
import string

def Generate_Random_Username(length = 6):
    return 'User' + ''.join(random.choices(string.ascii_letters + string.digits, k = length))


def Generate_Random_Password(attach = '@123'):
    return Generate_Random_Username() + attach


def Genarate_Random_Email(domain = 'example.com'):
    return Generate_Random_Username() + '@' + domain


def Generate_Random_Phone_Number():
    return ''.join(random.choices(string.digits, k = 10))
