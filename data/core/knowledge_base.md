## ask about products #1
* greet
    - action_greet_user
* what_products{"entity_type": "product"}
    - action_query_entities
* ask_product_details
    - action_request_info

## ask about products #2
* greet
    - action_greet_user
* ask_product_details
    - action_request_info

## ask about products #3
* greet
    - action_greet_user
* ask_whatisrasa
    - utter_ask_whatisrasa
* what_products{"entity_type": "product"}
    - action_query_entities
* ask_product_details
    - action_request_info

## ask about products #4
* greet
    - action_greet_user
* what_products{"entity_type": "product"}
    - action_query_entities
* ask_whatisrasa
    - utter_ask_whatisrasa
* ask_product_details
    - action_request_info

## ask about products #4
* greet
    - action_greet_user
* what_products{"entity_type": "product"}
    - action_query_entities
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
    
## ask about product details
* ask_product_details
    - action_request_info
    
## ask about products
* what_products{"entity_type": "product"}
    - action_query_entities
    
  