## Generated Story goal:chitchat, id:9ba470b867964cdc98cc7e136f5911ca, 1/17/2019 -3059658052540400860
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_weather
    - action_chitchat
* affirm
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

## Generated Story goal:chitchat, id:52be56be5b4b442e9ca93efc98d1e1f3, 1/17/2019 -2239970960692433696
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* affirm
    - utter_thumbsup
* ask_weather
    - action_chitchat
* ask_whatisrasa
    - action_chitchat
* ask_whatisrasa{"name": "AI"}
    - slot{"name": "AI"}
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* thank
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* thank
    - utter_noworries
    - utter_anything_else
* deny
    - utter_nohelp
* bye
    - utter_bye

## Generated Story goal:1 step, id:ad0e262cafeb4da79181e432aaa301fe, 1/17/2019 6156849827433177003
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* greet
    - action_greet_user
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* greet
    - action_default_ask_affirmation
* ask_whatisrasa
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_whatisrasa
    - action_chitchat
* affirm
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
    - utter_quickstart_nlu_only
    - utter_anything_else
* deny
    - utter_nohelp

## Generated Story goal:chitchat, id:93e8447e134049748974663f7b00e096, 1/17/2019 -1599232815211458948
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_howdoing
    - action_default_ask_affirmation
* ask_howdoing
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_howdoing
    - action_chitchat
* out_of_scope
    - action_default_ask_affirmation
* ask_howdoing
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}

## Generated Story goal:oos, id:d6ea06dfdc264dbe812f2fb0cbc6bc55, 1/21/2019 68641820257923046
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_faq_platform
    - action_default_ask_affirmation
