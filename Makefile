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

train-nlu:
	python3 -m rasa_nlu.train -c nlu_tensorflow.yml --fixed_model_name current --data train.md -o models --project nlu --verbose

train-tuned:
	python3 -m rasa_nlu.train -c nlu_tensorflow.yml --fixed_model_name tuned --data train.md -o models --project nlu --verbose

eval-current:
	python3 -m rasa_nlu.evaluate -m models/nlu/tuned --report tuned --errors tuned/errors.json -d test.md

train-core:
	python3 -m rasa_core.train -d domain.yml -s data/core -c policy.yml --debug -o models/dialogue --augmentation 0

train-memo:
	python -m rasa_core.train -d domain.yml -s data/core -c augmentedmemo-only.yml -o models/dialogue --augmentation 0

run-bert:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/bert --endpoints endpoints.yml

run-innatis:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/innatis --endpoints endpoints.yml

run-LRinnatis:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/innatis-full --endpoints endpoints.yml --debug

serve-innatis:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/innatis-full --credentials credentials.yml --debug --port 5555

serve-spacy:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/spacy --credentials credentials.yml --debug --port 5555

serve-current:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --credentials credentials.yml --debug --port 5555

run-cmdline:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --endpoints endpoints.yml

visualize:
	python3 -m rasa_core.visualize -s data/core/ -d domain.yml -o story_graph.png

train-online:
	python -m rasa_core.train -u models/nlu/current/ --online --core models/dialogue/

evaluate-core:
	python -m rasa_core.evaluate --core models/dialogue -s data/core/ --fail_on_prediction_errors

train-bert:
	python3 -m rasa_nlu.train -c bert_config.yml --fixed_model_name bert --data train.md -o models --project nlu --verbose

eval-bert:
	python3 -m rasa_nlu.evaluate -m models/nlu/bert --report -d test.md

train-innatis:
	python3 -m rasa_nlu.train -c innatis-config.yml --fixed_model_name innatis --data train.md -o models --project nlu --verbose

train-innatis-random:
	python3 -m rasa_nlu.train -c inn.yml --fixed_model_name innatis_random --data train.md -o models --project nlu --verbose

train-innatis-full:
	python3 -m rasa_nlu.train -c innatis-config.yml --fixed_model_name innatis-full --data train.md -o models --project nlu --verbose

train-spacy:
	python3 -m rasa_nlu.train -c spacy.yml --fixed_model_name spacy --data train.md -o models --project nlu --verbose

eval-inn:
	python3 -m rasa_nlu.evaluate -m models/nlu/innatis_random -d test.md --report random_report --errors random_errors.json

eval-spacy:
	python3 -m rasa_nlu.evaluate -m models/nlu/spacy -d test.md --report spacy_report.json --errors spacy_errors.json

eval-LRinnatis:
	python3 -m rasa_nlu.evaluate -m models/nlu/innatis-full -d test.md --report LRinnatis-report --errors LRinnatis_errors.json
