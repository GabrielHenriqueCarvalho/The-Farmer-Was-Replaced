clear()
change_hat(Hats.Dinosaur_Hat)
while True:
	x = get_pos_x()
	y = get_pos_y()
	if get_pos_x() == 0:
		for i in range(get_world_size()):
			move(East)
	if get_pos_x() == 1 and get_pos_y() == 0:
		for i in range(get_world_size() - 1):
			move(East)
	move(North)
	for i in range(get_world_size() - 2):
		move(West)
	move(North)
	for i in range(get_world_size() - 2):
		move(East)
	if get_pos_y() == get_world_size() - 1 and get_pos_x() == 0:
		for i in range(get_world_size()):
			move(South)
	if get_pos_x() == x and get_pos_y() == y:
		change_hat(Hats.Cactus_Hat)
		change_hat(Hats.Dinosaur_Hat)
		
