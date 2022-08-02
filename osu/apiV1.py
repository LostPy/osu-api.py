"""
Description: A Python module to use easily the osu!api V1.

Author: LostPy
License: MIT
Date: 2021-01-11
"""

import requests as req
import json

from . import from_json


base_url ='https://osu.ppy.sh/api'
urls = {
'beatmaps': base_url + '/get_beatmaps?',
'user': base_url + '/get_user?',
'scores': base_url + '/get_scores?',
'user_best': base_url + '/get_user_best?',
'user_recent': base_url + '/get_user_recent?',
'match': base_url + '/get_match?',
'replay': base_url + '/get_replay?'
}



def get_beatmaps(key: str, since: str = None, beatmapset_id: int = None, beatmap_id: int = None, type_return: str = 'dict', **kwargs):
	"""Retrieve general beatmap information."""
	params = {
	'k': key,
	'since': since,
	's': beatmapset_id,
	'b': beatmap_id,
	'u': kwargs['user'] if 'user' in kwargs else None,
	'type': kwargs['type_'] if 'type_' in kwargs else None,
	'm': kwargs['mode'] if 'mode' in kwargs else None,
	'a': kwargs['a'] if 'a' in kwargs else 0,
	'h': kwargs['h'] if 'h' in kwargs else None,
	'limit': kwargs['limit'] if 'limit' in kwargs else 500,
	'mods': kwargs['mods'] if 'mods' in kwargs else None}
	r = req.get(urls['beatmaps'], params=params)
	return from_json(r.text, type_return)


def get_user(key: str, user: int, type_return: str = 'dict', **kwargs):
	"""Retrieve general user information."""
	params = {
	'k': key,
	'u': user,
	'm': kwargs['mode'] if 'mode' in kwargs else 0,
	'type': kwargs['type_'] if 'type_' in kwargs else None,
	'event_days': kwargs['event_days'] if 'event_days' in kwargs else 1}
	r = req.get(urls['user'], params=params)
	return from_json(r.text, type_return)


def get_scores(key: str, beatmap_id: int, user: int = None, type_return: str = 'dict', **kwargs):
	"""Retrieve information about the top 100 scores of a specified beatmap."""
	params = {
	'k': key,
	'b': beatmap_id,
	'u': user,
	'm': kwargs['mode'] if 'mode' in kwargs else 0,
	'mods': kwargs['mods'] if 'mods' in kwargs else 0,
	'type': kwargs['type_'] if 'type_' in kwargs else None,
	'limit': kwargs['limit'] if 'limit' in kwargs else 50}
	r = req.get(urls['scores'], params=params)
	return from_json(r.text, type_return)


def get_user_best(key: str, user: int, mode: int = 0, limit: int = 10, type_: str = None, type_return: str = 'dict'):
	"""Get the top scores for the specified user."""
	params = {
	'k': key,
	'u': user,
	'm': mode,
	'limit': limit,
	'type': type_}
	r = req.get(urls['user_best'], params=params)
	return from_json(r.text, type_return)


def get_user_recent(key: str, user: int, mode: int = 0, limit: int = 10, type_: str = None, type_return: str = 'dict'):
	"""Gets the user's ten most recent plays over the last 24 hours."""
	params = {
	'k': key,
	'u': user,
	'm': mode,
	'limit': limit,
	'type': type_}
	r = req.get(urls['user_recent'], params=params)
	return from_json(r.text, type_return)


def get_match(key: str, match_id: int, type_return: str = 'dict'):
	"""Retrieve information about multiplayer match."""
	r = req.get(urls['match'], {'k': key, 'mp': match_id})
	return from_json(r.text, type_return)


def get_replay(key: str, beatmap_id: int, user: int, **kwargs):
	"""Get the replay data of a user's score on a map."""
	params = {
	'k': key,
	'b': beatmap_id,
	'u': user,
	'm': kwargs['mode'] if 'mode' in kwargs else None,
	's': kwargs['score_id'] if 'score_id' in kwargs else None,
	'type_': kwargs['type_'] if 'type_' in kwargs else None,
	'mods': kwargs['mods'] if 'mods' in kwargs else None}
	return json.loads(req.get(urls['replay'], params=params).text)


def get_cover_image(beatmapset_id: int):
	"""Return url of cover image from beatmapset_id."""
	return f"https://assets.ppy.sh/beatmaps/{beatmapset_id}/covers/cover.jpg"


def get_profile_image(user_id: int):
	"""Return url of profile image of user."""
	return f"http://s.ppy.sh/a/{user_id}"