* ask_faq_differencecorenlu
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: enter_data
    - form: feedback_form
    - slot{"feedback_message": "On premisis"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart
    - restart
* ask_whoami
    - action_default_ask_affirmation
* ask_whoisit
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_whoisit
    - action_chitchat
* telljoke
    - action_default_ask_affirmation
* telljoke
    - action_revert_fallback_events
    - rewind
    - rewind
* telljoke
    - action_chitchat
* bye
    - utter_bye

## Generated Story goal:1 step, id:e6e65eb5983c4a3eb410fcac683169e1, 1/17/2019 3456148870107483958
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* technical_question{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_getstarted
    - utter_first_bot_with_rasa
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* switch{"name": "Microsoft Bot"}
    - slot{"name": "Microsoft Bot"}
    - action_store_unknown_product
    - slot{"unknown_product": "i'm migration from Microsoft Bot framework"}
    - utter_no_guide_for_switch
    - utter_anything_else
* affirm
    - utter_what_help
* technical_question
    - utter_explain_core
    - utter_also_explain_nlu
* deny
    - utter_tryout
* how_to_get_started
    - utter_quickstart
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
    - utter_direct_step3
* get_started_step3
    - action_greet_user
    - slot{"step": "3"}

## Generated Story goal:oos, id:68535305c8e94c24b6ceb3fabe9ef967, 1/21/2019 1144346795764522111
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* out_of_scope
    - utter_out_of_scope
* enter_data
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* enter_data
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* enter_data
    - action_store_email
    - rewind

## Generated Story goal:oos, id:412f99d45b7e4127821d7aca580232df, 1/21/2019 -2800644051762337531
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* ask_howdoing
    - action_default_ask_affirmation
* handleinsult
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: ask_weather
    - form: feedback_form
    - slot{"feedback_message": "can u tell the weather today?"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_nohelp

## Generated Story goal:oos, id:a7b3ec0f08aa4aefbe40b8cf73ad730e, 1/17/2019 -5894359074079461719
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* technical_question
    - action_default_ask_affirmation
* technical_question
    - action_revert_fallback_events
    - rewind
    - rewind
* technical_question
    - utter_great
    - utter_ask_email
* enter_data{"number": 1}
    - action_store_email
    - rewind
* ask_isbot
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* affirm
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* affirm
    - utter_thumbsup
* ask_whatspossible
    - action_chitchat
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
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
    - utter_direct_step3
* get_started_step3
    - action_greet_user
    - slot{"step": "3"}
* technical_question
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* technical_question
    - action_default_ask_affirmation
* technical_question
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
    - rewind
    - rewind
* technical_question
    - utter_out_of_scope
    - utter_possibilities
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
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
* ask_languagesbot{"language": "french"}
    - slot{"language": "french"}
    - action_chitchat
    - utter_tryout
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
    - utter_direct_step3

## Generated Story goal:1 step, id:f5b03ee6088f41c789511307b1278bd0, 1/17/2019 -2311932768906503071
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_whatspossible
    - action_chitchat
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

## Generated Story goal:1 step, id:244146ea21db4bd59e8b9bdc7cbfd90f, 1/17/2019 -2311932768906503071
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_whatspossible
    - action_chitchat
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

## Generated Story goal:faq, id:1f9da8c5ca53440f99141cb6cf0d4414, 1/17/2019 -7199178373619781498
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_faq_python_version
    - action_faqs
* ask_faq_channels
    - action_faqs

## Generated Story goal:1 step, id:ef9ba45f78b24a74849fd5ab77bebe77, 1/17/2019 -2214797796045185918
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* enter_data
    - action_store_unknown_product
    - slot{"unknown_product": "aws"}
    - utter_no_guide_for_switch
    - utter_anything_else
* ask_faq_languages
    - action_faqs
* ask_howdoing
    - action_chitchat

## Generated Story goal:1 step, id:1d0734fdbfea4412b5eaf47630f8a272, 1/17/2019 1783322181160637737
* get_started_step3
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "3"}
* ask_faq_languages
    - action_default_ask_affirmation
* how_to_get_started
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}

## Generated Story goal:1 step, id:1490cc913ad74a7598933af539001ed7, 1/17/2019 -5919864899240889730
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - action_default_ask_affirmation
* how_to_get_started
    - action_revert_fallback_events
    - rewind
    - rewind
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
* greet
    - action_greet_user
* enter_data
    - action_default_ask_affirmation
* enter_data
    - action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - utter_not_sure
    - utter_possibilities
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
* enter_data
    - action_default_ask_affirmation
* enter_data
    - action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - utter_not_sure
    - utter_tryout
* enter_data{"number": 3}
    - utter_not_sure
    - utter_possibilities
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
* deny
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
    - utter_direct_step3
* get_started_step3
    - action_greet_user
    - slot{"step": "3"}
* get_started_step4
    - action_greet_user
    - slot{"step": "4"}
* get_started_step2
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* get_started_step3
    - action_greet_user
    - slot{"step": "3"}
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* deny
    - utter_thumbsup

## Generated Story goal:oos, id:5c37c111bd3148a8a78b04396e811442, 1/21/2019 -7842643047626512937
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_whatisrasa
    - action_chitchat
* ask_which_events
    - action_default_ask_affirmation
* out_of_scope
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}

## Generated Story goal:subscribe, id:22e99f1b08304622a90a415d6d6f0884, 1/17/2019 -1742920849927930963
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* enter_data{"jobfunction": "developer"}
    - utter_not_sure
    - utter_possibilities
* out_of_scope
    - action_default_ask_affirmation
* ask_isbot
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_isbot
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* signup_newsletter
    - utter_great
    - utter_ask_email
* handleinsult{"email": "fuck@fuck.com"}
    - slot{"email": "fuck@fuck.com"}
    - action_default_ask_affirmation
* enter_data{"email": "fuk@google.com"}
    - slot{"email": "fuk@google.com"}
    - action_revert_fallback_events
    - rewind
    - rewind
