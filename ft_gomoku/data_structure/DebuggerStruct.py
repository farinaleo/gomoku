import time
import psutil
import platform, subprocess, re
from dataclasses import dataclass
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
		self.opponent_turn = game_engine.get_opponent_turn()
		self.total_time = game_engine.time
		self.total_time_player_1 = game_engine.total_time_player_1
		self.total_time_player_2 = game_engine.total_time_player_2
		self.captured_stones = game_engine.grid.captured_stones

		#System information
		if platform.system() == "Windows":
			self.cpu_info = platform.processor()
		elif platform.system() == "Linux":
			command = "cat /proc/cpuinfo"
			all_info = subprocess.check_output(command, shell=True).decode().strip()
			for line in all_info.split("\n"):
				if "model name" in line:
					self.cpu_info = re.sub(".*model name.*:", "", line, 1)
		self.cpu_freq = ""
		self.ram_total = 0
		self.ram_used = 0

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
		self.opponent_turn = game_engine.get_opponent_turn()
		self.total_time = game_engine.time
		self.total_time_player_1 = game_engine.total_time_player_1
		self.total_time_player_2 = game_engine.total_time_player_2
		self.captured_stones = game_engine.grid.captured_stones

	def update_cpu_info(self):
		"""Update the cpu information in the debugger struct"""
		self.cpu_freq = psutil.cpu_freq(True)[0][0]

	def update_ram_info(self):
		"""Update the ram information in the debugger struct"""
		self.ram_total = round((psutil.virtual_memory().total / (1024 ** 3)), 2)
		self.ram_used = round((psutil.virtual_memory().used / (1024 ** 3)), 2)

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
			"opponent_turn": self.opponent_turn,
			"total_time": time.time() - self.total_time,
			"total_time_player_1": self.total_time_player_1,
			"total_time_player_2": self.total_time_player_2,
			"captured_stones": self.captured_stones,
			"cpu_info": self.cpu_info,
			"cpu_freq": self.cpu_freq,
			"ram_total": self.ram_total,
			"ram_used": self.ram_used
		}
