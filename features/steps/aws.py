# -*- coding: UTF-8 -*-

from behave import step, given, then
from features.support.actions.aws.openloginaction import OpenLoginAction
from features.support.actions.aws.loginaction import LoginAction

from utils.assertutils import Assert

# ===============================================================================================
# STEP DEFINITIONS:
# ===============================================================================================

@given(u'I am an aws user')
def step_impl(context):

    context.scenario.open_login_action = OpenLoginAction(context)
    context.scenario.login_page = context.scenario.open_login_action.open_login()

@step(u'I Login aws account')
def step_impl(context):

    context.scenario.login_action = LoginAction(context)
    context.scenario.dashboard_page = context.scenario.login_action.login(
        context.accountId,
        context.username,
        context.password
    )

@then(u'Login is successfull')
def step_impl(context):
    Assert.assert_true(context.scenario.dashboard_page.is_user_logged_in(context.username),
                       "User is not logged in!")
