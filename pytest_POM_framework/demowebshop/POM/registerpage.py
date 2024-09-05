from demowebshop.POM.homepage import HomePage
class Register(HomePage):
    gender = ("id" , 'gender-male')
    firstname = ("id" , 'FirstName')
    lastname = ("id" , 'LastName')
    emailid = ("id" , 'Email')
    password = ("id" , 'Password')
    conformpassword = ("id"  ,"ConfirmPassword")
    submit = ("id" , 'register-button')

    def register_an_account(self , fname, lname,email ,passwd ,cpasswd ):
        self.click_on_register()
        self.click_on_an_element(self.gender)
        self.send_text_to_an_element(self.firstname,fname)
        self.send_text_to_an_element(self.lastname, lname)
        self.send_text_to_an_element(self.emailid, email)
        self.send_text_to_an_element(self.password , passwd)
        self.send_text_to_an_element(self.conformpassword , cpasswd)
        self.click_on_an_element(self.submit)

