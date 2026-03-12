class LionFish:
	count_animals = 0

	def __init__(self, name="seamba"):
		self._name = name
		self._age = 0
		LionFish.count_animals += 1

	def birthday(self):
		self._age += 1

	def get_age(self):
		return self._age

	def set_name(self, name):
		self._name = name

	def get_name(self):
		return self._name


def main():
	lf1 = LionFish()
	lf2 = LionFish("moriseao")
	print(lf1.get_name(), " ", lf2.get_name())
	lf2.set_name("move_in_move_it")
	print(lf2.get_name())
	print(lf1.count_animals)


if __name__ == "__main__":
	main()