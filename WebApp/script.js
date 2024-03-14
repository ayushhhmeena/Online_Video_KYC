document.getElementById('kyc-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('idCard', document.getElementById('id-card').files[0]);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        document.getElementById('output').textContent = `Verification Status: ${data.status}`;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('output').textContent = 'An error occurred. Please try again later.';
    }
});
