import pytest
import openpyxl
from demowebshop.POM.homepage import HomePage
from demowebshop.POM.loginpage import LogIn
from utilities.excel_reader import get_list_from_excel

# usernames=["reddyvinuth27@gmail.com","abc@gmail.com","xyz@gmail.com","mno@gmail.com"]
# usernames=[("reddyvinuth27@gmail.com","selenium"),("abc@gmail.com","1234"),("xyz@gmail.com","1123"),("mno@gmail.com","1234567")]


credentials = get_list_from_excel()

@pytest.mark.parametrize("username,password",credentials)
def test_login_with_proper_credentials(driver,username,password):
    
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application(username, password)
    assert driver.find_element("xpath", f"//a[.='{username}']").is_displayed()

@pytest.mark.skip
def test_login_with_no_password(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("reddyvinuth27@gmail.com", "")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()

@pytest.mark.skip
def test_login_with_no_username(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("", "selenium")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()

@pytest.mark.skip
def test_login_with_no_credntials(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("", "")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()

@pytest.mark.skip
def test_login_with_invalid_credntials(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("abc@gmail.com", "wastejava")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()