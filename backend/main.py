import http.client
import urllib.parse
import json


def print_data_output(data):
    parsedData = clean_data(data)

    with open("output.json", "w", encoding="utf-8") as json_file:
        json.dump(parsedData, json_file, indent=4)

def clean_data(data):
    parsedData = json.loads(data)
    
    cleaned_output = []

    for item in parsedData:
        movie_info = {
            "Title": item.get("title"),
            "Year": item.get("releaseYear"),
            "Runtime": f"{item.get('runtime', 0)} minutes",
            "Genres": [genre["name"] for genre in item.get("genres", [])],
            "Directors": item.get("directors", []),
            "Cast": item.get("cast", []),
            "Overview": item.get("overview", []),
            "Streaming Options": [],
            "Image": item.get("imageSet", {}).get("verticalPoster", {}).get("w480", "")
        }
        if "streamingOptions" in item and "us" in item["streamingOptions"]:
            for option in item["streamingOptions"]["us"]:
                movie_info["Streaming Options"].append({
                    "Service": option["service"]["name"],
                    "Type": option["type"].capitalize(),
                    "Price": (
                        option["service"].get("addon", {}).get("name", "addon") if option["type"] == "addon"
                        else option.get("price", {}).get("formatted", "subscription")
                    ),
                    
                    "Link": option.get("link", "N/A")
                })
                pass
        cleaned_output.append(movie_info)

    return cleaned_output
    
def get_encoded_title():
    movie = input("Enter Movie Title: ")
    return urllib.parse.quote(movie)

def read_key():
    file = open("backend/apikey.txt", "r")
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