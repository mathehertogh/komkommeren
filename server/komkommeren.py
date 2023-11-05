#!/bin/python3

import itertools
import random
import json
from flask import Flask
from pprint import pprint
from flask import request

kid_counter = 0
class Kaart:
	def __init__(self):
		self.kleur = random.randint(0, 3)
		self.rang = random.randint(2, 15)

	def str(self):
		if self.kleur < 0 or self.kleur > 3:
			print(f"ERROR: kaart met kleur {self.kleur}")
		elif self.kleur == 0:
			kleur = "harten"
		elif self.kleur == 1:
			kleur = "ruiten"
		elif self.kleur == 2:
			kleur = "klaver"
		elif self.kleur == 3:
			kleur = "schoppen"

		if self.rang < 2 or self.rang > 15:
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
		return f"{kleur} {rang}"

	def json(self):
		return self.__dict__

class Opgooi:
	def __init__(self, kaarten):
		self.kaarten = sorted(kaarten, key=lambda x: x.rang)

	def json(self):
		return [kaart.json() for kaart in self.opgooien]

	def __le__(self, other):
		assert(len(self) == len(other))
		return all(self.kaarten[i].rang <= other.kaarten[i].rang for i in range(len(self)))

class Slag:
	def __init__(self, aantal_spelers):
		self.opgooien = [[] for i in range(aantal_spelers)] # lijst van opgooien

	def json(self):
		return [opgooi.json() for opgooi in self.kaarten]

	def leeg(self):
		all([not k for k in self.opgooien])

	def wat_ligt_er(self):
		assert(not self.leeg())
		for k in self.opgooien:
			if k:
				hoogste = k
		for k in self.opgooien:
			if hoogste <= k:
				hoogste = k
		return hoogste

	def gooi_op(self, kaarten, index):
		self.kaarten[index] = kaarten

class Komkommeraar:
	def __init__(self, naam):
		global kid_counter
		self.kid = kid_counter
		kid_counter += 1
		self.naam = naam
		self.hand = [] # kaarten
		print(f"Komkommeraar {naam} aangemaakt met kid {self.kid}")

	def json(self):
		return {
			'kid': self.kid,
			'naam': self.naam,
			'hand': [kaart.json() for kaart in self.hand]
		}

	def print_hand(self):
		print(f"{self.naam}'s hand: ", end="")
		print(", ".join([kaart.str() for kaart in self.hand]))

	def kies_zet(self):
		print("Welke kaarten wil je opleggen? Je hand is dit:")
		print([kaart.str() for kaart in self.hand])
		indices = [int(index) for index in str(input()).split()]
		opgooi = [self.hand[index] for index in indices]
		print([kaart.str() for kaart in opgooi])
		return opgooi

class Potssjjj:
	def __init__(self, deelnemers):
		self.deelnemers = deelnemers # lijst komkommeraars
		self.tafel = [] # slagen
		self.aan_zet = 0 # index in deelnemers
		self.slag = Slag(len(deelnemers)) # huidige slag

	def json(self):
		return {
			'deelnemers': [k.json() for k in self.deelnemers],
			'aan_zet': self.aan_zet,
			'tafel': [slag.json() for slag in self.tafel]
		}

	def delen(self, hoeveel):
		for k in self.deelnemers:
			k.hand = sorted([Kaart() for i in range(hoeveel)], key=lambda x: x.rang)
			k.print_hand()

	def doe_zet(self, opgooi):
		if self.slag.leeg():
			print("Opening van de slag!")
			if any([opgooi[0].rang != kaart.rang for kaart in opgooi])
				print("VERZAKER! Je moet de slag openen met alleen maar kaarten van dezelfde rang.")
				return False



	def speel_slag(self):
		self.slag = Slag(len(self.deelnemers))
		winnaar = -1
		hoogste = -1
		for i in range(len(self.deelnemers)):
			speler = self.deelnemers[self.aan_zet]
			opgooi = speler.zet()

			slag.gooi_op([opgooi], self.aan_zet)
			print(f"{speler.naam:8} gooit op: {[kaart.str() for kaart in opgooi]}")
			self.aan_zet = (self.aan_zet + 1) % len(self.deelnemers)
		print(f"{self.deelnemers[winnaar].naam} wint de slag")
		self.aan_zet = winnaar
		self.tafel.append(slag)


app = Flask(__name__)

@app.route("/")
def speel_potsj():
	guus = Komkommeraar("Guus")
	ralph = Komkommeraar("Rafff")
	mathe = Komkommeraar("Mathé")
	emma = Komkommeraar("Emma")
	potsj = Potssjjj([guus, ralph, emma, mathe])
	potsj.delen(7)
	print()
	potsj.speel_slag()
	print()
	potsj.speel_slag()
	print(potsj.json())
	print()
	print("Potsj zier er nu zo uit:")
	pprint(potsj.json())

	with open("index.html", "r") as f:
		r = f.read()
	return r

@app.route("/Build/komkommerbezorger.wasm")
@app.route("/favicon.ico")
@app.route("/Build/komkommerbezorger.data")
@app.route("/Build/komkommerbezorger.framework.js")
@app.route("/TemplateData/favicon.ico")
@app.route("/Build/komkommerbezorger.loader.js")
@app.route("/TemplateData/style.css")
def geef_file():
	with open("/var/www/komkommerbezorger" + request.path, "rb") as f:
		r = f.read()
	return r


if __name__ == "__main__":
	speel_potsj()