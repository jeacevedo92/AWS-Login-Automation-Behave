# -*- coding: UTF-8 -*-

from features.support.pageactions.aws.basepage import BasePage

from features.support.locators.aws import signInawspage as aws_login_locators



class LoginPage(BasePage):
    """Action class to perform different actions on login page
    More specifically, it's a modal, but still we are considering
    it as a single page.
﻿﻿﻿
    Usage: login_page = LoginPage(context)
    login_page.click_on_your_trips_link()
    """
    def __init__(self, context):
        super(LoginPage, self).__init__(context)

    def type_account_id(self, account_id):
        self.element_action.type(
            aws_login_locators.txt_root_user, account_id)


    def click_next(self):
        self.element_action.click(aws_login_locators.btn_next)

    def type_user_name(self, user_name):
        self.element_action.type(
            aws_login_locators.txt_user_name, user_name)

    def type_password(self, password):
        self.element_action.type(
            aws_login_locators.txt_password, password)

    def click_login(self):
        self.element_action.click(aws_login_locators.btn_sign_in)
