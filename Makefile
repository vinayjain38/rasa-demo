.PHONY: clean test lint

TEST_PATH=./

help:
	@echo "    train-nlu"
	@echo "        Train the natural language understanding using Rasa NLU."
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."
	@echo "    run-cmdline"
	@echo "        Starts the bot on the command line"
	@echo "    visualize"
	@echo "        Saves the story graphs into a file"

run-actions:
	python3 -m rasa_core_sdk.endpoint --actions demo.actions

train-nlu:
	python3 -m rasa_nlu.train -c nlu_tensorflow.yml --fixed_model_name current --data data/nlu/ -o models --project nlu --verbose

train-core-0:
	python3 -m rasa_core.train -d domain.yml -s data/core -c policy.yml --debug -o models/dialogue

train-core:
	python3 -m rasa_core.train -d domain.yml -s data/new_fail/train_goal.md -c policy.yml --debug -o models/dialogue --augmentation 0

train-core-2:
	python3 -m rasa_core.train -d domain.yml -s data/core-success/ -c policy.yml --debug -o models/dialogue --augmentation 0

train-core-3:
	python3 -m rasa_core.train -d domain.yml -s data/new_fail -c policy.yml --debug -o models/dialogue --augmentation 0

run-cmdline:
	make run-actions&
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug --endpoints endpoints.yml

visualize:
	python3 -m rasa_core.visualize -s data/core/ -d domain.yml -o story_graph.png

train-online:
	python3 -m rasa_core.train -u models/nlu/current/ --online --core models/dialogue/

evaluate-core-0:
	python3 -m rasa_core.evaluate --core models/dialogue -s data/core

evaluate-core-01:
	python3 -m rasa_core.evaluate --core models/dialogue -s data/new_fail/

evaluate-core:
	python3 -m rasa_core.evaluate --core models/dialogue -s data/new_fail/train_goal.md

evaluate-core-1:
	python3 -m rasa_core.evaluate --core models/dialogue -s data/new_fail/test_goal.md

evaluate-core-2:
	python3 -m rasa_core.evaluate --core models/dialogue -s data/core-success/ --topics

evaluate-core-3:
	python3 -m rasa_core.evaluate --core models/dialogue -s data/success/test_for_success.md --topics

evaluate-core-4:
	python3 -m rasa_core.evaluate --core models/dialogue -s data/success/test_new_for_success.md --topics