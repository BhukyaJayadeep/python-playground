# Hurdle 1

This project demonstrates the basic concepts of using functions to control a robot's movements. The code is designed to be run on the [Reeborg's World website](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json).

## Description

In this project, the robot is programmed to navigate a series of hurdles using custom-defined functions. The main functions used are `turn_right()`, `turn_square()`, and `turn_square1()`.

## How to Run

1. Visit the [Reeborg's World website](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json).
2. Copy the code from your project.
3. Paste it into the Python editor on the Reeborg's World website.
4. Run the program to see the robot navigate the hurdles.

## Functions

- `turn_right()`: Makes the robot turn right by turning left three times and then moving forward.
- `turn_square()`: Makes the robot turn a full square (three left turns and a move forward).
- `turn_square1()`: Combines `turn_right()` and `turn_square()` for a more complex movement.
