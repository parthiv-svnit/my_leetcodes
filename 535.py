class Codec:
    keych = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.longUrl = longUrl
        self.key = Codec.keych
        Codec.keych += 1
        self.di = {self.key: self.longUrl}
        return str(self.key)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        self.shortUrl = shortUrl
        return self.di[self.key]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))