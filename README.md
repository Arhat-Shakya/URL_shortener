# Python URL Shortener

A terminal-based URL shortener built with Python that generates unique short codes for URLs, stores URL mappings locally, and opens the original URLs in a web browser.

## Features

- **Short Code Generation:** Generates random short codes using letters and digits.
- **URL Storage:** Stores URL information in a local file.
- **Add URLs:** Save URLs with custom nicknames.
- **Remove URLs:** Remove saved URLs using their nicknames.
- **Change Nicknames:** Update the nickname associated with a saved URL.
- **Fetch URLs:** Retrieve a URL using its short code and open it in the default web browser.
- **Readable Report:** Generates a separate text file to display saved URL information in a readable format.

## Technologies Used

- Python
- File Handling
- Lists and Dictionaries
- Object-Oriented Programming (OOP)
- `ast` for reading stored Python literal data
- `secrets` and `string` for generating random short codes
- `webbrowser` for opening URLs

## How It Works

1. The user enters a URL and assigns it a nickname.
2. The program generates a random short code.
3. The URL, nickname, and short code are stored locally.
4. The user can retrieve a saved URL using its short code.
5. The program opens the original URL in the default web browser.

## Requirements

- Python 3
- A web browser

No external Python packages are required.

## How to Run

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Run the Python program:

   ```bash
   python main.py
   ```

   Replace `main.py` with the actual name of your Python file if it is different.

4. Follow the instructions displayed in the terminal.

Make sure the required storage file exists if your program expects to read it when starting.

## Storage

The program uses local text files to store URL information and generate a readable report.

- `storage.txt`: Stores URL mappings.
- `show.txt`: Displays saved URL information in a readable format.

These files are managed locally by the program.

## Learning Goals

This project was built to practice:

- Python functions and classes
- Lists and dictionaries
- Loops and conditional statements
- File reading and writing
- Generating random codes
- Checking for duplicate short codes
- Recursion and function return values
- Using Python's built-in modules

## Limitations

- The program runs in the terminal and does not provide a graphical user interface.
- Short codes work within this local program; they are not public web links that can be shared with other people.
- URL mappings are stored in local files rather than a database.
- The program requires access to the saved data files to retrieve previously stored URLs.

## Future Improvements

- Add stronger input validation and error handling.
- Prevent duplicate nicknames.
- Replace text-file storage with SQLite.
- Add a graphical interface or web interface.
- Build a web-based version with shareable short links.

## Author

Created as a Python learning project to develop practical programming and problem-solving skills.
