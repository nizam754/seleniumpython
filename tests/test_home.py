from seleniumbase import BaseCase

class HomeTest(BaseCase):
    def test_home_page(self):
        #open home page
        self.open("https://practice.automationbro.com")

        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")

        # assert logo
        self.assert_element(".custom-logo-link")