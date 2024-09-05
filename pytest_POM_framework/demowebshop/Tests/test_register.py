# import pytest
#
# from demowebshop.POM.homepage import HomePage
# from demowebshop.POM.registerpage import Register
#
#
# def test_register_with_all_valid_input(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("abhiram" ,"pradeep" , "karma@gmail.com" , "heyraam" , "heyraam")
#     assert driver.find_element("xpath" , "//input[@value='Continue']").is_displayed()
#
#
# def test_register_without_fname(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account(" " ,"pradeep" , "karma@gmail.com" , "heyraam" , "heyraam")
#     assert driver.find_element("xpath" , "//span[@data-valmsg-for='FirstName']").is_displayed()
#
# def test_register_without_lname(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("abhiram" ,"" , "karma@gmail.com" , "heyraam" , "heyraam")
#     assert driver.find_element("xpath" , "//span[@data-valmsg-for='LastName']").is_displayed()
#
# def test_register_without_email(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("abhiram" ,"pradeep" , "" , "heyraam" , "heyraam")
#     assert driver.find_element("xpath" , "//span[@data-valmsg-for='Email']").is_displayed()
#
# def test_register_with_improper_email(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("abhiram" ,"pradeep" , "karma@" , "heyraam" , "heyraam")
#     assert driver.find_element("xpath" , "//span[.='Wrong email']//span").is_displayed()
#
# def test_register_without_passwd(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("abhiram" ,"pradeep" , "karma@gmail.com" , "" , "heyraam")
#     assert driver.find_element("xpath" , "//span[@data-valmsg-for='Password']").is_displayed()
#
