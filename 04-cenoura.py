clear()
while True:
	for i in range(get_world_size()):
		if get_ground_type() == Grounds.Soil:
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
				move(East)
		else:
			harvest()
			till()
			plant(Entities.Carrot)
			move(East)
	move(North)
			
