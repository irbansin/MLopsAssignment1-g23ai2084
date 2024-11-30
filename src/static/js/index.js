const etlBtn = document.querySelector('#etl-btn')

etlBtn.addEventListener('click',(e)=>{
    e.stopPropagation();
    e.preventDefault();

    fetch('/startetl', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        loader.style.display = 'none';
        alert(data.message);
    })
    .catch(error => {
        loader.style.display = 'none';
        alert('ETL Process failed');
        console.error('ETL Process failed:'+ error);
    });
})