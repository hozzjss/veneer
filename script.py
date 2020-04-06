from art import Art
from marketplace import MarketPlace
from listing import Listing
from client import Client

veneer = MarketPlace()


edytta = Client('Edytta Halpirt')

girl_with_mandolin = Art(
    artist='Picasso, Pablo',
    title="Girl with a Mandolin (Fanny Tellier)",
    year=1910,
    medium="oil on canvas",
    owner=edytta
)

moma = Client("The MOMA", "New York", True)
listing = edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')
veneer.add_listing(listing)

veneer.remove_listing(listing)
moma.buy_artwork(listing)

print(girl_with_mandolin)

print(veneer.show_listings())
