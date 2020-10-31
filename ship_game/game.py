from backend import *

# Function get_shape
# ------------------
# This function should return a list of tuples. The number of 
# tuples returned should be equal to the number of sides
# Every tuple should be the position (x,y) of a vertex 
# of a geometric figure with given number of "sides" and "radius",
# centered around the "position". This figure should be rotated
# by the given "rotation" (given in degrees)
# The vertices should be integer positions.
def get_shape(position, radius, sides, rotation):
    pass

# Function ship_move
# ------------------
# This function should return the new position of the ship.
# The current position of the ship is given by "position",
# and its rotation should be "rotation" (given in degrees). 
# The movement should be done in that direction, and it 
# should move "distance" units forward.
def ship_move(position, rotation, distance):
    pass

# Function get_cone
# ------------------
# This function should return a list with 3 tuples, corresponding
# to the vertices of a cone of vision, centered on "position", 
# and extending "range" forward. The enemy is rotated "rotation"
# degrees and has a field of view given by "field_of_view" (also
# in degrees)
# The vertices should be integer positions.
def get_cone(position, rotation, field_of_view, range):
    pass

# Function ship_detected
# ------------------
# This function should take the current position of the player
# "ship_position", an enemy position ("enemy_position"), rotation
# ("enemy_rotation"), field of view ("enemy_fov") and range
# ("enemy_range)" and return True if the enemy detects the player,
# and return False otherwise
def ship_detected(ship_position, enemy_position, enemy_rotation, enemy_fov, enemy_range):
    pass

play(get_shape, ship_move, get_cone, ship_detected)
