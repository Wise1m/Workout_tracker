# Workout Tracker

## Overview

The Workout Tracker is a command-line application designed to help users track their workouts using natural language inputs. It accepts input such as "I ran 5 kilometers" or "Did 30 minutes of cycling" and stores this information in an Excel sheet for easy management and analysis.

## Features

- Accepts natural language inputs for different types of workouts.
- Tracks metrics like distance, duration, calories burned, etc.
- Stores workout data in an Excel sheet for record-keeping and analysis.
- Provides a simple and intuitive interface for managing workout logs.

## Installation

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/yourusername/workout-tracker.git
   ```

2. Navigate to the project directory:
   ```
   cd workout-tracker
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script to start the Workout Tracker:
   ```
   python main.py
   ```

2. Enter your workout details using natural language inputs when prompted.
   Example inputs:
   - "I ran 5 kilometers"
   - "Did 30 minutes of cycling"
   - "Completed 100 push-ups and 50 sit-ups"

3. View and manage your workout logs in the generated Excel sheet (`workout_tracker.xlsx`).

## Dependencies

The Workout Tracker uses the following Api:

- `sheety`: To store add data to Excel files.
- `nutritionix`: For natural language processing (NLP) to parse workout inputs.

## File Structure

- `main.py`: Main script to run the Workout Tracker.
- `workout_tracker.xlsx`: Excel sheet to store workout logs.

## Contributing

Contributions to the Workout Tracker are welcome! If you have any suggestions, bug fixes, or new features to add, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the GNU License.
