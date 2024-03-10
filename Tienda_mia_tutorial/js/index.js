const contenedorTarjetas = document.getElementById("productos-container");


function crearTarjetasProductosInicio(productos){
    productos.forEach(producto => {
        const nuevaBicicleta = document.createElement("div");
        nuevaBicicleta.classList = "tarjeta-producto";
        nuevaBicicleta.innerHTML = `
            <img src=${producto.img}
        
        `
        contenedorTarjetas.appendChild(nuevaBicicleta);
    });
}



crearTarjetasProductosInicio(bicicletas)