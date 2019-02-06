## Generated Story goal:1 step, id:d1f0cdf624a74a2ea7323b0817353037, 12/15/18 1731815793411691019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started
    - getstarted_1_success: action_default_fallback
    - rewind
* how_to_get_started
    - getstarted_1_success: utter_quickstart_nlu_only -> fail
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_default_fallback
    - rewind
* enter_data
    - chitchat: action_default_fallback
    - rewind

## Generated Story goal:oos, id:697db34a22db4c089e85f2c9ae3ee88f, 05/01/19 8439639792622345614
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: action_default_ask_affirmation

## Generated Story goal:chitchat, id:ada5f58b5ea4436fb1993578ca7fc805, 12/15/18 8327066330043087187
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* ask_weather{"name": "New York"}
    - slot{"name": "New York"}
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:4f647cb2427c495dbff5cf6fa1d7feb9, 12/15/18 -1171376024735749581
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: action_greet_user -> fail
    - getstarted_1: utter_stack_details -> fail
    - getstarted_1: utter_anything_else -> fail
* affirm
    - chitchat: utter_quickstart -> fail
    - chitchat: utter_anything_else -> fail

## Generated Story goal:1 step, id:99ca2d48ec6b4563a09b13303f4b6960, 12/17/18 4281123642591350586
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_getstarted -> fail
    - onboarding: utter_first_bot_with_rasa -> fail
* affirm
    - getstarted_1: action_set_onboarding -> fail
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before -> fail
* affirm
    - getstarted_1: utter_ask_migration -> fail
* deny
    - getstarted_1: utter_explain_stack -> fail
    - getstarted_1: utter_stack_details -> fail
    - getstarted_1: utter_explain_nlucore -> fail
* telljoke
    - chitchat: action_chitchat
    - getstarted_1: utter_explain_nlucore -> fail

## Generated Story goal:chitchat, id:debe18e2325840aeb5313ad18a27fa42, 05/01/19 1747852281231103127
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_isbot
    - chitchat: action_chitchat
* bye
    - chitchat: utter_bye

## Generated Story goal:chitchat, id:624b61bee53b411bac4a3855343dd0c7, 12/15/18 -8806002753186605917
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_thumbsup
* out_of_scope
    - oos: action_default_fallback
    - rewind
* ask_howold
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:bfdc18480a8a48e19aacf281bdd5db46, 05/01/19 9082912409352129743
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatisrasa{"language": "Japanese"}
    - slot{"language": "Japanese"}
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* ask_faq_languages
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* ask_faq_languages
    - faq: action_faqs
* enter_data{"language": "Japanese"}
    - slot{"language": "Japanese"}
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* enter_data
    - chitchat: action_chitchat -> fail
    - getstarted_1: utter_ask_migration
* ask_whatisrasa
    - chitchat: action_default_ask_affirmation

## Generated Story goal:chitchat, id:455210c2c7c9471194a7faaf2e63579f, 12/15/18 7957735631208973079
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: action_default_fallback
    - rewind
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* ask_isbot
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:9724aac6adda47a38271574fddb1529d, 05/01/19 6727944383445682358
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: action_default_ask_affirmation
* ask_faq_platform
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_faq_platform
    - faq: action_faqs
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: action_default_ask_affirmation
* affirm
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout

## Generated Story goal:1 step, id:2f822433f6a9427c8bff569c676d824e, 12/15/18 -6375541493127917237
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* handleinsult
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities -> fail
* enter_data
    - chitchat: utter_possibilities -> fail
* enter_data
    - chitchat: utter_possibilities -> fail
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp
* ask_whoisit
    - chitchat: action_chitchat

## Generated Story goal:oos, id:47f2fe45cd5f463cbaf2bc72def8f569, 05/01/19 -763810754505424450
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* out_of_scope
    - oos: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* install_rasa
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_thumbsup
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp

## Generated Story goal:chitchat, id:0f8142515810483a8c2e777909c37c2c, 12/17/18 -8573563216604908022
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whoisit
    - chitchat: action_chitchat
* telljoke
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_select_installation_command -> fail
    - getstarted_3: utter_ask_ready_to_build -> fail
