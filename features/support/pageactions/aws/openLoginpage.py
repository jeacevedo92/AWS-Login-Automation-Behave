# -*- coding: UTF-8 -*-

from features.support.pageactions.aws.basepage import BasePage
from features.support.pageactions.aws.loginAws import LoginPage
from features.support.locators.aws import awshomepage as homepage_locators


class OpenLoginPage(BasePage):
    """Action class to perform different actions on login page
    More specifically, it's a modal, but still we are considering
    it as a single page.
﻿﻿﻿
    Usage: login_page = LoginPage(context)
    login_page.click_on_your_trips_link()
    """
    def __init__(self, context):
        super(OpenLoginPage, self).__init__(context)

    def click_on_my_account(self):
        self.element_action.click(homepage_locators.btn_my_account)

    def click_on_account_settings(self):
        self.element_action.click(homepage_locators.btn_account_settings)
        return LoginPage(self.context)

