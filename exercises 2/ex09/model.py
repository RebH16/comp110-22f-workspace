"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


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
    
    def distance(self, other: Point) -> int:
        distance: int = sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance
    
        


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
        if self.is_infected():
            self.sickness += 1
            if self.sickness > constants.RECOVERY_PERIOD:
                self.immunize()

    def contract_disease(self) -> None:
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
        
    def is_infected(self) -> bool:
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
        
    def color(self) -> str:
        if self.is_vulnerable():
            return "gray"
        elif self.is_immune():
            return "lavender"
        else:
            return "red"
    
    def contact_with(self, other: Cell) -> None:
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        elif other.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(self) -> None:
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False

class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected_cells >= cells or infected_cells <= 0:
            ValueError("Some number of cells must begin infected.")
        if immune_cells >= cells or immune_cells <= 0:
            ValueError("Some number of cells must begin immune.")
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction, constants.VULNERABLE)
            if i < infected_cells:
                cell.contract_disease()
            if i < immune_cells:
                cell.immunize()
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

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
        i: int = 0
        while i < len(self.population):
            if self.population[i].is_infected():
                return False
            i += 1
        return True
    
    def check_contacts(self) -> None:
        i: int = 0
        while i < len(self.population):
            j: int = i + 1
            while j < len(self.population):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                j += 1
            i += 1