import pytest
from selenium import webdriver

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome(options=chrome_option)
    driver.maximize_window()
    driver.get("https://apps.credence.in/")
    yield driver
    driver.quit()


# pytest -v -s --browser chrome --html="HTMLReports\BankApp.html" --alluredir="AllureReports"


def pytest_html_report_title(report):
    report.title = "BankApp Test Cases"
