from listing import Listing


class MarketPlace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing: Listing):
        self.listings = self.listings + [new_listing]

    def remove_listing(self, listing: Listing):
        self.listings = [
            item for item in self.listings if item.art != listing.art
        ]

    def show_listings(self):
        for listing in self.listings:
            print(listing)

