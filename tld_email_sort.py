#!/usr/bin/env python3
import re
import os
import sys

try:
	os.mkdir('TLD SORTED')
except:
	pass
	
cwd = os.getcwd()
tlds = ['com', 'net', 'org', 'biz', 'info', 'pro', 'aero', 'coop', 'museum', 'online', 'name', 'edu', 'gov', 'mil', 'ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo', 'bq', 'br', 'bt', 'bw', 'by', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st', 'su', 'sv', 'sx', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'us', 'uy', 'uz', 'va', 'vc', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'za', 'zm', 'zw']

email_pattern = "[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
file_name = input('Enter file name: ')

with open(file_name, 'r', encoding='utf8') as input_file:
	content = str(input_file.read())

	for tld in tlds:
		# pattern = f'^.*@.*\.{tld}$'
		# pattern = f'^[a-zA-Z0-9._%-]+@.*\.{tld}$'
		pattern = f'[a-zA-Z0-9._%-]+@.*\.{tld}'
		if re.search(pattern, content, re.MULTILINE):
			print(f"Currently on .{tld.upper()}")
			matches = re.findall(pattern, content, re.MULTILINE)
			# new_content = re.sub(pattern, "", content, re.MULTILINE)

			with open(f'{cwd}\\tld SORTED\\.{tld.upper()}.txt', 'a', encoding='utf8') as tld_file:
				tld_file.write('\n'.join(matches))

	# others = re.findall(email_pattern, content, flags = re.DOTALL)
	new_content = re.sub(pattern, "", content, flags = re.MULTILINE)
	others = re.findall(email_pattern, new_content)

with open(f'{cwd}\\tld SORTED\\NON_tld.txt', 'a', encoding='utf8') as non_tld_file:
	# non_tld_file.write('\n'.join(others))
	non_tld_file.write(new_content)
    