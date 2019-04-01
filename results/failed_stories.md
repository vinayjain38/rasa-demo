## Generated Story goal:chitchat, id:2ca65157d22b43caad664589ee29524e, 12/15/18 3415830769284134354
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howold
    - action_chitchat
* ask_howold{"number": 42}
    - action_chitchat
* ask_howold
    - action_chitchat
* ask_whatspossible
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:0430099345234226aecbf5260cd864b8, 12/15/18 4509295789363688221
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_time
    - action_chitchat
* ask_weather
    - action_chitchat
* ask_weather
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:0430099345234226aecbf5260cd864b8, 12/15/18 4509295789363688221
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_time
    - action_chitchat
* ask_weather
    - action_chitchat
* handleinsult
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:0430099345234226aecbf5260cd864b8, 12/15/18 4509295789363688221
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_time
    - action_chitchat
* ask_weather
    - action_chitchat
* handleinsult
    - action_chitchat
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howold
    - action_chitchat
* out_of_scope
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* out_of_scope
    - action_default_fallback   <!-- predicted: action_default_ask_rephrase -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "docs"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* enter_data
    - action_default_fallback   <!-- predicted: utter_possibilities -> fail -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* handleinsult
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* nicetomeeyou
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* nicetomeeyou
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* nicetomeeyou
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* nicetomeeyou
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* canthelp
    - action_default_fallback


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* ask_faq_opensource
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* out_of_scope
    - utter_out_of_scope   <!-- predicted: action_chitchat -->
    - utter_possibilities   <!-- predicted: action_listen -->
* affirm
    - action_default_fallback


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* out_of_scope
    - utter_out_of_scope   <!-- predicted: action_chitchat -->
    - utter_possibilities   <!-- predicted: action_listen -->
* signup_newsletter
    - utter_great   <!-- predicted: action_default_fallback -->
    - utter_ask_email   <!-- predicted: action_listen -->
* deny
    - utter_cantsignup   <!-- predicted: action_default_fallback -->
    - action_listen   <!-- predicted: action_default_fallback -->
* deny
    - action_default_fallback


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* out_of_scope
    - utter_out_of_scope   <!-- predicted: action_chitchat -->
    - utter_possibilities   <!-- predicted: action_listen -->
* signup_newsletter
    - utter_great   <!-- predicted: action_default_fallback -->
    - utter_ask_email   <!-- predicted: action_listen -->
* deny
    - utter_cantsignup   <!-- predicted: action_default_fallback -->
    - action_listen   <!-- predicted: action_default_fallback -->
* enter_data
    - action_store_email   <!-- predicted: action_default_fallback -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* out_of_scope
    - utter_out_of_scope   <!-- predicted: action_chitchat -->
    - utter_possibilities   <!-- predicted: action_listen -->
* signup_newsletter
    - utter_great   <!-- predicted: action_default_fallback -->
    - utter_ask_email   <!-- predicted: action_listen -->
* deny
    - utter_cantsignup   <!-- predicted: action_default_fallback -->
    - action_listen   <!-- predicted: action_default_fallback -->
* bye
    - action_default_fallback


## Generated Story goal:1 step, id:f48bb43d6f5645d69b0c1cd1cfc9c62b, 12/15/18 923590105913609100
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howold
    - action_chitchat
* ask_howdoing
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* enter_data
    - action_revert_fallback_events


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howold
    - action_chitchat
* ask_howdoing
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howold
    - action_chitchat
* enter_data
    - action_greet_user -> fail   <!-- predicted: action_default_fallback -->
* enter_data
    - utter_possibilities -> fail   <!-- predicted: action_default_fallback -->
* greet
    - action_greet_user   <!-- predicted: action_default_fallback -->
* greet
    - action_greet_user
* ask_whatspossible
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - action_revert_fallback_events


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howold
    - action_chitchat
* enter_data
    - action_greet_user -> fail   <!-- predicted: action_default_fallback -->
* enter_data
    - utter_possibilities -> fail   <!-- predicted: action_default_fallback -->
* greet
    - action_greet_user   <!-- predicted: action_default_fallback -->
* greet
    - action_greet_user
* ask_whatspossible
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howold
    - action_chitchat
* enter_data
    - action_greet_user -> fail   <!-- predicted: action_default_fallback -->
* enter_data
    - utter_possibilities -> fail   <!-- predicted: action_default_fallback -->
* greet
    - action_greet_user   <!-- predicted: action_default_fallback -->
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* ask_wherefrom
    - action_chitchat
* ask_wherefrom
    - action_chitchat
* ask_wherefrom
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* install_rasa
    - action_revert_fallback_events


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howold
    - action_chitchat
