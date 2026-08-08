# Python Practice Projects

This repository contains beginner Python projects built while learning core programming concepts — no AI-generated code, everything written and debugged by hand to build real understanding.

## What I'm Learning
This repo tracks my progress learning Python fundamentals — starting with basic loops and conditionals, moving into functions, exception handling, object-oriented programming (classes), file I/O, and now working with external APIs and libraries. Each project builds on concepts from the previous one.

## Projects

### 1. CLI Calculator
A command-line calculator supporting addition, subtraction, multiplication, and division, with a continuous menu loop and robust error handling.

**Concepts practiced:** functions (`def`, parameters, `return`), multiple exception handling (`ValueError`, `ZeroDivisionError`), `if/elif/else` chains, the `in` keyword for checking valid options.

**Run it:**
---

### 2. Contact Book App
A menu-driven contact manager that lets users add, view, and delete contacts, storing each one as an object.

**Concepts practiced:** classes, `__init__`, `self`, object attributes, storing objects in a list, looping through objects, search-and-remove logic using flag variables.

**Run it:**
---

### 3. Expense Tracker
A CLI app for logging and tracking expenses, with data saved to a file so it persists between runs.

**Concepts practiced:** file I/O (`open`, `with`, reading/writing/appending), string splitting and parsing, exception handling for missing files (`FileNotFoundError`), running totals, menu-driven loops.

**Run it:**
---

### 4. Number Guessing Game
A CLI game where the program picks a random number (1-100) and the user tries to guess it, with feedback on each guess (too high/too low) and a tracked attempt count.

**Concepts practiced:** loops (`while`), nested loops, conditionals, exception handling (`try/except`), input validation, replay logic using flag variables.

**Run it:**

### 6. Rock Paper Scissors
A CLI game where the player competes against the computer, with win/tie/loss detection and input validation.

**Concepts practiced:** the `random` module (`random.choice`), boolean logic with multiple `and`/`or` conditions, exception handling with a manually raised `ValueError`, list membership checks (`in`).

**Run it:**
```
python rock_paper_scissors/rock_paper_scissors.py
```

### 5. Weather CLI App
A command-line app that fetches real-time weather data for any city using the OpenWeatherMap API.

**Concepts practiced:** working with external libraries (`requests`), making HTTP requests, parsing nested JSON responses, handling API errors (`KeyError` for invalid cities), protecting sensitive data (API keys) using a separate config file excluded via `.gitignore`.

**Setup:**
1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Create a `config.py` file inside `weather_cli_app/` with:
```python
   api_key = "your_api_key_here"
```
   (see `config_example.py` for the format)

**Run it:**
```
python weather_cli_app/weather.py
```
