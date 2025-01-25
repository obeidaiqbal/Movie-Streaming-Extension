console.log("This is a test popup!")

document.addEventListener("DOMContentLoaded", function () {
    const inputField = document.getElementById("mtitle");
    
    inputField.addEventListener("keydown", function (event) {
        if (event.key === "Enter") { 
            event.preventDefault(); 
            console.log("User Input:", inputField.value.trim());
        }
    });
});
