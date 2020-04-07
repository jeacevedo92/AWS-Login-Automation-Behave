# -*- coding: UTF-8 -*-

# ----------------------------------------------------------------------------
#   SUPPORTED LOCATOR STRATEGIES:
#       * XPATH
#       * ID
#       * NAME
#       * CSS_SELECTOR
#       * TAG_NAME
#       * LINK_TEXT
#       * PARTIAL_LINK_TEXT
# ----------------------------------------------------------------------------

txt_root_user = "ID,resolving_input"

btn_next = "ID,next_button_text"

txt_account_id = "ID,account"

txt_user_name = "ID,username"

txt_password = "ID,password"

btn_sign_in = "ID,signin_button"


account_id_required = "XPATH,//div[@id='accountFields']/fieldset/div[1][@class='textinput error']"

username_required = "XPATH,//div[@id='accountFields']/fieldset/div[2][@class='textinput error']"

password_required = "XPATH,//div[@id='accountFields']/fieldset/div[3][@class='textinput error']"

information_incorrect = "XPATH,//div[@id='main_message' and @class!='hide-page show-page ng-hide']"

account_id_alert = "ID, resolving_account_input_alert_content"