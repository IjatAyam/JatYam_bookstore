from django.conf import settings
from shop.models import Product

from decimal import Decimal


class Wishlist(object):
    def __init__(self, request):
        """
        Initialize the wishlist.
        """
        self.session = request.session
        wishlist = self.session.get(settings.WISHLIST_SESSION_ID)
        if not wishlist:
            # save an empty wishlist in the session
            wishlist = self.session[settings.WISHLIST_SESSION_ID] = {}
        self.wishlist = wishlist
        # Check for deleted items
        self.check()

    def check(self):
        for product_id in list(self.wishlist):
            try:
                Product.objects.get(id=int(product_id))
            except:
                del self.wishlist[product_id]

    def add(self, product):
        """
        Add a product to wishlist.
        """
        product_id = str(product.id)
        self.wishlist[product_id] = {'price': str(product.price)}
        self.save()

    def save(self):
        # Mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def __iter__(self):
        """
        Iterate over the items in the wishlist and get the products
        from the database.
        """
        products_ids = self.wishlist.keys()
        # get the products objects and add them to the wishlist
        products = Product.objects.filter(id__in=products_ids)

        wishlist_session = self.wishlist.copy()
        wishlist = {}
        for product in products:
            wishlist[str(product.id)] = {'product': product}

        for item, item_s in zip(wishlist.values(), wishlist_session.values()):
            item['per_now'] = 0
            item['price'] = Decimal(item_s['price'])
            if product.price != item['price']:
                new_price = Decimal(item['product'].price)
                old_price = Decimal(item['price'])
                per_now = (new_price - old_price) / old_price * Decimal('100')
                item['per_now'] = int(per_now)
            yield item

    def remove(self, product):
        """
        Remove a product from the wishlist
        """
        product_id = str(product.id)
        if product_id in self.wishlist:
            del self.wishlist[product_id]
            self.save()

    def __len__(self):
        """
        Count all items in the wishlist.
        """
        return sum(1 for item in self.wishlist.values())

    def clear(self):
        # remove wishlist from session
        del self.session[settings.WISHLIST_SESSION_ID]
        self.save()
