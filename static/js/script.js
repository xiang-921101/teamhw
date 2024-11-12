// Function to load an HTML file into an element
function loadHTML(elementId, filePath) {
    fetch(filePath)
        .then(response => response.text())
        .then(data => {
            document.getElementById(elementId).innerHTML = data;
        })
        .catch(error => console.error('Error loading file:', error));
}

// Load header and footer
loadHTML('header', 'header.html');
loadHTML('footer', 'footer.html');
