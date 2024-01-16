
# Ecosystem Simulation WebApp

## Introduction
This interactive web application, developed using Streamlit, provides a unique educational experience through ecosystem simulations. It includes three distinct simulations, each depicting various species and ecosystems. Users engage with the app by matching animals and plants to their appropriate ecosystems, enhancing their understanding of ecological relationships.

## Features
- **Interactive Simulations**: Three simulations featuring different ecosystems and species.
- **Dynamic User Interface**: Each simulation presents a sidebar with animal and plant cards, a main screen divided into ecosystem parts, and a column displaying selected species and ecosystem characteristics.
- **Custom Styling and Interactive Elements**: Custom styles for Streamlit components and interactive elements like buttons and sidebars.
- **Authentication System**: Secure login functionality with password hashing for user access, utilizing the `config.yaml` file for configuration management.
- **Educational and Engaging**: Designed to teach ecological principles in an engaging manner.
- **Error Handling and Feedback**: Mechanisms for handling errors and providing user feedback.

## Installation

To run this application, you'll need Python installed on your system. Follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/TovTechDataCourse/streamlit-ecosystem-simulation
   ```

2. Navigate to the project directory:
   ```
   cd streamlit-ecosystem-simulation
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the application locally, run:

```
streamlit run run.py
```
To start the application through streamlit cloud:

https://ecosystem-sim.streamlit.app/
```
Navigate through the application using the sidebar to select simulations and make your ecosystem choices.


**## login**

username: admin
password: 1234


## Project Structure

The main directory contains:
- `pages` folder with subfolders for each simulation (`simulation_1`, `simulation_2`, `simulation_3`).
- Within each simulation folder, there are `animals`, `plants`, and `split_photo` folders containing respective photos.
- A `for_reference.xlsx` file in each simulation folder, detailing data about the ecosystem squares.

## Dependencies

The application requires several Python packages, listed in `requirements.txt`. Key dependencies include Streamlit, Pandas, Pillow, and various Streamlit plugins for enhanced functionality.

## Contributing

Contributions to this project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Security

- The application uses a password hasher script for creating secure hashed passwords, enhancing the security of the authentication system.
- Configuration settings, including authentication credentials, are managed securely using a `config.yaml` file.

## License

This project is licensed under the Apache License. For more information, see the LICENSE file in the repository.

cludes mechanisms for handling errors and providing user feedback, ensuring a smooth user experience.
- **Authentication System Enhancements**: The application uses `password hasher.py` for hashing passwords and `config.yaml` for managing configuration settings, particularly for the login page.

## Installation

To run this application, you'll need Python installed on your system. Follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/TovTechDataCourse/streamlit-ecosystem-simulation
   ```

2. Navigate to the project directory:
   ```
   cd streamlit-ecosystem-simulation
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the application, run:

```
streamlit run run.py
```

Navigate through the application using the sidebar to select simulations and make your ecosystem choices.

## Project Structure

The main directory contains:
- `pages` folder with subfolders for each simulation (`simulation_1`, `simulation_2`, `simulation_3`).
- Within each simulation folder, there are `animals`, `plants`, and `split_photo` folders containing respective photos.
- A `for_reference.xlsx` file in each simulation folder, detailing data about the ecosystem squares.

## Dependencies

The application requires several Python packages, listed in `requirements.txt`. Key dependencies include Streamlit, Pandas, Pillow, and various Streamlit plugins for enhanced functionality.

## Contributing

Contributions to this project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the Apache License. For more information, see the LICENSE file in the repository.
