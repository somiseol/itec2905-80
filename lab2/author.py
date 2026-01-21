class Author:
    def __init__(self, name):
        self.name = name
        self.books = [] 

    def publish(self, title):
        if title in self.books:
            print(f"duplicate error: {title}")
            # raise error?
        else:
            self.books.append(title)

    def __str__(self):
        return f"{self.name} {self.books}"

def main():
    # test case w books
    chambers = Author("Robert W Chambers")
    chambers.publish("The King in Yellow")
    chambers.publish("The Maker of Moons")
    chambers.publish("The Prophets' Paradise")
    print(chambers)

    # test case w/o books
    bierce = Author("Ambrose Bierce")
    print(bierce)

    # test case w duplicates
    zweig = Author("Stefan Zweig")
    zweig.publish("Beware of Pity")
    zweig.publish("Fear")
    zweig.publish("Fear") # duplicate
    print(zweig)

main()
