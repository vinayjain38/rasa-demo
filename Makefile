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
	python3 -m rasa_core_sdk.endpoint --actions actions

train-core:
	python3 -m rasa_core.train -d domain.yml -s data/core -c policy.yml --debug -o models/dialogue --augmentation 0

train-memo:
	python -m rasa_core.train -d domain.yml -s data/core -c augmentedmemo-only.yml -o models/dialogue --augmentation 0

run-innatis:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/innatis --endpoints endpoints.yml

serve-innatis:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/innatis-full --credentials credentials.yml --debug --port 5555

serve-spacy:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/spacy --credentials credentials.yml --debug --port 5555

serve-current:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --credentials credentials.yml --debug --port 5555

evaluate-core:
	python -m rasa_core.evaluate --core models/dialogue -s data/core/ --fail_on_prediction_errors

train-innatis:
	python3 -m rasa_nlu.train -c innatis-config.yml --fixed_model_name innatis --data train.md -o models --project nlu --verbose

eval-inn:
	python3 -m rasa_nlu.evaluate -m models/nlu/innatis -d test.md --report innatis_report --errors innatis_errors.json

eval-spacy:
	python3 -m rasa_nlu.evaluate -m models/nlu/spacy -d test.md --report spacy_report.json --errors spacy_errors.json