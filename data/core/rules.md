>> just newsletter
    - ...
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - submit_subscribe_newsletter_form
    - utter_docu
    - utter_ask_feedback

>> just newsletter (with email already)
    - ...
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - submit_subscribe_newsletter_form
    - utter_docu
    - utter_ask_feedback

>> newsletter, don't give email once
    - ...
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter

>> newsletter + greet
    - ...
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* greet
    - action_greet_user
    - utter_ask_continue_newsletter

>> newsletter + bye
    - ...
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* bye
    - utter_bye
    - utter_ask_continue_newsletter

>> newsletter + explain
    - ...
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* explain
    - utter_response_why_email
    - utter_ask_continue_newsletter

>> newsletter + canthelp
    - ...
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_newsletter

>> newsletter + chitchat
    - ...
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* chitchat
    - respond_chitchat
    - utter_ask_continue_newsletter

>> newsletter + out_of_scope
    - ...
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_newsletter

>> newsletter + react_positive
    - ...
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* react_positive
    - utter_react_positive
    - utter_ask_continue_newsletter

>> newsletter + react_negative
    - ...
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* react_negative
    - utter_react_negative
    - utter_ask_continue_newsletter

>> newsletter + faq
    - ...
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* faq
    - respond_faq
    - action_set_faq_slot
    - utter_ask_continue_newsletter

>> newsletter + handoff
    - ...
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* human_handoff
    - utter_contact_email
    - utter_ask_continue_newsletter

>> ask continue newsletter + affirm
    - ...
    - form{"name": "subscribe_newsletter_form"}
    - ...
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - submit_subscribe_newsletter_form
    - utter_docu
    - utter_ask_feedback

>> ask continue newsletter + deny
    - ...
    - form{"name": "subscribe_newsletter_form"}
    - ...
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - utter_ask_feedback

>> just sales
    - ...
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - submit_sales_form
    - utter_ask_feedback

>> sales + chitchat
    - ...
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* chitchat
    - respond_chitchat
    - utter_ask_continue_sales

>> sales + react_positive
    - ...
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* react_positive
    - utter_react_positive
    - utter_ask_continue_sales

>> sales + react_negative
    - ...
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* react_negative
    - utter_react_negative
    - utter_ask_continue_sales

>> sales + canthelp
    - ...
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* canthelp
    - utter_canthelp
    - action_set_faq_slot
    - utter_ask_continue_sales

>> sales + faq
    - ...
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* faq
    - respond_faq
    - action_set_faq_slot
    - utter_ask_continue_sales

>> sales + handoff
    - ...
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* human_handoff
    - utter_contact_email
    - utter_ask_continue_sales

>> sales + explain
    - ...
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* explain
    - action_explain_sales_form
    - utter_ask_continue_sales

>> sales + greet
    - ...
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* greet
    - action_greet_user
    - utter_ask_continue_sales

>> sales + bye
    - ...
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* bye
    - utter_bye
    - utter_ask_continue_sales

>> sales + out_of_scope
    - ...
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_sales

>> ask continue sales + affirm
    - ...
    - form{"name": "sales_form"}
    - ...
    - utter_ask_continue_sales
* affirm
    - utter_great
    - sales_form
    - form{"name": null}
    - submit_sales_form
    - utter_ask_feedback

>> ask continue sales + deny
    - ...
    - form{"name": "sales_form"}
    - ...
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - utter_ask_feedback

>> feedback + enter_data + chitchat + enter_data
    - ...
    - utter_ask_feedback
* enter_data
    - utter_thumbsup
    - utter_anything_else
* chitchat
    - respond_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities
