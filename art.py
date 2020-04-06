class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{artist}. \"{title}\". {year}, {medium}. {owner_name}, {owner_location}.".format(
            artist=self.artist,
            title=self.title,
            medium=self.medium,
            year=self.year,
            owner_name=self.owner.name,
            owner_location=self.owner.location
        )