* enter_data{"email": "fuk@google.com"}
    - action_store_email
    - slot{"email": "fuk@google.com"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "fuck@rasa.com"}
    - slot{"email": "fuck@rasa.com"}
    - action_store_email
    - slot{"email": "fuck@rasa.com"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "ghmulchandani@gmail.com"}
    - slot{"email": "ghmulchandani@gmail.com"}
    - action_store_email
    - slot{"email": "ghmulchandani@gmail.com"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat

## Generated Story goal:whatspossible, id:355e69b5d9d9411cb5fa52662fa2def0, 1/17/2019 -5217718344542950027
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_whoisit
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_tryout
* enter_data
    - action_store_job
    - slot{"job_function": "fll satck"}
    - utter_ask_usecase
* contact_sales
    - utter_explain_core
    - utter_ask_jobfunction
* enter_data{"jobfunction": "data analyst"}
    - action_store_job
    - slot{"job_function": "data analyst"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "sales bot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 0}
    - action_store_budget
    - slot{"budget": "0"}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "akshit"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "kl"}
    - utter_ask_businessmail
* enter_data
    - action_store_email
    - rewind
* enter_data
    - action_store_email
    - rewind
* deny
    - action_default_ask_affirmation
* deny
    - action_default_ask_rephrase
* react_positive
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* react_positive
    - action_store_email
    - rewind
* deny
    - utter_direct_install
    - utter_anything_else
* affirm
    - utter_thumbsup
    - utter_anything_else
* affirm
    - utter_what_help
* enter_data
    - action_select_installation_command
    - utter_ask_ready_to_build
* bye
    - utter_built_bot_before
    - utter_direct_to_forum_for_help
* bye
    - utter_bye
* greet
    - utter_great
    - utter_ask_email
* greet
    - action_greet_user
* greet
    - action_greet_user
* greet
    - action_greet_user
* greet
    - action_greet_user
* greet
    - action_greet_user
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities
* enter_data{"number": 4}
    - utter_not_sure
    - utter_possibilities
* enter_data
    - utter_not_sure
    - utter_possibilities

## Generated Story goal:oos, id:7af8ce52ee284c7f9d3fab14399f26ce, 1/21/2019 -8394501666578819484
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* out_of_scope
    - action_default_ask_affirmation
* greet
    - action_revert_fallback_events
    - rewind
    - rewind
* greet
    - action_greet_user
* enter_data
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* ask_why_contribute
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* ask_why_contribute
    - utter_reasons_to_contribute
* greet
    - action_greet_user
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* enter_data
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* how_to_get_started
    - action_default_ask_affirmation

## Generated Story goal:1 step, id:9ccbfe7e03d8493e9ad076ddb3bdf257, 1/21/2019 2542390019453906636
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities
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

## Generated Story goal:1 step, id:ef86c39b5e40417aac7ef15654d99a7d, 1/17/2019 2767800726246079999
* get_started_step2
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "2"}
    - utter_direct_step3
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
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Generated Story goal:oos, id:bf00d72bf89d41c3bce4df7fbb86ad25, 1/17/2019 7709824219965927386
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_howdoing{"product": "stack"}
    - slot{"product": "stack"}
    - action_default_ask_affirmation
* enter_data
    - action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - utter_not_sure
    - utter_possibilities

## Generated Story goal:-, id:6ed6199b142e48fd8d50b35699b72ac3, 1/17/2019 5133980967270429995
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_default_ask_affirmation
* ask_isbot
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: affirm
    - form: feedback_form
    - slot{"feedback_message": "yes"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* affirm
    - utter_thumbsup
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:chitchat, id:ad0e262cafeb4da79181e432aaa301fe, 1/17/2019 6156849827433177003
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* greet
    - action_greet_user
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* greet
    - action_default_ask_affirmation
* ask_whatisrasa
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_whatisrasa
    - action_chitchat
* affirm
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
    - utter_quickstart_nlu_only
    - utter_anything_else
* deny
    - utter_nohelp

## Generated Story goal:chitchat, id:acc9cd88dd6f4b71a4b4a5c446cd5cad, 1/17/2019 6204566475335477119
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_time
    - action_chitchat

## Generated Story goal:1 step, id:a49237cad6a048ccb0b27179fb717cd7, 1/17/2019 532369082825631795
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - utter_getstarted_new
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_tryout

## Generated Story goal:oos, id:d6ad79d6299f41a398b0e07b43f7ba3e, 1/17/2019 47470592212118036
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_whatisrasa
    - action_chitchat
* ask_howdoing
    - action_default_ask_affirmation
* ask_isbot
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: how_to_get_started
    - form: feedback_form
    - slot{"feedback_message": "How does a chatbot work?"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart
    - restart

## Generated Story goal:1step, id:61b4265420894753addaea0aba46e0cc, 1/21/2019 -6017048633046404641
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
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
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* deny
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* deny
    - utter_thumbsup
* enter_data
    - utter_not_sure
    - utter_possibilities
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "Student"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "E-commerce sales"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 0}
    - action_store_budget
    - slot{"budget": "0"}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "Partha Sarathi Nayak"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "Student at IIIT Bhubaneswar."}
    - utter_ask_businessmail
