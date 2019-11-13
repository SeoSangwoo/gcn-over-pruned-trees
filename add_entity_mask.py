import json
import copy

filenames = {"dev", "test", "train"}

for filename in filenames:
	with open("./dataset/semeval/" + filename + ".json") as f:
		data = json.load(f)
	data_list = []
	for d in data:
		tokens = list(d['token'])
		ss, se = d['subj_start'], d['subj_end']
		os, oe = d['obj_start'], d['obj_end']
		ori_tokens = copy.deepcopy(tokens)
		convert_token = [0] * len(ori_tokens)
		tokens.insert(ss, "e11")
		tokens.insert(se+2, "e12")
		tokens.insert(os+2, "e21")
		tokens.insert(oe+4, "e22")
		k = 0
		for i, word in enumerate(tokens):
			if ori_tokens[k] == word:
				convert_token[k] = i
				k += 1
			if k == len(convert_token):
				break
		head = d["stanford_head"]
		new_head = copy.deepcopy(head)
		for i in range(len(new_head)):
			if new_head[i] != 0:
				new_head[i] = convert_token[new_head[i] - 1] + 1
		d["stanford_pos"].insert(ss, "e11")
		d["stanford_pos"].insert(se+2, "e12")
		d["stanford_pos"].insert(os+2, "e21")
		d["stanford_pos"].insert(oe+4, "e22")
		d["stanford_ner"].insert(ss, "e11")
		d["stanford_ner"].insert(se+2, "e12")
		d["stanford_ner"].insert(os+2, "e21")
		d["stanford_ner"].insert(oe+4, "e22")
		# d["stanford_head"].insert(ss, ss+2)
		# d["stanford_head"].insert(se+2, se+2)
		# d["stanford_head"].insert(os+2, os+4)
		# d["stanford_head"].insert(oe+4, oe+4)
		# for i, token in enumerate(tokens):
		# 	if token != "e11" and token != "e12" and token != "e21" and token != "e22":
		# 		index = d["stanford_head"][i]
		# 		if index != 0 and ori_tokens[index-1] != tokens[index-1]:
		# 			d["stanford_head"][i] = tokens.index(ori_tokens[index-1]) + 1
		ss = ss + 1
		se = se + 1
		os = os + 3
		oe = oe + 3
		new_head.insert(ss - 1, ss + 1)
		new_head.insert(se + 1, se + 1)
		new_head.insert(os - 1, os + 1)
		new_head.insert(oe + 1, oe + 1)
		d["stanford_head"] = new_head
		d['subj_start'] = ss
		d['subj_end'] = se
		d['obj_start'] = os
		d['obj_end'] = oe
		d['token'] = tokens
		data_list.append(d)
	with open("./dataset/semeval/" + filename + ".json", 'w', encoding='utf-8') as f:
		json.dump(data_list, f, ensure_ascii=False, indent="\t")