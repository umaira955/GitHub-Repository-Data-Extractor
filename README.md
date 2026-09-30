# GitHub Repository Data Extractor



The program extracts information about repositories from GitHub, searching for a particular topic, selecting the number of stars greater than 10,000, displaying this information on the screen, and exporting it to CSV files.



## Features



- Search for topics on GitHub



- Sorting by stars



- Filtering by number of stars



- Display of the name of the repository, its stars, and URL



- Saving data in CSV files



- Handling of errors that may occur during the request



- Prevention of empty CSV files if no ID is found



## Technologies



- Python



- Requests



- CSV



- GitHub API



## Code Description



The program contains several steps. First, you need to enter the topic of the search. Then, the program will perform a request to the GitHub API, after which information about the repositories will be received in JSON format. Further, processing of this data occurs, during which repositories with more than 10,000 stars will be selected. Then, this information will be displayed on the screen and saved in CSV files.



An example of the simplest use of the program would be to enter `python` from the keyboard, after which the program will find the corresponding repositories and save them in the `python_repositories.csv` file.



The program demonstrates working with API requests, processing of JSON data, filtering, errors, and working with CSV files in Python.