* enter_data{"email": "b415034@iiit-bh.ac.in"}
    - slot{"email": "b415034@iiit-bh.ac.in"}
    - action_store_email
    - slot{"email": "b415034@iiit-bh.ac.in"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* affirm
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_faqs
    - utter_first_bot_with_rasa
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core

## Generated Story goal:1 step, id:b0eb3d9db3284bff84e93b1ba713e60f, 1/17/2019 5579353674653128417
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_isbot
    - action_default_ask_affirmation
* affirm
    - action_revert_fallback_events
    - rewind
    - rewind
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* enter_data
    - action_default_ask_affirmation
* deny
    - action_revert_fallback_events
    - rewind
    - rewind
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout

## Generated Story goal:3 step, id:506d3367e58644bbacff46b6f5be1745, 1/17/2019 -3286283981681924695
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* enter_data
    - action_default_ask_affirmation
* install_rasa
    - action_revert_fallback_events
    - rewind
    - rewind
* install_rasa
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step4
* thank
    - utter_noworries
    - utter_anything_else
* enter_data
    - action_select_installation_command
    - utter_ask_ready_to_build

## Generated Story goal:1 step, id:cb1f92b4146448b3a59981760ce593ea, 1/17/2019 5614594403456815770
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* affirm
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
* how_to_get_started
    - utter_explain_core
    - utter_also_explain_nlu
* how_to_get_started
    - utter_explain_nlu
    - utter_anything_else
* how_to_get_started
    - action_default_ask_affirmation
* how_to_get_started
    - action_revert_fallback_events
    - rewind
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* enter_data
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* telljoke
    - action_default_ask_affirmation
* telljoke
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
    - rewind
    - rewind
* telljoke
    - action_chitchat
* ask_howbuilt
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* signup_newsletter
    - utter_great
    - utter_ask_email
* ask_isbot
    - action_default_ask_affirmation
* affirm
    - action_revert_fallback_events
    - rewind
    - rewind
* affirm
    - utter_quickstart
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
    - utter_direct_step3
* source_code
    - utter_source_code
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_default_ask_affirmation
* enter_data{"jobfunction": "developer"}
    - action_revert_fallback_events
    - rewind
    - rewind
* enter_data{"jobfunction": "developer"}
    - action_store_job
    - slot{"job_function": "developer"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "A FAQ bot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"amount-of-money": 10000}
    - action_store_budget
    - slot{"budget": 10000}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "Jaison"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "Jose"}
    - utter_ask_businessmail
* enter_data{"email": "jaison.basket@gmail.com"}
    - slot{"email": "jaison.basket@gmail.com"}
    - action_store_email
    - slot{"email": "jaison.basket@gmail.com"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* source_code
    - utter_source_code
    - utter_anything_else

## Generated Story goal:oos, id:5805f0243b464ca8993f94baf85c33a4, 1/21/2019 1381373174730398034
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* enter_data
    - utter_not_sure
    - utter_possibilities
* enter_data{"language": "spanish"}
    - slot{"language": "spanish"}
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* enter_data
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* bye
    - utter_bye

## Generated Story goal:chitchat, id:0769470f9f7740cb95046aa133aeb14b, 1/17/2019 7137735297069808552
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* ask_weather
    - action_chitchat
* ask_howdoing
    - action_chitchat

## Generated Story goal:1 step, id:e9524046e5c24186a6f990d910baa1eb, 1/17/2019 -8612460516688307242
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* enter_data
    - utter_not_sure
    - utter_possibilities
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

## Generated Story goal:1 step, id:925876eff1bd4dc19c07d231f412e0eb, 1/17/2019 5915949618218378596
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
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
    - utter_quickstart_nlu_only
    - utter_anything_else

## Generated Story goal:chitchat, id:a822333f98824fef860dd749ff9422d8, 1/17/2019 -1839787126588499699
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_howdoing
    - action_chitchat
* ask_wherefrom
    - action_chitchat
* affirm
    - action_default_ask_affirmation

## Generated Story goal:1 step, id:4adec11afb8e4f9fbbcb4025edd27830, 1/21/2019 -1120330112114412360
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_whatisrasa
    - action_chitchat
* how_to_get_started
    - action_default_ask_affirmation
* how_to_get_started
    - action_revert_fallback_events
    - rewind
    - rewind
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
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
    - utter_direct_step3

## Generated Story goal:oos, id:6d95958b82fc469ba8f9990dc4dbfc05, 1/17/2019 -5868830470542520042
* get_started_step3
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "3"}
* install_rasa
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda
* affirm
    - utter_what_help
* enter_data{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_store_problem_description
    - slot{"problem_description": "pip"}
    - utter_direct_to_forum_for_help
    - utter_direct_to_step4
* install_rasa
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step4
* how_to_get_started
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout

## Generated Story goal:1 step, id:f4680c9ddacb4b81a2669a39b5862065, 1/17/2019 8187327133369364489
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* affirm
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
* affirm
    - utter_quickstart
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
    - utter_direct_step3
* get_started_step3
    - action_greet_user
    - slot{"step": "3"}
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
    - utter_direct_step3
* enter_data
    - action_greet_user
* out_of_scope
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* deny
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* deny
    - utter_nohelp
* out_of_scope
    - action_default_ask_affirmation
* out_of_scope
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: out_of_scope
    - form: feedback_form
    - slot{"feedback_message": ".."}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* enter_data
    - action_chitchat
* enter_data{"number": 12}
    - utter_not_sure
    - utter_possibilities
* enter_data{"number": 10000}
    - action_store_problem_description
    - slot{"problem_description": "10000"}
    - utter_direct_to_forum_for_help
    - utter_direct_to_step4
* enter_data{"amount-of-money": 10}
    - utter_not_sure
    - utter_possibilities
* enter_data
    - utter_not_sure
    - utter_possibilities

## Generated Story goal:1 step, id:1d0cde95693545c7b90eb59519261521, 1/17/2019 -7875375942282893765
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
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
    - utter_quickstart_nlu_only
    - utter_anything_else
* ask_weather
    - action_chitchat
* ask_time
    - action_chitchat
* enter_data
    - action_default_ask_affirmation
* ask_faq_languages
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_faq_languages
    - action_faqs
* out_of_scope
    - action_default_ask_affirmation
* react_negative
    - action_revert_fallback_events
    - rewind
    - rewind
* react_negative
    - utter_react_negative
* enter_data{"number": 8}
    - utter_not_sure
    - utter_possibilities

## Generated Story goal:chitchat, id:bcfc47ddc1ea4ad4924b07f7a1bc1906, 1/21/2019 1224248502435864843
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat

## Generated Story goal:sales, id:d3f8c55df53b474090f006b27cb3fc44, 1/17/2019 7908576531261852000
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* ask_howdoing
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction

## Generated Story goal:3 step, id:fdfb547d2c9d46718c302d5afb09a5a7, 1/17/2019 8579901162986307660
* get_started_step3
    - action_greet_user
    - slot{"shown_privacy": true}
* install_rasa
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* install_rasa
    - utter_get_starter_pack
    - utter_direct_to_step4
    - utter_anything_else
* install_rasa
    - utter_ask_python_installed
* deny
    - utter_get_python
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step4
    - utter_anything_else
* install_rasa
    - action_select_installation_command
    - utter_ask_ready_to_build
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_store_problem_description
    - slot{"problem_description": "i don't have pip"}
    - utter_direct_to_forum_for_help
    - utter_direct_to_step4
* install_rasa
    - utter_ask_python_installed
* deny
    - utter_get_python
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build

## Generated Story goal:chitchat, id:7875335dadee450ebedb65f7b7d953c4, 1/17/2019 -6941617494270426218
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_howdoing
    - action_chitchat
* ask_howold
    - action_chitchat
* ask_whatspossible
    - action_chitchat

## Generated Story goal:chitchat, id:5a2b952a2a2e40b79ffad27d677394a3, 1/17/2019 -4301117471664301348
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* handleinsult
    - action_chitchat
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny{"number": 1}
    - action_default_ask_affirmation

## Generated Story goal:oos, id:2205ba7e0a51493a87556de8fbbebaf5, 1/21/2019 -8331117403531210884
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_isbot
    - action_chitchat
* ask_why_contribute
    - action_default_ask_affirmation

## Generated Story goal:oos, id:5d105ffb029a49ed81fa018b0f3eca19, 1/21/2019 4526405120276826591
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* affirm
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
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* enter_data
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* out_of_scope
    - action_default_ask_affirmation
* enter_data
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
    - rewind
    - rewind
* enter_data
    - action_store_usecase
    - slot{"use_case": "which is the LNU asynchronism ?"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 0}
    - action_store_budget
    - slot{"budget": "0"}
    - utter_sales_contact
    - utter_ask_name
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* deny
    - utter_thumbsup
* bye
    - utter_bye

## Generated Story goal:oos, id:de216e50de4c4ff4a5b8ed0fb74a26e6, 1/21/2019 8103667558216051675
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* pipeline_recommendation
    - action_chitchat
* out_of_scope
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_default_ask_affirmation
* pipeline_recommendation
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
    - rewind
    - rewind
* pipeline_recommendation
    - action_chitchat

## Generated Story goal:1 step, id:91fdceb3d46e4fcd97cd799ccbc5f140, 1/21/2019 7750376655925581632
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* affirm
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
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu

## Generated Story goal:3 step, id:cf97f9a619fc4499aec02913a3af97ec, 1/21/2019 -7428466196972691692
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* install_rasa
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* affirm
    - utter_ask_describe_problem
* enter_data{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - action_store_problem_description
    - slot{"problem_description": "conda"}
    - utter_direct_to_forum_for_help
    - utter_direct_to_step4
* enter_data{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* out_of_scope
    - action_default_ask_affirmation
* install_rasa
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
    - rewind
    - rewind
* install_rasa
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda
* out_of_scope
    - action_default_ask_affirmation
* install_rasa
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: install_rasa
    - form: feedback_form
    - slot{"feedback_message": "how to install rasa"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart
    - restart
* install_rasa
    - utter_ask_python_installed
* deny
    - utter_get_python
    - utter_ask_pip_or_conda

## Generated Story goal:chitchat, id:a4c4f272c8c84e7fb4dbc39da817ad4c, 1/17/2019 -186258698547404555
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_which_events
    - action_default_ask_affirmation
* ask_isbot
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_isbot
    - action_chitchat
* ask_time
    - action_chitchat

## Generated Story goal:1 step, id:e4656a2c31284236bf171526035120e8, 1/17/2019 -3263251592600618020
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_whatspossible
    - action_default_ask_affirmation
* ask_whatspossible
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_whatspossible
    - action_chitchat
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
* affirm
    - utter_quickstart

## Generated Story goal:1 step, id:7779b3cfd6b5490987ad97187a9ee7d1, 1/21/2019 -7278276833542344557
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else

## Generated Story goal:subscribe, id:147d393c027548419fe17336f99bc035, 1/17/2019 8283729657769865684
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_time
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* enter_data
    - action_default_ask_affirmation
* enter_data
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
    - rewind
    - rewind
* enter_data
    - utter_not_sure
    - utter_possibilities
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "no@gmail.com"}
    - slot{"email": "no@gmail.com"}
    - action_store_email
    - slot{"email": "no@gmail.com"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* deny
    - utter_thumbsup
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:chitchat, id:a68ca108b64f472a80029812b28434a6, 1/17/2019 2154844902595340358
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* nicetomeeyou
    - action_chitchat
* ask_wherefrom
    - action_chitchat

## Generated Story goal:sales, id:54fc2e35242c48b9aebcbc5ba30ef2ec, 1/21/2019 -6009149791961527670
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "founder"}
    - utter_ask_usecase

## Generated Story goal:1 step, id:d151bcf3c1814c8aa27e3b3f8e74ee96, 1/17/2019 3698557900280193396
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_whatisrasa
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - action_default_ask_affirmation
* affirm
    - action_revert_fallback_events
    - rewind
    - rewind
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else
* how_to_get_started
    - utter_switch_dialogflow
    - utter_anything_else
* how_to_get_started
    - utter_core_tutorial
    - utter_anything_else

## Generated Story goal:1 step, id:db1138da5cdc4d93ba7a005f317e71ad, 1/17/2019 -3526295212200092928
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started
    - utter_explain_nlu
    - utter_also_explain_core
* affirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else

## Generated Story goal:1 step, id:6c0ffe5199d041a9b46a289858ea3465, 1/17/2019 1279779274023163116
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
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

## Generated Story goal:oos, id:33a424d9652d4849a050d71e0e87a760, 1/21/2019 564695357239455892
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_how_contribute
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* enter_data
    - action_default_ask_affirmation
* out_of_scope
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}

## Generated Story goal:4 step, id:285148ade0054c4ea41defb13fb1af35, 1/17/2019 -8477420856448046153
* get_started_step3
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "3"}
* ask_howdoing
    - action_chitchat
* ask_faq_opensource
    - action_faqs
* ask_faq_community_size
    - action_default_ask_affirmation
* ask_faq_community_size
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: ask_howdoing
    - form: feedback_form
    - slot{"feedback_message": "How can I get touch with you?"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thank
    - utter_noworries
    - utter_anything_else
* deny
    - utter_thumbsup

## Generated Story goal:1 step, id:a44cb258eef542499a3216e492ae37c2, 1/17/2019 -812360895569522996
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_whatisrasa
    - action_chitchat
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
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
    - utter_direct_step3

## Generated Story goal:chitchat, id:6b24337fdd8c4457ad89a90472a4d3aa, 1/17/2019 8539871011768027171
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_whatisrasa
    - action_chitchat

## Generated Story goal:1 step, id:ca2e56178d0548c397765d3a0b554ea9, 1/21/2019 8289873301727816304
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore

## Generated Story goal:1 step, id:3adedf5d7b464c0a8853bccb8d495139, 1/21/2019 -7711324942145573685
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout

## Generated Story goal:oos, id:34a6b74d46c54cd586e2e7ac96e59817, 1/21/2019 5930284899517468410
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_whatisrasa
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_builder
    - action_chitchat
* out_of_scope
    - action_default_ask_affirmation

## Generated Story goal:chitchat, id:a3bf9b2181fa4fa8a8def9f6a2759492, 1/17/2019 -9082285897154099542
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_greet_user
* ask_whatisrasa
    - action_chitchat

## Generated Story goal:1 step, id:68ea147cf1004bc3a00663e2f028de3f, 1/17/2019 -2013527539277877927
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* out_of_scope
    - action_default_ask_affirmation
* install_rasa
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: ask_question_in_forum
    - form: feedback_form
    - slot{"feedback_message": "ask questions"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story goal:oos, id:c117fcb81e7d4ff8a8d88214f8b8d350, 1/17/2019 8180641022767921864
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* ask_faq_languages
    - action_faqs
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* affirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* deny
    - utter_nohelp
* bye
    - utter_bye

