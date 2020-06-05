## Story from conversation with 5aef32487804427bb6fd2d853b3d8249 on June 4th 2020

* greet: /greet
    - action_greet_user
    - slot{"shown_privacy":true}
* out_of_scope: do you like cakes?
    - respond_out_of_scope
* chitchat: what canyou hel with?
    - respond_chitchat
* chitchat: help
    - respond_chitchat
* enter_data: me
    - action_default_ask_affirmation
* trigger_rephrase: /trigger_rephrase
    - action_default_ask_rephrase
* deny: no
    - action_revert_fallback_events
* deny: no
    - utter_nohelp
* greet: hey
    - action_greet_user
* greet: hi
    - action_greet_user
* greet: ola
    - action_greet_user
* greet: oi
    - action_greet_user
* chitchat: do you speak [portuguese](language)?

## New Story

* greet: hello
    - action_greet_user
    - slot{"shown_privacy":true}
* affirm: that's cool
    - utter_thumbsup
