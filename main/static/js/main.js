document.getElementById('upload-button').addEventListener('click', function () {
    const fileInput = document.getElementById('file-input');
    const resultDiv = document.getElementById('result');

    if (!fileInput.files[0]) {
        resultDiv.innerHTML = "<p style='color: red;'>Please upload a file first!</p>";
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    resultDiv.innerHTML = "<p>Processing your image...</p>";

    fetch('/classify', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<p style='color: red;'>${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `
                    <h4>Classification Result:</h4>
                    <p>Plastic Type: ${data.label}</p>
                    <p>Confidence: ${data.confidence}</p>
                `;
            }
        })
        .catch(error => {
            console.error(error);
            resultDiv.innerHTML = "<p style='color: red;'>An error occurred. Please try again.</p>";
        });
});
