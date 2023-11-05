#!/bin/python3

import itertools
import random
import json

class Kaart:
	def __init__(self):
		self.kleur = random.choice(["harten", "ruiten", "klaver", "schoppen"])
		self.rang = random.randint(2, 15)

	def str(self):
		if self.rang < 2:
			print(f"ERROR: kaart met rang {self.rang}")
		elif self.rang <= 10:
			rang = self.rang
		elif self.rang == 11:
			rang = "B"
		elif self.rang == 12:
			rang = "V"
		elif self.rang == 13:
			rang = "H"
		elif self.rang == 14:
			rang = "A"
		elif self.rang == 15:
			return "Joker"
		else:
			print(f"ERROR: kaart met rang {self.rang}")
		return f"{self.kleur} {rang}"

class Komkommeraar:
	def __init__(self, naam):
		self.naam = naam
		self.kid = itertools.count()
		self.hand = [] # kaarten

	def zet(self):
		kies = random.randint(0, len(self.hand)-1)
		opgooi = self.hand[kies]
		del self.hand[kies]
		return opgooi

	def print_hand(self):
		print(f"{self.naam}'s hand: ", end="")
		print(", ".join([kaart.str() for kaart in self.hand]))

class Potssjjj:
	def __init__(self, deelnemers):
		self.deelnemers = deelnemers # lijst komkommeraars
		self.aanzet = 0 # index in deelnemers
		self.tafel = [] # slagen

	def delen(self, hoeveel):
		for k in self.deelnemers:
			k.hand = [Kaart() for i in range(hoeveel)]
			k.print_hand()

	def speel_slag(self):
		winnaar = -1
		hoogste = -1
		for i in range(len(self.deelnemers)):
			speler = self.deelnemers[self.aanzet]
			opgooi = speler.zet()
			print(f"{speler.naam:8} gooit op: {opgooi.str()}")
			if opgooi.rang >= hoogste:
				hoogste = opgooi.rang
				winnaar = self.aanzet
			self.aanzet = (self.aanzet + 1) % len(self.deelnemers)
		print(f"{self.deelnemers[winnaar].naam} wint de slag")
		self.aanzet = winnaar

if __name__ == "__main__":
	guus = Komkommeraar("Guus")
	ralph = Komkommeraar("Rafff")
	mathe = Komkommeraar("Mathé")
	emma = Komkommeraar("Emma")
	potsj = Potssjjj([guus, ralph, emma, mathe])
	potsj.delen(3)
	print()
	potsj.speel_slag()
	print()
	potsj.speel_slag()
	print()
	potsj.speel_slag()

