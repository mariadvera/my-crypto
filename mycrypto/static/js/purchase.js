
function calculate() {
    console.log('Has llamado a la función calculate  para obtener cantidad destino y precio unitario');

    // obtiene los valores del formulario

    const monedaOrigen = document.getElementById('from_currency').value;
    const cantidadOrigen = parseFloat(document.getElementById('from_amount').value);
    const monedaDestino = document.getElementById('to_currency').value;

    // Valida que los campos no estén vacíos
    if (!monedaOrigen || !cantidadOrigen || !monedaDestino) {
        alert('Por favor completa todos los campos.');
        return;
    }
   
    // crea una solicitud  para enviar datos al servidor flask
     const peticion = new XMLHttpRequest();
     peticion.open('POST', 'http://127.0.0.1:5000/api/calculate', false);
     peticion.send(JSON.stringify({
        moneda_origen: monedaOrigen,
        cantidad_origen: cantidadOrigen,
        moneda_destino: monedaDestino
     }));
    
     // actualiza los campos del formulario con la respuesta del servidor
    const response = JSON.parse(peticion.responseText);
    document.getElementById('unit_price').value = response.unit_price ;
    document.getElementById('to_amount').value = response.to_amount ;       
    
  
}
// Función para confirmar la compra
function confirmPurchase() {
    console.log('Has llamado a la funcion confirmPurchase  para confirmar  la transacción');

    // Obtener valores del formulario
    const fromCurrency = document.getElementById('from_currency').value;
    const fromAmount = parseFloat(document.getElementById('from_amount').value);
    const toCurrency = document.getElementById('to_currency').value;
    const unitPrice = parseFloat(document.getElementById('unit_price').value);
    const toAmount = parseFloat(document.getElementById('to_amount').value);

    // Validar los campos
    if (!fromCurrency || !fromAmount || !toCurrency || !unitPrice || !toAmount) {
        alert('Por favor, debes completar los campos');
        return;
    }

    // Crear la solicitud XMLHttpRequest
    const peticion = new XMLHttpRequest();
    peticion.open('POST', 'http://127.0.0.1:5000/api/v1/purchase' ,false);   

    // Crear el objeto con la respuesta 
    const requestData = {
        action: 'confirm',
        from_currency: fromCurrency,
        from_amount: fromAmount,
        to_currency: toCurrency,
        unit_price: unitPrice,
        to_amount: toAmount
    };

    // Enviar la solicitud con los datos como JSON
    peticion.send(JSON.stringify(requestData));
}

// Asocia las funciones a los botones
const simulateButton = document.getElementById('simulate');
simulateButton.addEventListener('click', calculate);
const confirmButton = document.getElementById('confirm');
confirmButton.addEventListener('click', confirmPurchase);

  