* enter_data
    - action_greet_user -> fail   <!-- predicted: action_default_fallback -->
* enter_data
    - utter_possibilities -> fail   <!-- predicted: action_default_fallback -->
* greet
    - action_greet_user   <!-- predicted: action_default_fallback -->
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* ask_wherefrom
    - action_chitchat
* ask_wherefrom
    - action_chitchat
* ask_wherefrom
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:oos, id:864df094a24a4cc3a6b55a824c1f3a35, 12/17/18 -7699038322326118938
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted -> fail   <!-- predicted: action_default_fallback -->
    - utter_first_bot_with_rasa -> fail
* out_of_scope
    - utter_out_of_scope   <!-- predicted: action_set_onboarding -->
    - utter_possibilities   <!-- predicted: utter_first_bot_with_rasa -->
    - utter_first_bot_with_rasa -> fail   <!-- predicted: action_listen -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: action_default_fallback -->
    - utter_first_bot_with_rasa -> fail   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding -> fail   <!-- predicted: action_set_onboarding -->
    - slot{"onboarding": true}
    - utter_built_bot_before -> fail   <!-- predicted: utter_built_bot_before -->
* affirm
    - utter_ask_migration -> fail   <!-- predicted: action_default_fallback -->
* affirm
    - utter_ask_which_tool -> fail
* enter_data
    - action_store_unknown_product -> fail   <!-- predicted: action_default_fallback -->
    - slot{"unknown_product": "Cleverbot"}
    - utter_no_guide_for_switch -> fail   <!-- predicted: utter_no_guide_for_switch -->
    - utter_anything_else -> fail   <!-- predicted: utter_anything_else -->
* deny
    - utter_nohelp   <!-- predicted: action_chitchat -->
* affirm
    - action_default_ask_affirmation   <!-- predicted: action_default_fallback -->
* deny
    - action_default_ask_rephrase   <!-- predicted: action_revert_fallback_events -->
* ask_weather
    - action_revert_fallback_events


## Generated Story goal:oos, id:864df094a24a4cc3a6b55a824c1f3a35, 12/17/18 -7699038322326118938
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted -> fail   <!-- predicted: action_default_fallback -->
    - utter_first_bot_with_rasa -> fail
* out_of_scope
    - utter_out_of_scope   <!-- predicted: action_set_onboarding -->
    - utter_possibilities   <!-- predicted: utter_first_bot_with_rasa -->
    - utter_first_bot_with_rasa -> fail   <!-- predicted: action_listen -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: action_default_fallback -->
    - utter_first_bot_with_rasa -> fail   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding -> fail   <!-- predicted: action_set_onboarding -->
    - slot{"onboarding": true}
    - utter_built_bot_before -> fail   <!-- predicted: utter_built_bot_before -->
* affirm
    - utter_ask_migration -> fail   <!-- predicted: action_default_fallback -->
* affirm
    - utter_ask_which_tool -> fail
* enter_data
    - action_store_unknown_product -> fail   <!-- predicted: action_default_fallback -->
    - slot{"unknown_product": "Cleverbot"}
    - utter_no_guide_for_switch -> fail   <!-- predicted: utter_no_guide_for_switch -->
    - utter_anything_else -> fail   <!-- predicted: utter_anything_else -->
* deny
    - utter_nohelp   <!-- predicted: action_chitchat -->
* affirm
    - action_default_ask_affirmation   <!-- predicted: action_default_fallback -->
* deny
    - action_default_ask_rephrase   <!-- predicted: action_revert_fallback_events -->


## Generated Story goal:oos, id:864df094a24a4cc3a6b55a824c1f3a35, 12/17/18 -7699038322326118938
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted -> fail   <!-- predicted: action_default_fallback -->
    - utter_first_bot_with_rasa -> fail
* out_of_scope
    - utter_out_of_scope   <!-- predicted: action_set_onboarding -->
    - utter_possibilities   <!-- predicted: utter_first_bot_with_rasa -->
    - utter_first_bot_with_rasa -> fail   <!-- predicted: action_listen -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: action_default_fallback -->
    - utter_first_bot_with_rasa -> fail   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding -> fail   <!-- predicted: action_set_onboarding -->
    - slot{"onboarding": true}
    - utter_built_bot_before -> fail   <!-- predicted: utter_built_bot_before -->
* affirm
    - utter_ask_migration -> fail   <!-- predicted: action_default_fallback -->
* affirm
    - utter_ask_which_tool -> fail
