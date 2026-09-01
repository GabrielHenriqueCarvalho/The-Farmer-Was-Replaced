clear()
vai = West
x = get_pos_x()
y = get_pos_y()
n = get_world_size() / 2 * get_world_size()
def labirinto():
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, n)
labirinto()
while True:
	move(vai)
	x2 = get_pos_x()
	y2 = get_pos_y()
	if x == x2 and y == y2:
		if vai == West:
			vai = South
		elif vai == South:
			vai = East
		elif vai == East:
			vai = North
		elif vai == North:
			vai = West
	else:
		if vai == West:
			vai = North
		elif vai == North:
			vai = East
		elif vai == East:
			vai = South
		elif vai == South:
			vai = West
	x = get_pos_x()
	y = get_pos_y()
	if get_entity_type() == Entities.Treasure:
		harvest()
		labirinto()
