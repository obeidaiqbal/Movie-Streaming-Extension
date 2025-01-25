import http.client
import urllib.parse

conn = http.client.HTTPSConnection("streaming-availability.p.rapidapi.com")

file = open("apikey.txt", "r")
key = file.read()

headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': "streaming-availability.p.rapidapi.com"
}

movie = input("Enter Movie Title: ")
encodedMovie = urllib.parse.quote(movie)

conn.request("GET", f"/shows/search/title?country=us&title={encodedMovie}&show_type=movie&output_language=en", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))