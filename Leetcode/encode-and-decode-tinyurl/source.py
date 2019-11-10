import uuid

class Codec:

    link = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        short_key = uuid.uuid4().hex[:6]
        self.link[short_key] = longUrl
        return 'http://tinyurl.com/{}'.format(short_key)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        short_key = shortUrl.split('/')[-1]
        return self.link[short_key]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
