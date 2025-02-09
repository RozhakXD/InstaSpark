const descriptionInput = document.getElementById('description');
const generateBtn = document.getElementById('generateBtn');
const outputSection = document.getElementById('outputSection');
const bioOutput = document.getElementById('bioOutput');
const copyBtn = document.getElementById('copyBtn');

async function generateBio(description) {
    try {
        const response = await fetch('/api/generate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ description }),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Something went wrong');
        }

        return data.message;
    } catch (error) {
        throw new Error(error.message);
    }
}

generateBtn.addEventListener('click', async () => {
    const description = descriptionInput.value.trim();

    if (description) {
        generateBtn.disabled = true;
        generateBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Generating...';

        try {
            const bio = await generateBio(description);

            bioOutput.value = bio;
            outputSection.classList.remove('hidden');

            Swal.fire({
                icon: 'success',
                title: 'Success!',
                text: 'Your bio has been generated successfully.',
                confirmButtonColor: '#3B82F6',
            });
        } catch (error) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: error.message,
                confirmButtonColor: '#EF4444',
            });
        } finally {
            generateBtn.disabled = false;
            generateBtn.innerHTML = '<i class="fas fa-magic mr-2"></i> Generate Bio';
        }
    } else {
        Swal.fire({
            icon: 'warning',
            title: 'Oops...',
            text: 'Please enter a description!',
            confirmButtonColor: '#F59E0B',
        });
    }
});

copyBtn.addEventListener('click', () => {
    bioOutput.select();
    document.execCommand('copy');
    Swal.fire({
        icon: 'success',
        title: 'Copied!',
        text: 'Your bio has been copied to clipboard.',
        confirmButtonColor: '#3B82F6',
    });
});