* enter_data
    - getstarted_3: action_store_problem_description -> fail
    - slot{"problem_description": "i have installed rasa_core"}
    - getstarted_3_success: utter_direct_to_forum_for_help -> fail
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_ask_which_product -> fail
* affirm
    - chitchat: utter_thumbsup
    - getstarted_1: action_listen -> fail
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - rasa_help_success: utter_core_tutorial
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:db1d15d9e40047ebb3e8c13bbd0810b3, 12/15/18 2742610268326907746
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore

## Generated Story goal:3 step, id:f509c57ec8014ac9b4bd1eb7fde32f87, 12/17/18 -6498136812331561160
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_what_help -> fail
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* install_rasa{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities -> fail
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: action_select_installation_command -> fail
    - getstarted_3: utter_ask_ready_to_build -> fail
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user -> fail
* bye
    - chitchat: action_default_fallback
    - rewind
* technical_question
    - faq: action_default_fallback
    - rewind
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: action_greet_user -> fail
    - getstarted_1: utter_stack_details -> fail
    - utter_anything_else -> fail
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* ask_howdoing
    - chitchat: action_default_fallback
    - rewind
* handleinsult
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: action_default_fallback
    - rewind
* enter_data
    - chitchat: action_default_fallback
    - rewind
* bye
    - chitchat: utter_bye
* nlu_info
    - rasa_help: action_default_fallback
    - rewind
* deny
    - chitchat: action_default_fallback
    - rewind

## Generated Story goal:1 step, id:84082ae966d64d0ca415b276c3635916, 12/15/18 -5644677460292251299
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:79e8dd05329946a8963c170d920e0144, 05/01/19 -5283482436135596936
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: utter_ask_migration -> fail
* enter_data
    - chitchat: utter_contact_email -> fail
* ask_howdoing
    - chitchat: action_default_ask_affirmation
* telljoke
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* telljoke
    - chitchat: action_chitchat
* telljoke
    - chitchat: action_chitchat
* react_negative
    - chitchat: action_default_ask_affirmation
* ask_faq_channels
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_faq_channels
    - faq: action_faqs
* technical_question
    - faq: action_default_ask_affirmation
* how_to_get_started
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* ask_whatspossible
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else

## Generated Story goal:chitchat, id:e14eddaf8dc14ff7bb8104696c4eb1d2, 05/01/19 7896940127074527179
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_whatisrasa
    - chitchat: action_chitchat

## Generated Story goal:chitchat, id:94f6b465ee3e4a9297dcf1ed5ed22c27, 12/17/18 -2986161335647465616
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:cfa8bb9deaf0427498c662745431a282, 12/15/18 -56217783078242536
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_greet_user -> fail
* enter_data
    - chitchat: utter_possibilities -> fail
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp
* deny
    - chitchat: utter_nohelp
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp

## Generated Story goal:1 step, id:16439d767388463d93e9c827767bca96, 05/01/19 -5426994757726665781
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* greet
    - greet_success: action_greet_user

## Generated Story goal:chitchat, id:f509c57ec8014ac9b4bd1eb7fde32f87, 12/17/18 -6498136812331561160
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_what_help -> fail
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* install_rasa{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## Generated Story goal:chitchat, id:9e785c9f586b48b7affc592dd2d499fb, 12/17/18 8538685554217994801
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities -> fail

## Generated Story goal:oos , id:5a1c8e47b3ba4dc38b2a3de3ffedee30, 12/17/18 4221492392327213787
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* ask_whoisit
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* deny
    - chitchat: utter_thumbsup -> fail
    - rasa_help: action_listen -> fail
* ask_whatspossible
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:fe9205767e5540319511248ba2d7aa7d, 12/15/18 -1169614020695031757
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user -> fail

## Generated Story goal:1 step, id:de903a69d7524115a8affa517ba1df0c, 12/15/18 4546830120439352871
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"name": "sara"}
    - slot{"name": "sara"}
    - getstarted_1: action_default_fallback
    - rewind
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: action_default_fallback
    - rewind
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started
    - getstarted_1: action_chitchat -> fail
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1: utter_explain_nlu  -> fail
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout

## Generated Story goal:1 step, id:f425b3ba996e4eaeacbc82becd473dbf, 12/17/18 4246660389998784195
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* ask_whoisit
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* ask_whatspossible
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* ask_whatspossible
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities -> fail
