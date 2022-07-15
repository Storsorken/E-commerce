from timezone.models import Watch
from timezone import db


def create_watches():
    watches = [
        Watch(name='Casio Linage', price=199.99, description='The Casio Linage is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/1'),
        Watch(name='Casio G-Shock MTG-100', price=100, description='The Casio G-Shock MTG-100 is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/2'),
        Watch(name='Rolex Daytona', price=10000.99, description='The Rolex Daytona is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/3'),
        Watch(name='Longines Master', price=699.99, description='The Longines Master is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/4'),
        Watch(name='Seiko prospex alpinist', price=800.99, description='The Seiko prospex alpinist is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/5'),
        Watch(name='Seiko presage cocktail time', price=350.99, description='The Seiko presage cocktail time is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/6'),
        Watch(name='Omega speedmaster', price=6999.99, description='The Omega speedmaster is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/1'),
        Watch(name='Omega seamaster', price=5999.99, description='The Omega seamaster is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/2'),
        Watch(name='Orient bambino', price=119.99, description='The Orient bambino is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/3'),
        Watch(name='Orient mako', price=139.99, description='The Orient mako is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/4'),
        Watch(name='Rolex datejust', price=11999.99, description='The Rolex datejust is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/5'),
        Watch(name='Rolex submariner', price=13999.99, description='The Rolex submariner is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/6'),
        Watch(name='Audemars Piguet Royal Oak', price=45000.00, description='The Audemars Piguet is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/1'),
        Watch(name='Seiko snxs79', price=100.00, description='The Seiko snxs79 is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/2'),
        Watch(name='Seiko turtle', price=300.00, description='The Seiko turtle is a stylish watch that features a large, round dial.', image_url='assets/img/gallery/shop/3'),
    ]
    for watch in watches:
        db.session.add(watch)
    db.session.commit()


create_watches()