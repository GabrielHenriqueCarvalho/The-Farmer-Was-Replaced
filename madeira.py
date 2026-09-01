clear()
while True:
	for i in range(get_world_size()):
		if get_pos_y() % 2==0:
			if get_pos_x() % 2==0:
				if get_water() < 0.5:
					use_item(Items.Water)
				if can_harvest():
					harvest()
					plant(Entities.Tree)
				move(East)
			else:
				if can_harvest():
					harvest()
					plant(Entities.Bush)
					move(East)
		else:
			if get_pos_x() % 2==1:
				if can_harvest():
					harvest()
				plant(Entities.Tree)
				move(East)
			else:
				if can_harvest():
					harvest()
					plant(Entities.Bush)
					move(East)
	move(North)