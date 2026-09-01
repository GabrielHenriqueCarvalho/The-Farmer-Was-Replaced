clear()
while True:
	n = 0
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			if get_ground_type() == Grounds.Soil:
				plant(Entities.Sunflower)
				move(East)
			else:
				till()
				plant(Entities.Sunflower)
				move(East)
		move(North)
	for i in range(9):
		n = n + 1
		for i in range(get_world_size()):
			for i in range(get_world_size()):
				if measure() == 16 - n:
					harvest()
					move(East)
				else:
					move(East)
			move(North)
