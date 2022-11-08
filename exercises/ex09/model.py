"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi


__author__ = "730568515"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point, sickness: int):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
        self.sickness = sickness

    def tick(self) -> None:
        self.location = self.location.add(self.direction)

    def contract_diseas(self) -> None:
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
        
    def is_infected(self) -> bool:
        if self.sickness == constants.INFECTED:
            return True
        else:
            return False
        
    def color(self) -> str:
        if self.is_vulnerable == True:
            return "gray"
        else:
            return "red"
    

class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected_cells >= cells or infected_cells <= 0:
            ValueError("Some number of cells must begin infected.")
        i: int = 0
        while i < cells - infected_cells:
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            start_status_vulnerable: int = constants.VULNERABLE
            cell: Cell = Cell(start_location, start_direction, start_status_vulnerable)
            self.population.append(cell)
            i += 1
        while i < infected_cells:
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            start_status_infected: int = constants.INFECTED
            cell: Cell = Cell(start_location, start_direction, start_status_infected)
            self.population.append(cell)
            i += 1
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False