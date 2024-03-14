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

document.getElementById('id-card-form').addEventListener('submit', (e) => {
    e.preventDefault();
    window.location.href = 'face-verification.html';
});

function verifyFace() {
    window.location.href = 'user-details-verification.html';
}


document.getElementById('user-details-form').addEventListener('submit', (e) => {
    e.preventDefault();
});