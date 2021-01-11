"""
Description: A module with utility functions use in apiV1.py and apiV2.py
Author: LostPy
License: MIT
Date: 2021-01-11
"""
import json

try:
	import pandas as pd
	pandas_imported = True
except ImportError:
	pandas_imported = False


def from_json(text_json, type_return: str):
	"""A function to convert json result in a type specify"""
	if type_return == 'json':
		return r.text

	elif type_return == 'dict':
		return json.loads(text_json)

	elif type_return == 'dataframe':
		if pandas_imported:
			return pd.read_json(text_json)
		else:
			raise ValueError("type_return can't take 'dataframe' value if pandas is not installed! Install pandas and retry.")
	else:
		raise ValueError(f"type_return can't take the value: '{type_return}'. Possibles types: 'json', 'dict', 'dataframe'.")
