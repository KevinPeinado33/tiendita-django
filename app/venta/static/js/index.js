/**
 * Despues de que carge la pagina recién 
 * ejecutaremos las funcione dento la callback
 */
window.addEventListener('load', () => {
    getProductos()
})

/**
 * llamado de peticiones
 */
const getProductos = async () => {

    const productos = await fetch('/api/productos').then( res => res.json() )

    console.log({ productos })

    let productosInTable = ''

    productos.forEach( ({ fields: producto, pk }) => {
        productosInTable += `
            <tr>
                <td>
                    <div class="flex items-center space-x-3">
                        <div class="avatar">
                        <div class="mask mask-squircle w-12 h-12">
                            <img src="${ producto.url_producto }" alt="Avatar Tailwind CSS Component" />
                        </div>
                        </div>
                        <div>
                            <div class="font-bold">${ producto.nombre }</div>
                        </div>
                    </div>
                </td>
                <td>
                    <span class="badge badge-ghost badge-sm">${ producto.tipo }</span>
                </td>
                <td>${ producto.cantidad }</td>
                <td>${ producto.precio }</td>
                <th>
                    <button class="btn btn-ghost btn-xs">editar</button>
                    <button 
                        class="btn btn-ghost btn-xs"
                        onclick="${deleteProductoById( pk )}">
                        eliminar
                    </button>
                </th>
            </tr>
        `
    })

    tblProductos.innerHTML = productosInTable

}

const deleteProductoById = (id) => {

    console.log('estas borrando lo sgte', id)

    Swal.fire({
        title: '¿Quieres borrar este producto?',
        text: "No podras recuperarlo mas adelante!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, borrar'
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire(
                'Deleted!',
                'Your file has been deleted.',
                'success'
                )
            }
    })

    return

    //const response = await fetch(`/api/productos/${ id }`).then( res => res.json() )

}
