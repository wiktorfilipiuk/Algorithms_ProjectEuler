def loadPlayers():
	player1 = []
	player2 = []
	file = open('poker.txt', 'r')
	for line in file:
		lineSplitted = line.split(" ")
		lineSplitted[9] = lineSplitted[9][0:2]
		player1.append(lineSplitted[0:5])
		player2.append(lineSplitted[5:])
	return (player1, player2)

(player1, player2) = loadPlayers()



