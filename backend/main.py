from flask import Flask, request, jsonify
from flask_cors import CORS
import http.client
import urllib.parse
import json

app = Flask(__name__)
CORS(app) 

def read_key():
    file = open("apikey.txt", "r")
    return file.read()

def clean_data(data):
    try:
        parsedData = json.loads(data)
    except json.JSONDecodeError:
        return {"error": "Failed to decode API response"}

    cleaned_output = []

    for item in parsedData:
        movie_info = {
            "Title": item.get("title"),
            "Year": item.get("releaseYear"),
            "Runtime": f"{item.get('runtime', 0)} minutes",
            "Genres": [genre["name"] for genre in item.get("genres", [])],
            "Directors": item.get("directors", []),
            "Cast": item.get("cast", []),
            "Overview": item.get("overview", ""),
            "Streaming Options": [],
            "Image": item.get("imageSet", {}).get("verticalPoster", {}).get("w480", "")
        }

        if "streamingOptions" in item and "us" in item["streamingOptions"]:
            for option in item["streamingOptions"]["us"]:
                price = option.get("price", {}).get("formatted", "subscription")
                if option["type"] == "addon":
                    price = option["service"].get("addon", {}).get("name", "addon")
                movie_info["Streaming Options"].append({
                    "Service": option["service"]["name"],
                    "Type": option["type"].capitalize(),
                    "Price": price,
                    "Link": option.get("link", "N/A")
                })

        cleaned_output.append(movie_info)

    return cleaned_output

def get_movie_data(title):
    conn = http.client.HTTPSConnection("streaming-availability.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': read_key(),
        'x-rapidapi-host': "streaming-availability.p.rapidapi.com"
    }

    conn.request("GET", f"/shows/search/title?country=us&title={urllib.parse.quote(title)}&show_type=movie&output_language=en", headers=headers)

    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

@app.route('/get-movie', methods=['GET'])
def get_movie():
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Missing 'title' parameter"}), 400

    raw_data = get_movie_data(title)
    cleaned_output = clean_data(raw_data)

    return jsonify(cleaned_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run Flask on port 5000
