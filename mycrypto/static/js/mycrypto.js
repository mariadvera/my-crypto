const peticion = new XMLHttpRequest();

function cargarMovimientos() {
    console.log('Has llamado a la función para cargar los movimientos');
    peticion.open('GET', 'http://127.0.0.1:5000/api/v1/movimientos', false);
    peticion.send();
    console.log('Respuesta de la API', peticion.status, peticion.statusText, peticion.responseText)
}

window.onload = function () {    
    console.log('Ya  se han cargado los elementos de la página');
    const boton = document.getElementById('boton-recarga');
    boton.addEventListener('click', cargarMovimientos);
    console.log('FIN de la función `window.onload`');
};

// js llama  a la api y recoge los datos de los movimientos