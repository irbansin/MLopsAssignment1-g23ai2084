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

        let columns = data.message.x_columns;
        createInputElements(columns);
    })
    .catch(error => {
        loader.style.display = 'none';
        alert('File upload failed: '+error);
    });
});

function createInputElements(qty) {
    let featureInput = document.querySelector('#feature-input');
    featureInput.innerHTML = '';

    let form = document.createElement('form');
    form.className = 'dynamic-form';

    for (let i = 1; i <= qty; i++) {
        let label = document.createElement('label');
        label.setAttribute('for', `field-${i}`);
        label.textContent = `Field ${i}:`;

        let input = document.createElement('input');
        input.type = 'number';
        input.name = `field-${i}`;
        input.id = `field-${i}`;

        form.appendChild(label);
        form.appendChild(input);
    }

    let submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = 'Submit';
    form.appendChild(submitButton);

    featureInput.appendChild(form);

}