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
    # Create empty list to store vertices
    points = []

    # Calculate angle per vertice
    angle = 360 / sides

    # Compute one vertice per side
    for i in range(0, sides):
        # Calculate the vertice around the trigonometric circle, account for given rotation
        x = math.cos(math.radians(angle * i + rotation))
        y = math.sin(math.radians(angle * i + rotation))

        # Get the point from the unit circle to the appropriate radius
        x = x * radius
        y = y * radius

        # Move the point so that the origin of the circle is the given one
        x = x + position[0]
        y = y + position[1]

        # Create a tuple with the vertex position
        pt = (x,y)

        # Add the point to the list
        points.append(pt)

    # Return list of vertices
    return points

# Function ship_move
# ------------------
# This function should return the new position of the ship.
# The current position of the ship is given by "position",
# and its rotation should be "rotation" (given in degrees). 
# The movement should be done in that direction, and it 
# should move "distance" units forward.
def ship_move(position, rotation, distance):
    
    delta_x = math.cos(math.radians(rotation)) * distance
    delta_y = math.sin(math.radians(rotation)) * distance

    new_pos_x = position[0] + delta_x
    new_pos_y = position[1] + delta_y

    return (new_pos_x, new_pos_y)

# Function get_cone
# ------------------
# This function should return a list with 3 tuples, corresponding
# to the vertices of a cone of vision, centered on "position", 
# and extending "range" forward. The enemy is rotated "rotation"
# degrees and has a field of view given by "field_of_view" (also
# in degrees)
# The vertices should be integer positions.
def get_cone(position, rotation, field_of_view, range):
    angle1 = rotation + field_of_view / 2
    angle2 = rotation - field_of_view / 2

    p1x = math.cos(math.radians(angle1)) * range + position[0]
    p1y = math.sin(math.radians(angle1)) * range + position[1]

    p2x = math.cos(math.radians(angle2)) * range + position[0]
    p2y = math.sin(math.radians(angle2)) * range + position[1]

    return [ position, (p1x, p1y), (p2x, p2y) ]

# Function ship_detected
# ------------------
# This function should take the current position of the player
# "ship_position", an enemy position ("enemy_position"), rotation
# ("enemy_rotation"), field of view ("enemy_fov") and range
# ("enemy_range)" and return True if the enemy detects the player,
# and return False otherwise
def ship_detected(ship_position, enemy_position, enemy_rotation, enemy_fov, enemy_range):
    
    return False

play(get_shape, ship_move, get_cone, ship_detected)
