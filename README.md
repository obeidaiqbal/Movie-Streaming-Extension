## Movie Streaming Extension
This is meant to be an extension that allows you to search for the most accurate streaming and renting data for a movie, this is intended to work hand and hand with letterboxd. The program uses a api from [https://rapidapi.com/hub](https://rapidapi.com/hub) to pull the most current streaming and renting data. It then uses an AWS EC2 instance to host a Flask backend that processes movie search queries. The backend fetches data from the API, cleans and formats it, and returns structured JSON responses. The Chrome extension interacts with this backend by sending user-inputted movie titles, retrieving availability details, and displaying streaming and rental options for the user in real time.

Pushing: 
  ```sh
  git add .
  git commit -m "comment"
  git push origin main
  ```
Pulling:
  ```sh
  git pull origin main
  ```
To Run the main.py flask instance locally:
1. Activate the virtual enviornment & run main.py
  ```sh
  source venv/bin/Activate
  cd backend
  python3 main.py
  ```
2. In a web broswer enter to test a seach (update address portion with whats in terminal)
  ```sh
  {address}/get-movie?title=Star%20Wars
  ```
