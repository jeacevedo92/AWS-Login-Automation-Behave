# -*- coding: UTF-8 -*-

from features.support.pageactions.aws.openLoginpage import OpenLoginPage
from features.support.pageactions.aws.loginAws import LoginPage


class OpenLoginAction(object):
    """Action class to perform operations related to login
    """
    def __init__(self, context):
        self.context = context

        # Visually there is no separate Login Page as such, but to make things more
        # clear, let's treat the sign in page modal as a complete page in itself
        self.open_login_page = OpenLoginPage(self.context)

    def open_login(self):
        """Login to application
        :param email_address: Email address of the user
        :param password: Password of the user
        :return: Boolean value specifying whether login was successful
        """
        self.open_login_page.click_on_my_account()
        self.open_login_page.click_on_account_settings()

        return LoginPage(self.context)
