let cart = localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : [];
// // store cart in submit form for checkout form
document.getElementById('cart').value = JSON.stringify(cart);

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
                        <h5>$${Math.round(watch.price * item.quantity * 100)/100}</h5>
                    </td>
                `;
                tableBody.prepend(row);
                // update total cart price incrementally for each loaded item
                let prevPrice = Number(document.getElementById('total_price').innerHTML.substring(1));
                document.getElementById('total_price').innerHTML = `$${Math.round((prevPrice + watch.price * item.quantity)*100)/100}`;
            }
        );
    }    
}

function decrement_quantity(id) {
    let item = cart.find(item => item.id === id);
    if (item.quantity > 1) {
        item.quantity--;
        // update input value
        document.getElementById(`cart-item-${id}`).getElementsByClassName('input-number')[0].value = item.quantity;
        // update price for this batch of items
        let item_price = Number(document.getElementById(`cart-item-${id}`).getElementsByTagName('h5')[0].innerHTML.substring(1));
        document.getElementById(`cart-item-${id}`).getElementsByTagName('h5')[1].innerHTML = `$${item.quantity * item_price}`;
    } else {
        cart.splice(cart.indexOf(item), 1);
        let row = document.getElementById(`cart-item-${id}`);
        row.remove();
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    // store cart in submit form
    document.getElementById('cart').value = JSON.stringify(cart);
    update_total_cart_price();
}

function increment_quantity(id) {
    let item = cart.find(item => item.id === id);
    item.quantity++;
    // update input value
    document.getElementById(`cart-item-${id}`).getElementsByClassName('input-number')[0].value = item.quantity;
    // update price for this batch of items
    let item_price = Number(document.getElementById(`cart-item-${id}`).getElementsByTagName('h5')[0].innerHTML.substring(1));
    document.getElementById(`cart-item-${id}`).getElementsByTagName('h5')[1].innerHTML = `$${item.quantity * item_price}`;
    localStorage.setItem('cart', JSON.stringify(cart));
    // store cart in submit form
    document.getElementById('cart').value = JSON.stringify(cart);
    update_total_cart_price();
}

// This function is not called right after fillTableWithCartItems() because all items have not been fetched at that point
function update_total_cart_price() {
    let total_price = 0;
    for (let item of cart) {
        let item_price = Number(document.getElementById(`cart-item-${item.id}`).getElementsByTagName('h5')[0].innerHTML.substring(1));
        total_price += item_price * item.quantity;
    }
    document.getElementById('total_price').innerHTML = `$${Math.round(total_price*100)/100}`;
}

fillTableWithCartItems();