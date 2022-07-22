let cart = localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : [];
let tableBody = document.getElementById('cart-table').getElementsByTagName('tbody')[0];

function fillTableWithCartItems() {
    for (let item of cart) {
        // request item data from server
        fetch(`/items/${item.id}`)
            .then(response => response.json())
            .then(watch => {
                let row = document.createElement('tr');
                row.id = `cart-item-${watch.id}`;
                row.innerHTML = `
                    <td>
                        <div class="media">
                            <div class="d-flex">
                                <img src="../static/${watch.image_url}.png" />
                            </div>
                            <div class="media-body">
                                <p>${watch.name}</p>
                            </div>
                        </div>
                    </td>
                    <td>
                        <h5>$${watch.price}</h5>
                    </td>
                    <td>
                        <div class="product_count">
                            <span onclick="decrement_quantity(${watch.id})" class="input-number-decrement"> <i class="ti-minus"></i></span>
                                <input class="input-number" type="text" value="${item.quantity}" min="0" max="10">
                            <span onclick="increment_quantity(${watch.id})" class="input-number-increment"> <i class="ti-plus"></i></span>
                        </div
                    </td>
                    <td>
                        <h5>$${watch.price * item.quantity}</h5>
                    </td>
                `;
                tableBody.prepend(row);
            }
        );
    }
}

function decrement_quantity(id) {
    let item = cart.find(item => item.id == id);
    if (item.quantity > 1) {
        item.quantity--;
        // update input value
        document.getElementById(`cart-item-${id}`).getElementsByClassName('input-number')[0].value = item.quantity;
    } else {
        cart.splice(cart.indexOf(item), 1);
        let row = document.getElementById(`cart-item-${id}`);
        row.remove();
    }
    localStorage.setItem('cart', JSON.stringify(cart));
}

function increment_quantity(id) {
    for (let item of cart) {
        console.log(id, item.id);
        if (item.id == id) {
            console.log('found item');
            item.quantity++;
            // update input value
            document.getElementById(`cart-item-${id}`).getElementsByClassName('input-number')[0].value = item.quantity;
        }
    }
    localStorage.setItem('cart', JSON.stringify(cart));
}

fillTableWithCartItems();