document.addEventListener('DOMContentLoaded', function () {
    console.log('prediction.js is successfully connected!');

    fetch('http://localhost:3000/predictions')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Filter the data for StudentID 1000
            const filteredData = data.filter(item => item.StudentID === 1000);

            // Prepare HTML content
            let content = '';
            filteredData.forEach(item => {
                // Assuming 'PredictedOutcome' is the property you want to display
                content += `<p>AssignmentID: ${item.AssignmentID}, PredictedOutcome: ${item.PredictedOutcome}</p>`;
            });

            // Display the data
            document.getElementById('courseContainer').innerHTML = content;
        })
        .catch(error => console.error('Fetch error:', error));
});
