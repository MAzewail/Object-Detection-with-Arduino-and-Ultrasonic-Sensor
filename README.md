# Object Detection with Arduino and Ultrasonic Sensor

This repository contains a project that combines Arduino, ultrasonic sensor, servo motor, and machine learning techniques to implement object detection. The project includes the deployment of a machine learning model on an Arduino board, along with the Python code for data generation, model creation, and the training process.

## Table of Contents

- [Introduction](#introduction)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The objective of this project is to demonstrate object detection using an Arduino board and an ultrasonic sensor. The deployed machine learning model, based on ensemble techniques such as Random Forests and Decision Trees, enables the Arduino to detect objects in its surroundings. This repository provides the necessary code and instructions to replicate and extend the project.

## Hardware Requirements

To replicate this project, you will need the following hardware components:

- Arduino board (e.g., Arduino Uno)
- Ultrasonic sensor
- Servo motor

Make sure you have the above components available to successfully deploy and test the object detection system.

## Software Requirements

The project requires the following software dependencies:

- Arduino IDE (for uploading the code to the Arduino board)
- Python 3.x
- Required Python libraries (specified in `requirements.txt`)

Please ensure that you have the necessary software installed before proceeding.

## Installation

To set up the project on your local machine, follow these steps:

1. Clone this repository to your local machine using the following command:
   ````
   git clone https://github.com/your-username/arduino-object-detection.git
   ```

2. Change into the project directory:
   ````
   cd arduino-object-detection
   ```

3. Install the required Python libraries by running the following command:
   ````
   pip install -r requirements.txt
   ```

4. Connect the Arduino board, ultrasonic sensor, and servo motor according to the wiring instructions provided in the `docs` folder.

5. Upload the Arduino code to the board using the Arduino IDE. The code for the Arduino can be found in the `arduino` directory.

Congratulations! You have successfully installed the project.

## Usage

To run the object detection system, follow these steps:

1. Make sure the Arduino board is connected to your computer.

2. Open the Arduino IDE and upload the code to the Arduino board.

3. Run the Python script `data_generation.py` to collect training data. This script will generate the necessary data for training the machine learning model.

4. Run the Python script `model_training.py` to train the ensemble machine learning model using the generated data.

5. Finally, run the Python script `object_detection.py` to deploy the trained model on the Arduino board and start the object detection process.

The object detection system should now be up and running!

## Project Structure

The project directory is structured as follows:

```
.
├── arduino_object_detection
│   ├── arduino_object_detection.ino
|   └── model.h
├── docs
│   ├── wiring_diagram.jpeg
│   └── README.md
├── data_generation.py
├── model_training.py
├── object_detection.py
├── README.md
└── requirements.txt
```

- The `arduino` directory contains the Arduino code (`object_detection.ino`) for the object detection system.

- The `docs` directory includes additional documentation, such as a wiring diagram, to help with the hardware setup.

- The `data_generation.py` script is responsible for generating training data.

- The `model_training.py` script trains the ensemble machine learning model.

- The `object_detection.py` script deploys the trained model on the Arduino board and performs object detection.

## Contributing

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per your requirements.
