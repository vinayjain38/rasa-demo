import json

with open("errors.json") as f:
	bert_errors = f.read()
	bert_errors = json.loads(bert_errors)

with open("tuned/errors.json") as f:
	tuned_errors = f.read()
	tuned_errors = json.loads(tuned_errors)

tuned_list = [ex.get("text") for ex in tuned_errors]
bert_list = [ex.get("text") for ex in bert_errors]




bert_not_tuned = [str(ex) for ex in bert_list if ex not in tuned_list]
tuned_not_bert = [str(ex) for ex in tuned_list if ex not in bert_list]


print('bert mistakes', bert_not_tuned)


print('tuned mistakes', tuned_not_bert)
