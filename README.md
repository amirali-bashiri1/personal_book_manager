# Personal Book Manager

![Python](https://img.shields.io/badge/Python-3.12-blue)

A simple book management project built with Python.
This project helps users manage their personal book collection.

## Features

- Add multiple books
- Display books
- Save books
- Load saved books
- Set priority for each book
- Admin Mode

## Book Priority

Each book can have one of three priority levels:

- `low`
- `medium`
- `high`

The program asks the user to choose a priority when adding a book. It also checks whether the entered priority is valid.

## Requirements

- Python
- python-dotenv

## Installation

Install the required packages using:

```bash
python -m pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project folder.

The `.env.example` file is a template that shows which environment variable is needed.

The required variable is `BOOK_MANAGER_ADMIN_PASSWORD`.

Add this to your `.env` file:

```env
BOOK_MANAGER_ADMIN_PASSWORD=your_password_here
```

Replace `your_password_here` with your own password.

**Important:** Do not upload `.env` to GitHub. Only upload `.env.example`.

## Run the Program

The main file of the project is `main.py`.

Run the program using:

```bash
python main.py
```

## Screenshot

![Program Screenshot](images/screenshot.png.png)

## Project Structure

- `main.py` — The main file that runs the program and handles user interactions.
- `books.py` — Contains functions for displaying and managing books.
- `.gitignore` — Prevents unnecessary and private files from being uploaded to GitHub.
- `.env.example` — Shows which environment variable is needed for Admin Mode.
- `requirements.txt` — Lists the external Python packages required by the project.
- `images/` — Contains screenshots of the program for the README.

## How It Works

1. The program starts by running `main.py`.
2. It loads environment variables from the `.env` file.
3. It loads previously saved books from `books.json`.
4. The user can add new books and choose a priority.
5. The program checks the selected priority.
6. The program displays the books and their priorities.
7. Book information is saved in `books.json`.
8. Admin Mode allows access to the admin section using the password stored in the `.env` file.

## Troubleshooting

### 1. FileNotFoundError

- **What does it mean?** The program cannot find a required file.
- **Why can it happen?** The file may not exist or the program may be running from the wrong folder.
- **What should I check first?** Check the project folder and make sure the required file exists.

### 2. JSONDecodeError

- **What does it mean?** The program cannot read the JSON data.
- **Why can it happen?** The `books.json` file may be empty or contain invalid JSON.
- **What should I check first?** Check whether `books.json` contains valid JSON data.

### 3. ModuleNotFoundError: No module named 'dotenv'

- **What does it mean?** Python cannot find the `python-dotenv` package.
- **Why can it happen?** The package may not be installed.
- **What should I check first?** Run `python -m pip install -r requirements.txt`.

### 4. Admin Password Not Working

- **What does it mean?** The program cannot read the Admin Mode password correctly.
- **Why can it happen?** The `.env` file may be missing, the variable name may be incorrect, or `load_dotenv()` may not be called.
- **What should I check first?** Check that `.env` exists, contains `BOOK_MANAGER_ADMIN_PASSWORD`, and that `load_dotenv()` runs before `os.getenv()`.
