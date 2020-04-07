# -*- coding: UTF-8 -*-

from features.support.pageactions.aws.loginAws import LoginPage
from features.support.pageactions.aws.dashboardawspage import DashBoardPage


class LoginAction(object):
    """Action class to perform operations related to login
    """
    def __init__(self, context):
        self.context = context

        # Visually there is no separate Login Page as such, but to make things more
        # clear, let's treat the sign in page modal as a complete page in itself
        self.login_page = LoginPage(self.context)

    def login(self, accountId,username,password):
        """Login to application
        :param email_address: Email address of the user
        :param password: Password of the user
        :return: Boolean value specifying whether login was successful
        """
        self.login_page.type_account_id(accountId)
        self.login_page.click_next()
        self.login_page.type_user_name(username)
        self.login_page.type_password(password)
        self.login_page.click_login()

        return DashBoardPage(self.context)
