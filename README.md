# Survival Calculator

## Project Overview
The Survival Calculator is a Python program that calculates the duration of survival in various time units based on the user's age. This project aims to provide a fun and interactive way for users to reflect on the time they have lived in different units such as months, weeks, days, hours, minutes, and seconds.

## Thought Process and Design

### Class Definition
The first step in creating the Survival Calculator was to define a class `Survival_cal`. This class encapsulates the functionality of the calculator and contains a method `duration_of_survival` which performs the calculations.

### Method Definition
The `duration_of_survival` method was designed to:
- Take user input for age and preferred time unit.
- Calculate the duration of survival in the selected time unit.
- Handle different user inputs and provide appropriate outputs.

### Error Handling and User Experience
To enhance user experience, the method includes basic error handling to manage incorrect time unit entries. It ensures that the user is informed if their choice is not available, prompting them to enter a valid option.

### Implementation

Here’s the implementation of the `Survival_cal` class and the `duration_of_survival` method:

#### Survival_cal Class
```python
class Survival_cal:
    # class method
    def duration_of_survival(self):
        # take input from user 
        age = int(input("What's your age? "))  
        unit = input("Please choose time unit: Months, Weeks, Days, Hours, Minutes, Seconds. \nNote: You can write the first letter or the full name of the time unit. ").strip().lower()
        
        months = age * 12
        weeks = months * 4
        days = age * 365
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60

        if unit == 'months' or unit == 'm':
            print(f'You lived for {months:,} Months')

        elif unit == 'weeks' or unit == 'w':
            print(f'You lived for {weeks:,} Weeks')

        elif unit == 'days' or unit == 'd':
            print(f'You lived for {days:,} Days')

        elif unit == 'hours' or unit == 'h':
            print(f'You lived for {hours:,} Hours')

        elif unit == 'minutes' or unit == 'mi':
            print(f'You lived for {minutes:,} Minutes')

        elif unit == 'seconds' or unit == 's':
            print(f'You lived for {seconds:,} Seconds')

        else:
            print('Your choice is not available')

        return
```
## Main Execution
The main part of the script creates an instance of the Survival_cal class and calls the duration_of_survival method:
```python
# object create 
s = Survival_cal()
# call to the method of class 
s.duration_of_survival()

print(
    f'''
\n Expected output example:
\n What's your age? 25
\n Please choose time unit: Months, Weeks, Days, Hours, Minutes, Seconds. 
\n Note: You can write the first letter or the full name of the time unit. d
\n You lived for 9,125 Days
 '''
)
```
## Running the Project
To run this project on your local machine:

1 Ensure Python is installed. You can download it from python.org.

2 Navigate to the project directory:
```sh
cd <project_directory>
```
3 Run the script:
```sh
python <script_name>.py
```
Replace <project_directory> with the path to your project directory and <script_name> with the name of your Python script file, e.g., main.py.

### Future Improvements
* Add additional time units like decades or centuries.
* Implement more robust error handling and input validation.
* Create a graphical user interface (GUI) for better user experience.

### Acknowledgements
Thanks to all who inspired and guided this project.


### Save and Commit the README.md

1. **Save the File:**
   - After writing your `README.md`, save the file by clicking `File > Save` or pressing `Ctrl+S`.

2. **Move the File to Your Local Machine Folder:**
   - If you're using Google Colab, download the `README.md` file to your local machine.
   - Move the `README.md` file to your project directory on your local machine.

3. **Version Control (Optional):**
   - If you are using version control (e.g., Git), you can add and commit the `README.md` file to your repository:
     ```sh
     git add README.md
     git commit -m "Add README.md with project details"
     ```

By following these steps, you will have a detailed `README.md` file in your project directory that explains the project's purpose, design, usage, and other relevant information.

