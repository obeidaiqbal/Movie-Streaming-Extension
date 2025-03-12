import React, { useState } from "react";

function App() {
  const [movieTitle, setMovieTitle] = useState("");
  const [message, setMessage] = useState("");

  const handleSearch = () => {
    if (!movieTitle.trim()) {
      setMessage("Please enter a movie title."); // Prevents an empty search
      return;
    }

    setMessage(`Searching for: ${movieTitle}`);
    fetch(`http://34.205.24.0:5000/get-movie?title=${encodeURIComponent(movieTitle)}`)
      .then(response => response.json())
      .then(data => console.log("Movie API Response:", data))
      .catch(error => console.error("Error fetching movie data:", error));
  };

  return (
    <div
      style={{
        width: "300px",
        height: "200px",
        padding: "10px",
        textAlign: "center",
        backgroundColor: "white",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <h2>Movie Finder</h2>
      <input
        type="text"
        placeholder="Enter movie title"
        value={movieTitle}
        onChange={(e) => setMovieTitle(e.target.value)} 
      />
      <button onClick={handleSearch}>Search</button> {/* Runs handleSearch after a click */}
      
      {message && <p>{message}</p>} {/* Displays search result message */}
    </div>
  );
}

export default App;