* enter_data
    - action_store_unknown_product -> fail   <!-- predicted: action_default_fallback -->
    - slot{"unknown_product": "Cleverbot"}
    - utter_no_guide_for_switch -> fail   <!-- predicted: utter_no_guide_for_switch -->
    - utter_anything_else -> fail   <!-- predicted: utter_anything_else -->
* deny
    - utter_nohelp   <!-- predicted: action_chitchat -->
* affirm
    - action_default_ask_affirmation   <!-- predicted: action_default_fallback -->


## Generated Story goal:3 step, id:9cbbe8c0fa0841deb30fe973cd80c614, 05/01/19 -1765672058575339702
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* install_rasa
    - utter_ask_python_installed   <!-- predicted: action_default_fallback -->
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: action_default_fallback -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command   <!-- predicted: action_default_fallback -->
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step4
    - utter_anything_else
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_thumbsup -->
* enter_data
    - action_revert_fallback_events


## Generated Story goal:3 step, id:9cbbe8c0fa0841deb30fe973cd80c614, 05/01/19 -1765672058575339702
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* install_rasa
    - utter_ask_python_installed   <!-- predicted: action_default_fallback -->
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: action_default_fallback -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command   <!-- predicted: action_default_fallback -->
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step4
    - utter_anything_else
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_thumbsup -->


## Generated Story goal:3 step, id:9cbbe8c0fa0841deb30fe973cd80c614, 05/01/19 -1765672058575339702
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* install_rasa
    - utter_ask_python_installed   <!-- predicted: action_default_fallback -->
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: action_default_fallback -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command   <!-- predicted: action_default_fallback -->
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step4
    - utter_anything_else
* enter_data
    - action_select_installation_command -> fail   <!-- predicted: action_default_fallback -->
    - utter_ask_ready_to_build -> fail   <!-- predicted: action_default_fallback -->
* affirm
    - action_default_ask_affirmation   <!-- predicted: action_default_fallback -->
* ask_whatspossible
    - action_default_fallback   <!-- predicted: action_revert_fallback_events -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "what i have to do"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart


## Generated Story goal:oos, id:174129b4be704f47b76aa8dc5b2f3ab6, 12/15/18 -5421971901023397932
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* out_of_scope
    - utter_out_of_scope   <!-- predicted: action_chitchat -->
    - action_listen   <!-- predicted: utter_possibilities -->
* enter_data{"email": "lavi@email.com"}
    - slot{"email": "lavi@email.com"}
    - slot{"email": "lavi@email.com"}
    - action_greet_user -> fail   <!-- predicted: utter_possibilities -> fail -->
* greet
    - action_greet_user   <!-- predicted: action_default_fallback -->
* enter_data
    - action_default_fallback


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - action_chitchat   <!-- predicted: action_default_fallback -->
* enter_data
    - action_default_ask_affirmation   <!-- predicted: action_default_fallback -->
* deny
    - action_default_ask_rephrase   <!-- predicted: action_revert_fallback_events -->
* how_to_get_started
    - action_revert_fallback_events


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - action_chitchat   <!-- predicted: action_default_fallback -->
* enter_data
    - action_default_ask_affirmation   <!-- predicted: action_default_fallback -->
