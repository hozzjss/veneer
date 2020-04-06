from art import Art
from listing import Listing


class Client:
    def __init__(self, name: str, location="Private Collection", is_museum=False):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def sell_artwork(self, artwork: Art, price: str):
        if (self == artwork.owner):
            listing = Listing(artwork, price, self)
            return listing

    def buy_artwork(self, artwork: Listing):
        if (artwork.art.owner != self):
            artwork.art.owner = self
