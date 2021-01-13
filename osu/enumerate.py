"""
Description:

Author: LostPy
License: MIT
Date: 2021-01-11
"""


class Mods:
	none = 0
	no_fail = 1
	easy = 2
	touch_device = 4
	hidden = 8
	hard_rock = 16
	sudden_death = 32
	double_time = 64
	relax = 128
	half_time = 256
	nightcore = 512  # Only set along with DoubleTime. i.e: NC only gives 576
	flashlight = 1024
	autoplay = 2048
	spun_out = 4096
	relax2 = 8192  # Autopilot
	perfect = 16384  # Only set along with SuddenDeath. i.e: PF only gives 16416  
	key4 = 32768
	key5 = 65536
	key6 = 131072
	key7 = 262144
	key8 = 524288
	fade_in = 1048576
	random = 2097152
	cinema = 4194304
	target = 8388608
	key9 = 16777216
	key_coop = 33554432
	key1 = 67108864
	key3 = 134217728
	key2 = 268435456
	score_v2 = 536870912
	mirror = 1073741824

	@staticmethod
	def key_mod():
		return Mods.key1 | Mods.key2 | Mods.key3 | Mods.key4 | Mods.key5 | Mods.key6 | \
		Mods.key7 | Mods.key8 | Mods.key9 | Mods.key_coop
	
	@staticmethod
	def free_mod_allowed():
		return Mods.no_fail | Mods.easy | Mods.hidden | Mods.hard_rock | Mods.sudden_death | \
		Mods.flashlight | Mods.fade_in | Mods.relax | Mods.relax2 | Mods.spun_out | Mods.key_mod()
	
	@staticmethod
	def score_increase_mods():
		return Mods.hidden | Mods.hard_rock | Mods.double_time | Mods.flashlight | Mods.fade_in
