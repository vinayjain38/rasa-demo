#!/usr/bin/env bash
rasa test nlu --nlu data/nlu/new_format/response_splits/test_data.md --include_test_intent 1 --successes success.json 
# --report results/run2
