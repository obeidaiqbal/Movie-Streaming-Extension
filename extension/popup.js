console.log("Movie Streaming Finder Extension Loaded");

document.addEventListener("DOMContentLoaded", function () {
    const inputField = document.getElementById("mtitle");

    inputField.addEventListener("keydown", function (event) {
        if (event.key === "Enter") { 
            event.preventDefault(); 
            const movieTitle = inputField.value.trim();
            
            if (movieTitle) {
                fetch(`http://(publicipv4ec-2instanceaddress)/get-movie?title=${encodeURIComponent(movieTitle)}`)
                    .then(response => response.json())
                    .then(data => console.log("Movie API Response:", data))
                    .catch(error => console.error("Error fetching movie data:", error));
            }
        }
    });
});
