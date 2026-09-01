clear()
def plantar():
	while True:
		move(North)
		harvest()
for i in range(get_world_size()):
	move(East)
	spawn_drone(plantar)
plantar()
