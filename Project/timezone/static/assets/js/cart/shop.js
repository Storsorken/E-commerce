let addBtns = document.getElementsByClassName('img-cap');
let cart = localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : [];

for (btn of addBtns) {
    btn.addEventListener('click', addToCartBtn);
}

function addToCartBtn() {
    let id = this.id.split('-')[1];
    let item = {
        id: id,
        quantity: 1
    };
    // if id already in cart, increase quantity
    if (cart.find(item => item.id === id)) {
        let index = cart.findIndex(item => item.id === id);
        cart[index].quantity++;
    } else {
        cart.push(item);
    }
    // store cart in local storage
    localStorage.setItem('cart', JSON.stringify(cart));
}

