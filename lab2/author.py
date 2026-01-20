class Author:
    def __init__(self, name):
        self.name = name
        self.books = [] 

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        return f"{self.name} {self.books}"

def main():
    chambers = Author("Robert W Chambers")
    chambers.publish("The King in Yellow")
    chambers.publish("The Maker of Moons")
    chambers.publish("The Prophets' Paradise")
    print(chambers)

    bierce = Author("Ambrose Bierce")
    print(bierce)

main()
