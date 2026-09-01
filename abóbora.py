n = 0
clear()
while True:
	if get_water() < 0.5:
		use_item(Items.Water)
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			if can_harvest():
				n = n + 1
			if get_ground_type() == Grounds.Soil:
				plant(Entities.Pumpkin)
			else:
				till()
				plant(Entities.Pumpkin)
			move(East)
		move(North)
	if n == get_world_size() * get_world_size():
		harvest()
	else:
		n = 0