* deny
    - action_default_ask_rephrase   <!-- predicted: action_revert_fallback_events -->


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - action_chitchat   <!-- predicted: action_default_fallback -->
* enter_data
    - action_default_ask_affirmation   <!-- predicted: action_default_fallback -->


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - action_chitchat   <!-- predicted: action_default_fallback -->
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_faq_differencecorenlu
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: action_default_fallback -->
* ask_faq_differencecorenlu{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_default_ask_affirmation   <!-- predicted: utter_quickstart -->
* deny
    - action_default_ask_rephrase   <!-- predicted: action_revert_fallback_events -->
* enter_data
    - action_revert_fallback_events


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - action_chitchat   <!-- predicted: action_default_fallback -->
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_faq_differencecorenlu
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: action_default_fallback -->
* ask_faq_differencecorenlu{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_default_ask_affirmation   <!-- predicted: utter_quickstart -->
* deny
    - action_default_ask_rephrase   <!-- predicted: action_revert_fallback_events -->


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - action_chitchat   <!-- predicted: action_default_fallback -->
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_faq_differencecorenlu
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: action_default_fallback -->
* ask_faq_differencecorenlu{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_default_ask_affirmation   <!-- predicted: utter_quickstart -->


## Generated Story goal:1 step, id:3c9cd2509a78495bb5fd306618a9ba8e, 12/17/18 3076997113982385599
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted -> fail   <!-- predicted: action_default_fallback -->
    - utter_first_bot_with_rasa -> fail
* enter_data
    - action_greet_user -> fail   <!-- predicted: action_set_onboarding -> fail -->
* affirm
    - utter_explain_nlu -> fail   <!-- predicted: action_set_onboarding -> fail -->
    - utter_tryout -> fail   <!-- predicted: utter_built_bot_before -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart -> fail   <!-- predicted: action_default_fallback -->
    - utter_anything_else -> fail   <!-- predicted: utter_anything_else -->
* source_code
    - utter_source_code   <!-- predicted: action_default_fallback -->
    - utter_anything_else


## Generated Story goal:chitchat, id:2ca65157d22b43caad664589ee29524e, 12/15/18 3415830769284134354
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howold
    - action_chitchat
* ask_howold{"number": 42}
    - action_chitchat
* ask_howold
    - action_chitchat
* enter_data
    - utter_possibilities -> fail   <!-- predicted: action_default_fallback -->


## Generated Story goal:chitchat, id:0430099345234226aecbf5260cd864b8, 12/15/18 4509295789363688221


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat
* out_of_scope
    - utter_out_of_scope   <!-- predicted: action_chitchat -->
    - utter_possibilities   <!-- predicted: action_listen -->
* signup_newsletter
    - utter_great   <!-- predicted: action_default_fallback -->
    - utter_ask_email   <!-- predicted: action_listen -->
* deny
    - utter_cantsignup   <!-- predicted: action_default_fallback -->
    - action_listen   <!-- predicted: action_default_fallback -->
* handleinsult
    - action_chitchat   <!-- predicted: action_default_fallback -->
    - utter_ask_email -> fail   <!-- predicted: action_listen -->
* deny
    - utter_cantsignup -> fail   <!-- predicted: action_default_fallback -->
* deny
    - utter_direct_install -> fail   <!-- predicted: action_default_fallback -->
    - utter_anything_else -> fail   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_default_fallback -->


## Generated Story goal:3 step, id:953db2ccbe0748c586f5904a1b9b4432, 12/15/18 -2802431565840004587
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* install_rasa
    - utter_ask_python_installed   <!-- predicted: action_default_fallback -->
* deny
    - utter_get_python   <!-- predicted: action_default_fallback -->
    - utter_ask_pip_or_conda   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_default_fallback -->
    - utter_ask_ready_to_build   <!-- predicted: utter_ask_ready_to_build -> fail -->
* affirm
    - utter_get_starter_pack   <!-- predicted: action_default_fallback -->
    - utter_direct_to_step4   <!-- predicted: action_default_fallback -->
    - utter_anything_else   <!-- predicted: action_listen -->
* ask_howdoing
    - action_chitchat   <!-- predicted: action_default_fallback -->


## Generated Story goal:1 step, id:f48bb43d6f5645d69b0c1cd1cfc9c62b, 12/15/18 923590105913609100
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only   <!-- predicted: utter_quickstart_nlu_only -> fail -->
    - utter_anything_else


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howold
    - action_chitchat
* enter_data
    - action_greet_user -> fail   <!-- predicted: action_default_fallback -->
* enter_data
    - utter_possibilities -> fail   <!-- predicted: action_default_fallback -->
* greet
    - action_greet_user   <!-- predicted: action_default_fallback -->
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* ask_wherefrom
    - action_chitchat
* ask_wherefrom
    - action_chitchat
* install_rasa
    - utter_ask_python_installed   <!-- predicted: action_default_fallback -->
* enter_data
    - utter_get_python -> fail   <!-- predicted: action_default_fallback -->
    - utter_ask_pip_or_conda   <!-- predicted: action_default_fallback -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command   <!-- predicted: action_default_fallback -->
    - utter_ask_ready_to_build


## Generated Story goal:oos, id:864df094a24a4cc3a6b55a824c1f3a35, 12/17/18 -7699038322326118938
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted -> fail   <!-- predicted: action_default_fallback -->
    - utter_first_bot_with_rasa -> fail
* out_of_scope
    - utter_out_of_scope   <!-- predicted: action_set_onboarding -->
    - utter_possibilities   <!-- predicted: utter_first_bot_with_rasa -->
    - utter_first_bot_with_rasa -> fail   <!-- predicted: action_listen -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: action_default_fallback -->
    - utter_first_bot_with_rasa -> fail   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding -> fail   <!-- predicted: action_set_onboarding -->
    - slot{"onboarding": true}
    - utter_built_bot_before -> fail   <!-- predicted: utter_built_bot_before -->
* affirm
    - utter_ask_migration -> fail   <!-- predicted: action_default_fallback -->
* affirm
    - utter_ask_which_tool -> fail
* enter_data
    - action_store_unknown_product -> fail   <!-- predicted: action_default_fallback -->
    - slot{"unknown_product": "Cleverbot"}
    - utter_no_guide_for_switch -> fail   <!-- predicted: utter_no_guide_for_switch -->
    - utter_anything_else -> fail   <!-- predicted: utter_anything_else -->
* deny
    - utter_nohelp   <!-- predicted: action_chitchat -->
* ask_weather
    - action_chitchat


## Generated Story goal:faq, id:db852c1fc7144db09e449fec4567614e, 12/17/18 -5129452726289215743
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* greet
    - action_greet_user
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_default_fallback -->
    - utter_anything_else


## Generated Story goal:1 step, id:93b8b449ab074a6f973da26067b5c163, 12/17/18 -6676267086559597786
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* technical_question
    - utter_getstarted -> fail   <!-- predicted: action_default_fallback -->
    - utter_first_bot_with_rasa -> fail
* affirm
    - action_set_onboarding -> fail
    - slot{"onboarding": true}
    - utter_built_bot_before -> fail   <!-- predicted: utter_built_bot_before -->
* deny
    - utter_explain_stack -> fail   <!-- predicted: action_default_fallback -->
    - utter_stack_details -> fail   <!-- predicted: utter_stack_details -->
    - utter_explain_nlucore -> fail   <!-- predicted: utter_explain_nlucore -->
* enter_data{"number": 1}
    - utter_great -> fail   <!-- predicted: utter_explain_nlu -->
    - utter_ask_email -> fail
* deny
    - utter_cantsignup -> fail   <!-- predicted: action_default_fallback -->
    - action_listen   <!-- predicted: action_default_fallback -->


## Generated Story goal:1 step, id:5b7be2c22b874342aeca4216cfd5d35a, 12/15/18 1624335723075150223
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* out_of_scope
    - utter_out_of_scope   <!-- predicted: action_default_ask_affirmation -->
    - utter_possibilities   <!-- predicted: action_listen -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: action_default_fallback -->
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else


## Generated Story goal:oos, id:174129b4be704f47b76aa8dc5b2f3ab6, 12/15/18 -5421971901023397932
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* out_of_scope
    - utter_out_of_scope   <!-- predicted: action_chitchat -->
    - action_listen   <!-- predicted: utter_possibilities -->
* enter_data{"email": "lavi@email.com"}
    - slot{"email": "lavi@email.com"}
    - slot{"email": "lavi@email.com"}
    - action_greet_user -> fail   <!-- predicted: utter_possibilities -> fail -->
* greet
    - action_greet_user   <!-- predicted: action_default_fallback -->


## Generated Story goal:1 step, id:3a1c70eaf9234bb6b27160abfb6d1f88, 12/15/18 3863097957169160390
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities -> fail   <!-- predicted: action_default_fallback -->
* enter_data
    - utter_possibilities -> fail   <!-- predicted: action_default_fallback -->
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only   <!-- predicted: utter_quickstart_nlu_only -> fail -->
    - utter_anything_else
* deny
    - utter_nohelp   <!-- predicted: action_default_fallback -->
* affirm
    - utter_thumbsup   <!-- predicted: action_default_fallback -->


## Generated Story goal:1 step, id:ef54f3457dd947be9f7ccdfa66d146ce, 12/17/18 -4040032104474387651
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack   <!-- predicted: utter_explain_stack -> fail -->
    - utter_stack_details   <!-- predicted: utter_stack_details -> fail -->
    - utter_explain_nlucore
* ask_whatisrasa{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - action_chitchat   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: action_listen -->
* out_of_scope{"product": "core", "number": 1}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_out_of_scope   <!-- predicted: action_default_fallback -->
    - utter_possibilities   <!-- predicted: utter_anything_else -->
* affirm
    - utter_thumbsup   <!-- predicted: action_default_fallback -->


## Generated Story goal:1 step, id:19722107f07a4120bef398ea514e00de, 12/15/18 3342731703903234413
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"language": "chinese"}
    - slot{"language": "chinese"}
    - slot{"language": "chinese"}
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack   <!-- predicted: action_default_fallback -->
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - action_chitchat   <!-- predicted: action_default_fallback -->
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_faq_differencecorenlu
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: action_default_fallback -->
* enter_data
    - utter_tryout -> fail   <!-- predicted: action_default_fallback -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: action_default_fallback -->
    - utter_anything_else
* enter_data
    - utter_not_sure   <!-- predicted: action_default_fallback -->
    - utter_possibilities   <!-- predicted: action_default_fallback -->


