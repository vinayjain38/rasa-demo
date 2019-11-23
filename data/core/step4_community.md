## Step 4 prompt
* get_started_step4
    - action_greet_user

## Happy path: Prompt -> Get event locations -> get next event
* get_started_step4
    - action_greet_user
* ask_which_events
    - action_get_community_events
* ask_when_next_event
    - action_get_community_events
    - utter_recommend_forum

## Happy path: Prompt -> Get event locations -> get next event for location
* get_started_step4
    - action_greet_user
* ask_which_events
    - action_get_community_events
* ask_when_next_event{"location": "Berlin"}
    - action_get_community_events
    - utter_recommend_forum

## Happy path: Get event locations -> get next event
* ask_which_events
    - action_get_community_events
* ask_when_next_event
    - action_get_community_events
    - utter_anything_else

## Happy path: Get event locations -> get next event for location
* ask_which_events
    - action_get_community_events
* ask_when_next_event{"location": "Berlin"}
    - action_get_community_events
    - utter_anything_else

## Prompt -> Get next event
* get_started_step4
    - action_greet_user
* ask_when_next_event
    - action_get_community_events
    - utter_recommend_forum

## Prompt -> Get next event for location
* get_started_step4
    - action_greet_user
* ask_when_next_event{"location": "Berlin"}
    - action_get_community_events
    - utter_recommend_forum

## Get next event
* ask_when_next_event
    - action_get_community_events
    - utter_anything_else

## Get next event for location
* ask_when_next_event{"location": "Berlin"}
    - action_get_community_events
    - utter_anything_else

## Prompt -> Contribute
* get_started_step4
    - action_greet_user
* ask
    - respond_ask
* ask
    - respond_ask

## Contribute
* ask
    - respond_ask
* ask
    - respond_ask

## Prompt -> How can I contribute
* get_started_step4
    - action_greet_user
* ask
    - respond_ask

## Prompt -> Get help in forum
* get_started_step4
    - action_greet_user
* ask
    - respond_ask

## Get help in the forum, How can I contribute
* ask
    - respond_ask
