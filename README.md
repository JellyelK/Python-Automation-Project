# Python-Automation-Project
This is a simple automation project of a fictional user registration system. I have created a basic graphical interface to serve as an example of a registration platform. The script will retrieve the users and their passwords from the text file and populate them into the interface.

# User Registration Automation

## Description
This Python script automates the user registration process using data from a TXT file. The script uses the MouseInfo library to identify specific coordinates for mouse clicks and text inputs, facilitating the registration process on a graphical interface.

## Requirements
- Python 3.x
- MouseInfo library (Install using pip: `pip install mouseinfo`)
- Pyautogui library (Install using pip: `pip install pyautogui`)

## Usage
1. Ensure Python 3.x is installed on your system.
2. Install the MouseInfo library using pip.
3. Update the script with the correct file path containing user data in TXT format.
4. Modify the script to set the coordinates for mouse clicks and text inputs according to your graphical interface.

## Running the Script
1. Open a terminal or command prompt.
2. Navigate to the directory containing the Python script.
3. Run the script: `Tela_de_cadastro.py` for open the login interface.
4. Run the script: `main.py` and execute the script

## Script Configuration
- `mouse_click_coordinates`: Define the coordinates for mouse clicks on the GUI.
- `text_input_coordinates`: Set the coordinates for text input areas on the interface.

## Example
```python
mouse_click_coordinates = (x_coord, y_coord, duration)
text_input_coordinates = (x_input, y_input, duration)
