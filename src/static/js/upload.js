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
            alert('File upload failed: ' + error);
        });
});

async function createInputElements(qty) {
    let featureInput = document.querySelector('#feature-input');
    featureInput.innerHTML = '';

    let gridContainer = document.createElement('div');
    gridContainer.className = 'grid-container';

    let predictForm = document.createElement('form');
    predictForm.className = 'dynamic-form';

    for (let i = 1; i <= qty; i++) {
        let label = document.createElement('label');
        label.setAttribute('for', `field-${i}`);
        label.textContent = `Field ${i}:`;
    
        let input = document.createElement('input');
        input.type = 'number';
        input.step = '0.01'
        input.name = `field-${i}`;
        input.id = `field-${i}`;
    
        // Wrap label and input in a single grid item
        let gridItem = document.createElement('div');
        gridItem.className = 'grid-item';
        gridItem.appendChild(label);
        gridItem.appendChild(input);
    
        gridContainer.appendChild(gridItem);
    }
    predictForm.appendChild(gridContainer);

    // Create the submit button
    let submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = 'Submit';

    let buttonContainer = document.createElement('div');
    buttonContainer.className = 'button-container';
    buttonContainer.appendChild(submitButton);

    predictForm.appendChild(buttonContainer);

    featureInput.appendChild(predictForm);

    predictForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const formData = new FormData(predictForm);

        loader.style.display = 'block';

        fetch('/getPrediction', {
            method: 'POST',
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                loader.style.display = 'none';

                let mvValue = data.message.mvValue;
                mvValueDiv = document.querySelector('#mvvalue')
                mvValueDiv.innerHTML = mvValue.toFixed(2)
            })
            .catch(error => {
                loader.style.display = 'none';
                alert('File upload failed: ' + error);
            });
    })
}
