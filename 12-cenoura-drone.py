clear()
def plantar():
	while True:
		if get_water() < 0.5:
			use_item(Items.Water)
		move(North)
		if get_ground_type() == Grounds.Soil:
			harvest()
			plant(Entities.Carrot)
		else:
			harvest()
			till()
			harvest()
			plant(Entities.Carrot)

for i in range(get_world_size()):
	move(East)
	spawn_drone(plantar)
plantar()
	
	
