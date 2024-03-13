from dataclasses import dataclass

import cpuinfo#TODO: add cpuinfo to requirements.txt
import psutil#TODO: add psutil to requirements.txt
from ft_gomoku.engine import Engine
from ft_gomoku.data_structure import GameStruct


@dataclass
class DebuggerStruct:

	def __init__(self, engine: Engine, game_engine: GameStruct):

		# Settings file
		self.max_fps: int = engine.settings.get_fps()
		self.music_option: bool = engine.settings.get_music()
		self.fullscreen_option: bool = engine.settings.get_fullscreen()
		self.window_size: tuple = engine.settings.get_window_size()

		# Engine
		self.current_screen: str = engine.current_screen
		self.running: bool = engine.running
		self.window_size: tuple = engine.window_size

		# Game information
		self.board_grid = game_engine.grid
		self.player_1 = game_engine.player_1
		self.player_2 = game_engine.player_2
		self.grid_size = game_engine.grid_size
		self.player_turn = game_engine.player_turn
		self.total_time_player_1 = game_engine.total_time_player_1
		self.total_time_player_2 = game_engine.total_time_player_2

		#System information
		self.python_version = ""
		self.cpu_info = ""
		self.cpu_cores = 0
		self.cpu_arch = ""
		self.cpu_freq = ""
		self.ram_total = 0
		self.ram_used = 0
		self.update_cpu_info()
		self.update_ram_info()

	def update_settings(self, engine: Engine, game_engine: GameStruct):
		"""Update the settings in the debugger struct
		:param engine: the engine
		:param game_engine: the game engine
		"""
		self.max_fps: int = engine.settings.get_fps()
		self.music_option: bool = engine.settings.get_music()
		self.fullscreen_option: bool = engine.settings.get_fullscreen()
		self.window_size: tuple = engine.settings.get_window_size()
		self.current_screen: str = engine.current_screen
		self.running: bool = engine.running
		self.window_size: tuple = engine.window_size
		self.board_grid = game_engine.grid
		self.player_1 = game_engine.player_1
		self.player_2 = game_engine.player_2
		self.grid_size = game_engine.grid_size
		self.player_turn = game_engine.player_turn
		self.total_time_player_1 = game_engine.total_time_player_1
		self.total_time_player_2 = game_engine.total_time_player_2

	def update_cpu_info(self):
		"""Update the cpu information in the debugger struct"""
		cpu_info = cpuinfo.get_cpu_info()
		if 'python_version' in cpu_info:
			self.python_version = cpu_info['python_version']
		if 'brand_raw' in cpu_info:
			self.cpu_info = cpu_info['brand_raw']
		if 'count' in cpu_info:
			self.cpu_cores = cpu_info['count']
		if 'arch' in cpu_info:
			self.cpu_arch = cpu_info['arch']
		if 'hz_actual_friendly' in cpu_info:
			self.cpu_freq = cpu_info['hz_actual_friendly']

	def update_ram_info(self):
		"""Update the ram information in the debugger struct"""
		self.ram_total = round((psutil.virtual_memory().total / (1024 ** 3)), 2)
		self.ram_used = round((psutil.virtual_memory().used / (1024 ** 3)), 2)

	def print_terminal(self):
		"""Print the debugger information in the terminal"""

		# print header stylized debugger message
		print("+" + "-" * 78 + "+")
		print("|" + " " * 78 + "|")
		print("|" + " " * 30 + "DEBUGGER" + " " * 40 + "|")
		print("|" + " " * 78 + "|")
		print("+" + "-" * 78 + "+")

		# print system information
		print(f"Python version: {self.python_version}")
		print(f"CPU: {self.cpu_cores}x {self.cpu_info} @ {self.cpu_freq} {self.cpu_arch}")
		print(f"RAM: {self.ram_used}/{self.ram_total}GB")

		# print settings file
		print(f"Max FPS: {self.max_fps}")
		print(f"Music: {'ON' if self.music_option else 'OFF'}")
		print(f"Fullscreen: {'ON' if self.fullscreen_option else 'OFF'}")
		print(f"Window size: {self.window_size}")

		# print engine information
		print(f"Current screen: {self.current_screen}")
		print(f"Running: {self.running}")
		print(f"Window size: {self.window_size}")

		# print game information
		print(f"Board grid: {self.board_grid}")
		print(f"Player 1: {self.player_1}")
		print(f"Player 2: {self.player_2}")
		print(f"Grid size: {self.grid_size} # Board size, add 1 for the grid size")
		print(f"Player turn: {self.player_turn}")
		print(f"Total time player 1: {self.total_time_player_1} # (total_time, last_time, tmp_start_time)")
		print(f"Total time player 2: {self.total_time_player_2} # (total_time, last_time, tmp_start_time)")

	def get_all_game_info(self, reload: bool = False):
		"""Get all the game information
		:param reload: if True, reload the cpu and ram information
		:return: all the game information (dict)
		"""
		if reload:
			self.update_cpu_info()
			self.update_ram_info()
		return {
			"music_option": self.music_option,
			"fullscreen_option": self.fullscreen_option,
			"window_size_settings": self.window_size,
			"current_screen": self.current_screen,
			"running": self.running,
			"window_size_engine": self.window_size,
			"board_grid": self.board_grid,
			"player_1": self.player_1,
			"player_2": self.player_2,
			"grid_size": self.grid_size,
			"player_turn": self.player_turn,
			"total_time_player_1": self.total_time_player_1,
			"total_time_player_2": self.total_time_player_2,
			"python_version": self.python_version,
			"cpu_info": self.cpu_info,
			"cpu_cores": self.cpu_cores,
			"cpu_arch": self.cpu_arch,
			"cpu_freq": self.cpu_freq,
			"ram_total": self.ram_total,
			"ram_used": self.ram_used
		}
