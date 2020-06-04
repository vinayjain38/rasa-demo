>> feedback + thanks
    - ...
    - utter_ask_feedback
* thank
    - utter_noworries
    - utter_anything_else

>> feedback + out_of_scope
    - ...
    - utter_ask_feedback
* out_of_scope
    - utter_thumbsup
    - utter_anything_else

>> feedback + enter_data
    - ...
    - utter_ask_feedback
* enter_data
    - utter_thumbsup
    - utter_anything_else

>> feedback + positive
    - ...
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - action_tag_feedback
    - utter_great
    - utter_anything_else

>> feedback + negative
    - ...
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - action_tag_feedback
    - utter_thumbsup
    - utter_anything_else

>> feedback + affirm
    - ...
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

>> feedback + deny
    - ...
    - utter_ask_feedback
* deny
    - utter_thumbsup
    - utter_anything_else