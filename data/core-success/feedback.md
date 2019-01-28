## feedback1
    - feedback: utter_ask_feedback
* out_of_scope
    - feedback_success: utter_thumbsup
    - chitchat: utter_anything_else


## feedback2
    - feedback: utter_ask_feedback
* enter_data
    - feedback_success: utter_thumbsup
    - chitchat: utter_anything_else

## feedback3
    - feedback: utter_ask_feedback
* affirm
    - feedback_success: utter_great
    - chitchat: utter_anything_else

## feedback deny
    - feedback: utter_ask_feedback
* deny
    - feedback_success: utter_thumbsup
    - chitchat: utter_anything_else

## feedback thumbsup
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - feedback_success: utter_thumbsup
    - chitchat: utter_anything_else

## feedback thumbsup
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
