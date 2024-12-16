const peticion = new XMLHttpRequest();

function cargarMovimientos() {
   
    peticion.open('GET', 'http://127.0.0.1:5000/api/v1/movimientos', false);
    peticion.send();
    const resultado = JSON.parse(peticion.responseText);
    const movimientos = resultado.results;
   

    let html = '';
    for (let i = 0; i < movimientos.length; i++) {        
        const mov = movimientos[i]
        html = html + `   
            <tr class="fila fila-mov">
                <td class="dato">${mov.fecha}</td>
                <td class="dato">${mov.hora}</td>
                <td class="dato">${mov.moneda_origen}</td>
                <td class="dato">${mov.cantidad_origen}</td>
                <td class="dato">${mov.moneda_destino}</td>
                <td class="dato">${mov.cantidad_destino}</td>
                <td class="dato">${mov.precio_unitario}</td>
            </tr>   
        `; 
        
    }
    
   
    const tabla = document.querySelector('#cuerpo-tabla');
    tabla.innerHTML = html;
    const filasMov = document.querySelector('.fila-mov');
   
}

window.onload = function () {
   
    const boton = document.getElementById('boton-recarga');
    boton.addEventListener('click', cargarMovimientos);
    cargarMovimientos()
    
}

