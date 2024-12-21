
const peticion = new XMLHttpRequest();

function cargarMovimientos() {
    console.log('Has llamado a la función para cargar los movimientos');
    peticion.open('GET', 'http://127.0.0.1:5000/api/v1/movimientos', false);
    peticion.send();
    const resultado = JSON.parse(peticion.responseText);
    const movimientos = resultado.results;
    console.log('Movimientos', movimientos);

    let html = '';

    for (let i = 0; i < movimientos.length; i++) {
        const mov= movimientos[i]
        html = html + ` 
                  
                    <tr class='fila>
                        <td>${mov.fecha}</td>
                        <td>${mov.hora}</td>
                        <td>${mov.moneda_origen}</td>
                        <td>${mov.cantidad_origen}</td>
                        <td>${mov.moneda_destino}</td>
                        <td>${mov.cantidad_destino}</td>
                        <td>${mov.precio_unitario}</td>
                    </tr>
                 `;
    }
    console.log('html', html);
    const tabla = document.querySelector('#cuerpo-tabla');
    tabla.innerHTML = html;
}
window.onload = function () {
    console.log('Ya se han cargado los elementos de la pagina');
    const boton = document.getElementById('boton-recarga');
    boton.addEventListener('click', cargarMovimientos);    
    console.log('fin de la función window on load');    

}


