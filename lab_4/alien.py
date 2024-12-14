import random

import pygame


class Alien(pygame.sprite.Sprite):
	"""The user's enemies"""

	def __init__(self, type, x, y):
		super().__init__()
		self.type = type
		path = f"Graphics/alien_{type}.png"
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(topleft = (x, y))

	def update(self, direction):
		self.rect.x += direction


class MysteryShip(pygame.sprite.Sprite):
	"""An Unusual Enemy of the user"""

	def __init__(self, screen_width: int, offset:int) -> None:
		"""Create an object of the MysteryShip class"""
		super().__init__()
		self.screen_width = screen_width
		self.offset = offset
		self.image = pygame.image.load("Graphics/mystery.png")

		x = random.choice([self.offset/2, self.screen_width + self.offset - self.image.get_width()])
		if x == self.offset/2:
			self.speed = 3
		else:
			self.speed = -3

		self.rect = self.image.get_rect(topleft=(x, 90))

	def update(self) -> None:
		"""Update mystery ship status"""
		self.rect.x += self.speed
		if self.rect.right > self.screen_width + self.offset/2:
			self.kill()
		elif self.rect.left < self.offset/2:
			self.kill()
