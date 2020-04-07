# -*- coding: UTF-8 -*-

from features.support.pageactions.aws.basepage import BasePage

from features.support.locators.aws import dashboardawspage as dashboard_locators



class DashBoardPage(BasePage):
    """Action class to perform different actions on login page
    More specifically, it's a modal, but still we are considering
    it as a single page.
﻿﻿﻿
    Usage: login_page = LoginPage(context)
    login_page.click_on_your_trips_link()
    """
    def __init__(self, context):
        super(DashBoardPage, self).__init__(context)

    def is_user_logged_in(self, username):
        return self.element_action.is_element_displayed(
            dashboard_locators.btn_home)