def find_path(neighbour_fn,
			  start,
			  goal,
			  visited,
			  reachable = lambda pos: True,
			  depth = 100000):
	#The reachable function returns true if the given node is not blocked by a wall.


	
	if depth == 0:
		return []
	
	visited.append(start)
	# if we found the goal, return current node
	cur = start
	if cur == goal:
		return [cur]
	# check neighbours
	for n in neighbour_fn(cur):
		# skip it if we've already checked it, or if it isn't blocked
		if ((n in visited) or (not reachable(n))):
				continue
		path = find_path(neighbour_fn, n, goal, visited, reachable, depth-1)
		if len(path)>0 and path[-1] == goal:
			return [cur]+path
	# no path to be found
	if goal not in visited:
		return []

	return []

	
	




	
