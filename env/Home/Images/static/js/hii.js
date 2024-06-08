document.getElementById('convertButton').addEventListener('click', function() {
    // Add code here to handle image to speech conversion
    // Display the converted text in the #output element
});

document.getElementById('imageInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const output = document.getElementById('output');
            output.innerHTML = ''; // Clear any previous content
            const img = document.createElement('img');
            img.src = e.target.result;
            img.style.maxWidth = '100%'; // Ensure the image fits within its container
            output.appendChild(img);

            // Display image preview
            const imagePreview = document.getElementById('imagePreview');
            const uploadedImage = document.getElementById('uploadedImage');
            uploadedImage.src = e.target.result;
            imagePreview.style.display = 'block';
        }
        reader.readAsDataURL(file);
    }
});
