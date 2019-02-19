class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,id,author,title,description,url,urlToImage):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        