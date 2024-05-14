Overview

This project is designed to automate the process of booking a gym session on the Routine Gym website. The script uses Selenium to navigate the website, select the desired time slot, and log in with provided credentials. The booking process is scheduled to run at 04:30 AM every day to secure a slot for the following week.

 Features

- Automated Booking: Uses Selenium to navigate the Routine Gym website and book a session.
- Scheduling: Runs the booking process at a specified time every day.
- Error Handling: Includes basic error handling to retry booking if the preferred time slot is not available.
- Email Notification: Sends an email notification upon successful booking (optional, not included in the current script).

 Prerequisites

- Python 3.x
- Selenium
- ChromeDriver (or another WebDriver compatible with your browser)
- Required Python packages (listed in `requirements.txt`)

 Project Structure

```
gym_booking_automation/
├── app/
│   ├── static/
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── booking.py
│   ├── scheduler.py
│   └── utils.py
├── tests/
├── requirements.txt
└── run.py
```

 Files

- `app/booking.py`: Contains the main script for booking a gym session.
- `app/scheduler.py`: Schedules the script to run at a specific time.
- `app/utils.py`: Utility functions (e.g., sending email notifications).
- `app/__init__.py`: Initializes the Flask application.
- `app/forms.py`: Defines the form used in the Flask application.
- `app/models.py`: Database models (if needed).
- `app/routes.py`: Flask routes for handling web requests.
- `app/templates/index.html`: HTML template for the web interface.
- `requirements.txt`: Lists the Python dependencies.
- `run.py`: Entry point to run the Flask application.

 Setup

 Step 1: Install Python and Pip

Ensure you have Python 3 and pip installed on your machine. You can download Python from the official [Python website](https://www.python.org/).

 Step 2: Install Dependencies

Navigate to the project directory and install the required Python packages:

```bash
pip install -r requirements.txt
```

 Step 3: Set Up ChromeDriver

Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it is in your system PATH. You can do this by adding the directory containing `chromedriver` to your PATH environment variable.

 Step 4: Configure Environment Variables

Set up the necessary environment variables for email notifications in your operating system. You can do this by adding the following to your `.bashrc`, `.zshrc`, or `.profile` file on Unix-based systems, or through the Environment Variables settings on Windows:

```bash
export EMAIL_SENDER="your_email@example.com"
export EMAIL_PASSWORD="your_password"
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT=587
```

 Step 5: Run the Flask Application

Start the Flask application to serve the web interface:

```bash
python run.py
```

Open a web browser and navigate to `http://127.0.0.1:5000` to access the web interface. Fill in the required fields and submit the form to schedule the booking.

 Step 6: Schedule the Script

 On Unix-based Systems (Linux, macOS)

1. Open the crontab file for editing:

```bash
crontab -e
```

2. Add the following line to schedule the script to run at 04:30 AM every day:

```bash
30 4 * * * /usr/bin/python3 /path/to/your/booking.py
```

Replace `/usr/bin/python3` with the path to your Python interpreter and `/path/to/your/booking.py` with the path to your Python script.

 On Windows

1. Open Task Scheduler from the Start menu.

2. Create a New Basic Task:
- Name: Gym Booking
- Trigger: Daily at 04:30 AM
- Action: Start a program

3. Configure the Action:
- Program/script: `python`
- Add arguments: `C:\path\to\your\booking.py`

 Script Details

 `booking.py`

This script handles the automated booking process. It uses Selenium to:
1. Navigate to the Routine Gym website.
2. Select the "Small Group" option.
3. Move one week forward at 04:30 AM.
4. Attempt to book the 8:00 PM – 9:00 PM slot. If unavailable, attempt the 9:00 PM – 10:00 PM slot.
5. Enter the provided email and password to log in and complete the booking.

 `scheduler.py`

Schedules the `booking.py` script to run at 04:30 AM every day. This ensures that the booking process is triggered automatically without manual intervention.

 `utils.py`

Contains utility functions such as sending email notifications. This can be extended to include other helper functions as needed.

 `forms.py`

Defines the form used in the Flask application to collect user input for email, password, booking time, and system open date.

 `models.py`

Defines the database models if needed for storing user data or booking history.

 `routes.py`

Defines the routes for the Flask application, handling form submissions and triggering the booking process.

 `index.html`

HTML template for the web interface. It contains a form that users can fill out to schedule their gym bookings.

 Testing

To test the script, you can manually run `booking.py` and verify that it completes the booking process successfully. You can also test the Flask application by navigating to the web interface and submitting the form.

 Troubleshooting

If you encounter issues with the booking process, check the following:
- Ensure that ChromeDriver is correctly installed and in your system PATH.
- Verify that your email and password are correct and that the SMTP server settings are properly configured.
- Check the logs for any error messages that might indicate what went wrong.

By following this guide, you should be able to set up and run the gym booking automation script locally on your machine without any costs. If you have any questions or need further assistance, feel free to ask!
