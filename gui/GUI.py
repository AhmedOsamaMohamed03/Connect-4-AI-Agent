from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout, QLineEdit, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from functools import partial

class ConnectFour(QMainWindow):
    def __init__(self):
        
        super().__init__()
        
        # Set Window Title, Icon and Geometry (Position) 
        self.setWindowTitle("Connect Four")
        self.setWindowIcon(QIcon("gui\icon.png"))
        
        # Initialize the UI elements
        self.InitGUI()
        
        # Setting Styles and Decorations
        self.setStyles()
        
    def InitGUI(self):
        
        # Define the game variables
        self.next_place = [5 for i in range(7)]
        self.turn = 1
        # 1 for agent and 1 for player
        
        # Define the central widget and the layouts
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.scoreboard_layout = QHBoxLayout()
        self.board_layout = QGridLayout()
        self.board_widget = QWidget()
        self.inputs_layout = QHBoxLayout()
        
        # Set the central layout
        self.board_widget.setLayout(self.board_layout)        
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_layout)
        
        # Set some object names for CSS styling
        self.board_widget.setObjectName("board")
        self.central_widget.setObjectName("central")
        
        # Upper Section Structure: Scoreboard
        # ------------------------------------
        # Define variables
        self.agent_score = 0
        self.player_score = 0
        self.player_color = "#ff9900"
        self.agent_color = " #cc0000"
        # Define the scoreboard fields
        self.agent_name = QLabel("Agent", self)
        self.player_name = QLabel("Player", self)
        self.player_scoreboard = QLineEdit(str(self.player_score), self)
        self.agent_scoreboard = QLineEdit(str(self.agent_score), self)
        self.player_scoreboard.setReadOnly(True)
        self.agent_scoreboard.setReadOnly(True)
        self.player_scoreboard.setObjectName("player_points")
        self.agent_scoreboard.setObjectName("agent_points")
        # Include the scoreboard fields in the scoreboard layout
        self.scoreboard_layout.addWidget(self.agent_name)
        self.scoreboard_layout.addWidget(self.agent_scoreboard)
        self.scoreboard_layout.addWidget(self.player_scoreboard)
        self.scoreboard_layout.addWidget(self.player_name)
        
        # Middle Section Structure: Board
        # ------------------------------------
        # Define the board of buttons (7*6)
        self.board = [[QPushButton() for i in range(7)] for j in range(6)]
        for i in range(6):
            for j in range(7):
                self.board[i][j].setObjectName("slot")
                self.board[i][j].clicked.connect(partial(self.play, i, j))
                self.board_layout.addWidget(self.board[i][j], i, j)
        
        
        # Lower Section Structure: Inputs
        # ------------------------------------
        # Define the k input field
        self.input_limit = QLineEdit(self)
        self.input_limit.setPlaceholderText("Enter the limit k")
        self.input_limit.setObjectName("k_input")
        # Define the algorithm selection field
        self.algorithm = QComboBox(self)
        algorithms = ["Normal Minimax", "Alpha-Beta Pruning Minimax", "Expectiminimax"]
        self.algorithm.addItems(algorithms)
        # Define Start button
        self.start_game = QPushButton("Start Game", self)
        self.start_game.clicked.connect(self.initiate_game)
        # Include inputs in input layout
        self.inputs_layout.addWidget(self.input_limit)
        self.inputs_layout.addWidget(self.algorithm)
        self.inputs_layout.addWidget(self.start_game)
        
        # Final Step: Combining the full window layout 
        # ---------------------------------------------
        self.main_layout.addLayout(self.scoreboard_layout)
        self.main_layout.addWidget(self.board_widget)
        self.main_layout.addLayout(self.inputs_layout)
        
    
    def initiate_game(self):
        
        # Initiate the game variables and slots
        print("Game Started")
        self.InitGUI()
        self.setStyles()
    
    def play(self, row, col):
        
        # Check if it's the agent's turn
        if self.turn == 0:
            return
        
        # Check if the column chosen is available for play
        if self.next_place[col] == -1 or self.next_place[col] < row:
            return
        
        color = self.player_color if self.turn == 1 else self.agent_color
        self.board[self.next_place[col]][col].setStyleSheet(f"background-color: {color}; border: 1px groove {color};")
        self.next_place[col] -= 1
        self.turn = 1 - self.turn
        
        
    def setStyles(self):
        
        # Setting Functions for Styles
        # ----------------------------
        self.scoreboard_layout.setContentsMargins(0, 15, 0, 15)
        self.player_scoreboard.setAlignment(Qt.AlignCenter)
        self.agent_scoreboard.setAlignment(Qt.AlignCenter)
        self.player_scoreboard.setFixedSize(150, 100)
        self.agent_scoreboard.setFixedSize(150, 100)
        self.agent_name.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.input_limit.setFixedSize(200, 50)
        self.input_limit.setAlignment(Qt.AlignCenter)
        self.inputs_layout.setSpacing(20)
        self.scoreboard_layout.setSpacing(0)
        
        # CSS Properties
        # --------------
        self.setStyleSheet("""
                
                QWidget#central{
                    background-color: #0F172A;
                }
                
                QWidget#board{
                    background-color: #8ea4a9;
                    border: 2px inset #8ea4a9;
                    border-radius: 15;
                    margin: 5px;
                }
                
                QPushButton{
                    font-size: 20px;
                    font-family: 'Trebuchet MS', sans-serif;
                    font-weight: bold;
                    height: 39px;
                }
                
                QPushButton:hover{
                    
                }
                
                QPushButton#slot {
                    background-color: #0F172A;
                    height: 100px;
                    width: 100px;
                    border-radius: 50;
                    border: 0px groove #8ea4a9;
                }
                
                QPushButton#slot:hover {
                    background-color: #1b294b;
                }
                
                QLineEdit{
                    font-size: 50px;
                    font-family: 'Brush Script MT', cursive;
                    font-weight: bold;
                    color: #898c90;
                    padding: 5px;
                    border: 1px groove #aca5b0;
                    height: 50px;
                    border-radius: 6;
                }
                
                QLineEdit#player_points {
                    background-color: #ff9900;
                    border-top-left-radius: 0px;
                    border-bottom-left-radius: 0px;
                }
                
                QLineEdit#agent_points {
                    background-color: #cc0000;
                    border-top-right-radius: 0px;
                    border-bottom-right-radius: 0px;
                }
                
                QLabel{
                    font-size: 30px;
                    font-family: 'Trebuchet MS', sans-serif;
                    font-weight: bold;
                    color: #b0b2b5;
                    padding: 0px 5px;
                }
                
                QLineEdit#k_input{
                    font-size: 20px;
                    font-family: 'Trebuchet MS', sans-serif;
                    font-weight: bold;
                }
                
                QComboBox{
                    font-size: 20px;
                    font-family: 'Trebuchet MS', sans-serif;
                    font-weight: bold;
                    height: 42px;
                }
            """)
        

def main():
    app = QApplication([])
    window = ConnectFour()
    window.show()
    app.exec()

main()