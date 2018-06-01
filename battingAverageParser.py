import sys
import os
import re


class Player:
	atBats = float(0)
	totalHits = float(0)
	batting_average = float(0)
	name = "Blank"

	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	def add_atBats(self, times):
		self.atBats = self.atBats + times

	def add_hits(self, times):
		self.totalHits = self.totalHits + times

	def calculate_batting_average(self):
		if (self.atBats!=0):
			self.batting_average = (float(self.totalHits)/float(self.atBats))
		return self.batting_average

	def return_batting_average(self):
		batting_average = (float(self.totalHits)/float(self.atBats))
		return format(batting_average, '.3f')


def is_he_there(mystery_man):
	for guy in listOfPlayers:
		name = guy.name
		if (name==mystery_man):
			return True
	return False


def summon(him):
	for guy in listOfPlayers:
		name = guy.name
		if (name == him):
			return guy
	return "ERROR"  # This program only uses summon after knowing that is_he_there returns true


def scan_line_for_player(line):
	match = player_regex.match(line)
	if match is not None:
		the_name = match.group(1)
		if (is_he_there(the_name)):
			currentPlayer = summon(the_name)
		else:
			currentPlayer = Player(the_name)
			listOfPlayers.append(currentPlayer)
		currentPlayer.add_hits(float(match.group(3)))
		currentPlayer.add_atBats(float(match.group(2)))  # We skip ?: marked groups when numbering which groups to reference
		currentPlayer.calculate_batting_average()
		return True
	else:
		return False


# Main Method

player_regex = re.compile(r"(\w+\s+\w+)(?:\s+batted\s+)(\d)(?:\s+times\s+with\s+)(\d)(?:\s+hits\s+and\s+)(\d)(?:\s+runs)")
listOfPlayers = []

if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])

filename = sys.argv[1]
f = open(filename)
if not os.path.exists(filename):
	sys.ext("Error: File '%s' not found" % sys.argv[1])
for line in f:
	scan_line_for_player(line)
f.close()

sortedListOfPlayers = sorted(listOfPlayers, key=lambda player: player.batting_average*-1)

# First, the program prints the sorted list to the output console
for s in sortedListOfPlayers:
	name = s.getName()
	avg = s.return_batting_average()
	print "%s: %s" % (name, avg)

# Then, the program prints the sorted list to a .txt file
with open("team_batting_average.txt", "w") as f:
	for s in sortedListOfPlayers:
		name = s.getName()
		avg = s.return_batting_average()
		f.write("%s: %s \n" % (name, avg))
