# Connect 4 AI Agent using Minimax Algorithm

This repository contains the implementation of a Connect 4 AI agent using the Minimax algorithm with optional alpha-beta pruning and expected Minimax. The project was developed as part of the Artificial Intelligence course at Alexandria University, Faculty of Engineering, Computer and Systems Department.

## Project Description

Connect 4 is a two-player game where players take turns dropping colored discs into a grid. The objective is to connect four discs of the same color vertically, horizontally, or diagonally. This project implements an AI agent that can play Connect 4 against a human player using the Minimax algorithm with various enhancements.

## Features

- **Game GUI**: A graphical user interface for playing Connect 4 against the AI.
- **AI Algorithms**:
  - Minimax without alpha-beta pruning
  - Minimax with alpha-beta pruning
  - Expected Minimax with probabilistic disc placement
- **Heuristic Pruning**: A heuristic function to evaluate game states and truncate the game tree after a specified depth (K).
- **Minimax Tree Visualization**: The minimax tree is printed to the console in a readable format for each turn.

## Requirements

- Python
- PyQt5 library for GUI

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/AhmedOsamaMohamed03/Connect-4-AI-Agent.git
   ```
2. Navigate to the project directory:
   ```bash
   cd connect-4-ai-agent
   ```
3. Run the game:
   ```bash
   python main.py 
   ```

## YouTube Video

[![Connect 4 AI Demo](https://img.youtube.com/vi/ywYWBBuhXhw/0.jpg)](https://youtu.be/ywYWBBuhXhw)
