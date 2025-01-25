import http.client
import urllib.parse
import json


def print_data_output(data):
    parsedData = json.loads(data)

    with open("output.json", "w", encoding="utf-8") as json_file:
        json.dump(parsedData, json_file, indent=4)

def get_encoded_title():
    movie = input("Enter Movie Title: ")
    return urllib.parse.quote(movie)

def read_key():
    file = open("apikey.txt", "r")
    return file.read()

def get_movie_data():
    conn = http.client.HTTPSConnection("streaming-availability.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': read_key(),
        'x-rapidapi-host': "streaming-availability.p.rapidapi.com"
    }

    conn.request("GET", f"/shows/search/title?country=us&title={get_encoded_title()}&show_type=movie&output_language=en", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # print(data.decode("utf-8"))
    print_data_output(data)

def main():
    get_movie_data()

if __name__ == '__main__':
    main()