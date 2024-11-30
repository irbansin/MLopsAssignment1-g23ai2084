const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const loader = document.getElementById('loader');
const uploadForm = document.getElementById('uploadForm');

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    e.stopPropagation();
    uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', (e) => {
    e.preventDefault();
    e.stopPropagation();
    uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    e.stopPropagation();
    uploadArea.classList.remove('dragover');

    const files = e.dataTransfer.files;
    if (files.length > 0) {
        fileInput.files = files; 
    }
});

uploadArea.addEventListener('click', () => {
    fileInput.click();
});

uploadForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const formData = new FormData(uploadForm);

    loader.style.display = 'block';

    fetch('/uploadfile', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        loader.style.display = 'none';

        alert(data.message);
    })
    .catch(error => {
        loader.style.display = 'none';
        alert('File upload failed');
    });
});