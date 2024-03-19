class Codec:
    def __init__(self):
        self.map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        self.map[id(longUrl)] = longUrl
        return id(longUrl)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.map[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
