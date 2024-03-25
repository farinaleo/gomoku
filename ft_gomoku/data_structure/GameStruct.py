import time
from ft_gomoku import Grid
from dataclasses import dataclass
from ft_gomoku.engine.image_control import get_image


@dataclass
class GameStruct:
	def __init__(self, size: int, player1, player2):
		self.grid = Grid(size + 1, player1, player2)
		self.player_1 = (player1, '1')
		self.player_2 = (player2, '2')
		self.grid_size = size
		self.player_turn = self.player_1
		self.time = 0
		self.board = []
		self.last_move = [None, None, None]
		self.rock_white_img = None
		self.rock_black_img = None
		self.rock_white_last_img = None
		self.rock_black_last_img = None
		self.rock_help_img = None
		self.total_time_player_1 = (0, 0, 0.0)
		self.total_time_player_2 = (0, 0, 0.0)
		self.list_time_player_1 = []
		self.list_time_player_2 = []
		self.winner = None

	def init_img(self, radius: int):
		"""Init the images
		:param radius: the radius of the rocks
		"""
		self.rock_white_img = get_image('rocks_white.png', radius, radius)
		self.rock_black_img = get_image('rocks_black.png', radius, radius)
		self.rock_black_last_img = get_image('rocks_black_last.png', radius, radius)
		self.rock_white_last_img = get_image('rocks_white_last.png', radius, radius)
		self.rock_help_img = get_image('rocks_help.png', radius, radius)

	def get_rocks_img(self, player: str, last: bool):
		"""Get the rock image of a player
		:param player: the player
		:param last: if the rock is the last one placed
		"""
		if player == '2':
			return self.rock_white_last_img if last else self.rock_white_img
		elif player == '1':
			return self.rock_black_last_img if last else self.rock_black_img
		else:
			return self.rock_help_img

	def set_winner(self, winner_player: str, rocks_winner: list[tuple[int, int]], win_type: str):
		"""Set the winner
		:param winner_player: winner player
		:param rocks_winner: the rocks that make the winner
		:param win_type: the type of win
		"""
		self.winner = (winner_player, rocks_winner, win_type)

	def get_winner(self):
		return self.winner

	def get_last_move(self):
		return self.last_move

	def set_last_move(self, last_move):
		self.last_move = last_move

	def add_square(self, square):
		self.board.append(square)

	def set_player_turn(self, player_turn: tuple[str, str]):
		"""Set the player turn
		:param player_turn: the player turn
		"""
		self.player_turn = player_turn

	def update_player_turn(self):
		"""Update the player turn"""
		if self.player_turn == ('0', '0'):
			self.player_turn = self.player_2 if self.last_move[0] == '2' else self.player_1
		self.player_turn = self.player_2 if self.player_turn == self.player_1 else self.player_1

	def start_player_timer(self, player: str):
		"""Start the timer for the player
		:param player:
		"""
		actual_time = time.time()
		if player == '1':
			self.total_time_player_1 = (self.total_time_player_1[0], self.total_time_player_1[1], actual_time)
		else:
			self.total_time_player_2 = (self.total_time_player_2[0], self.total_time_player_2[1], actual_time)

	def end_player_timer(self, player: str):
		"""End the timer for the player
		:param player:
		"""
		elapsed_time = time.time() - self.total_time_player_1[2] if player == '1' else time.time() - self.total_time_player_2[2]
		if player == '1':
			self.total_time_player_1 = (self.total_time_player_1[0] + elapsed_time, elapsed_time, 0.0)
			self.list_time_player_1.append(elapsed_time)
		else:
			self.total_time_player_2 = (self.total_time_player_2[0] + elapsed_time, elapsed_time, 0.0)
			self.list_time_player_2.append(elapsed_time)

	def get_player_turn(self):
		return self.player_turn

	def get_opponent_turn(self):
		return self.player_1 if self.player_turn == self.player_2 else self.player_2

	def set_time(self, time: float):
		self.time = time

	def update_time(self, time: float):
		self.time += time

	def get_time(self):
		return self.time

	def get_board_size(self):
		return self.grid_size
