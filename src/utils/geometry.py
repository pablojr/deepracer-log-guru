import math

from src.utils.types import Point


def get_distance_between_points(first, second):
    (x1, y1) = first
    (x2, y2) = second

    x_diff = x2 - x1
    y_diff = y2 - y1

    return math.sqrt(x_diff * x_diff + y_diff * y_diff)

def get_bearing_between_points(start, finish):
    (start_x, start_y) = start
    (finish_x, finish_y) = finish

    direction_in_radians = math.atan2(finish_y - start_y, finish_x - start_x)
    return math.degrees(direction_in_radians)

def get_angle_in_proper_range(angle):
    if angle >= 180:
        return angle - 360
    elif angle <= -180:
        return 360 + angle
    else:
        return angle


def get_turn_between_directions(current, required):
    difference = required - current
    return get_angle_in_proper_range(difference)


def get_edge_point(previous: Point, mid: Point, future: Point, direction_offset: int, distance: float):
    assert direction_offset in [90, -90]
    assert previous != mid

    (previous_x, previous_y) = previous
    (mid_x, mid_y) = mid
    (next_x, next_y) = future

    degrees_to_mid_point = math.degrees(math.atan2(mid_y - previous_y, mid_x - previous_x))
    if mid == future:
        track_heading_degrees = degrees_to_mid_point
    else:
        degrees_from_mid_point = math.degrees(math.atan2(next_y - mid_y, next_x - mid_x))
        degrees_difference = get_turn_between_directions(degrees_to_mid_point, degrees_from_mid_point)
        track_heading_degrees = degrees_to_mid_point + degrees_difference / 2

    radians_to_edge_point = math.radians(track_heading_degrees + direction_offset)

    x = mid_x + math.cos(radians_to_edge_point) * distance
    y = mid_y + math.sin(radians_to_edge_point) * distance

    return x, y
