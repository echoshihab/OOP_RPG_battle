import random

#create weapons using this class
class weapon:
	def __init__(self, name, damage):
		self.name = name
		self.damage = damage

# create characters using this class
class character:
	def __init__(self, name, hp, attack, mod=0):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.mod = mod

	def main_attack(self):
		self.dmg = random.randint(1, self.attack) + self.mod
		print(f'{self.name} has caused {self.dmg} amount of damange')
		return self.dmg


goblin = character('Goblin', 40, 5)
sword = weapon('Sword', 5)
hero = character('Warrior', 60, 10, sword.damage)


def battle(hero, monster):
	while hero.hp >=0 and monster.hp >=0:
		hero.main_attack()
		monster.hp = monster.hp - hero.dmg
		monster.main_attack()
		hero.hp = hero.hp - monster.dmg
		if hero.hp <= 0:
			print('Hero has died')
		if monster.hp <=0:
			print('Monster has died')
		

battle(hero, goblin)