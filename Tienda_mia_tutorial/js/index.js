const contenedorTarjetas = document.getElementById("productos-container");


function crearTarjetasProductosInicio(productos){
    productos.forEach(producto => {
        const nuevaBicicleta = document.createElement("div");
        nuevaBicicleta.classList = "tarjeta-producto";
        nuevaBicicleta.innerHTML = `
            <img src="./images/productos/${producto.id}.jpg">
            <h3>${producto.nombre}</h3>
            <p>$${producto.precio}</p>
            <button>Agregar al carrito</button>
        `
        contenedorTarjetas.appendChild(nuevaBicicleta);
    });
}



crearTarjetasProductosInicio(bicicletas);