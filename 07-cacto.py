clear()
while True:
	n = 0
	if get_entity_type() != Entities.Cactus:
		for i in range(get_world_size()):
			if get_ground_type() == Grounds.Soil:
				plant(Entities.Cactus)
				move(East)
			else:
				till()
				plant(Entities.Cactus)
				move(East)
		move(North)
	else:
		for i in range(get_world_size()):
			for i in range(get_world_size()):
				if measure(North) < measure() and get_pos_y() + 1 != get_world_size():
					swap(North)
					n = n + 1
				if measure(East) < measure() and get_pos_x() + 1 != get_world_size():
					swap(East)
					n = n + 1
					move(East)
				else:
					move(East)
			move(North)
		if n == 0:
			harvest()
