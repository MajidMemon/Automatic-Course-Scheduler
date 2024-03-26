// Function to update the generation number in the HTML
function updateGenerationNumber(generationNum) {
    document.getElementById('generation-number').innerText = generationNum;
}

// Function to show loading message and start generating timetable
function generateTimetable() {
    document.getElementById('loading-message').style.display = 'block'; // Show loading message
    // Optionally, show a loading spinner if you have one
    // Update UI with the generation number (if applicable)
    // You can use AJAX to fetch the generation number from the server and update the UI dynamically
    // For now, let's assume you have access to the generation number variable
    var generationNum = 0; // Replace this with the actual generation number
    updateGenerationNumber(generationNum); // Update the HTML with the generation number
}
