import pypub

#my_first_epub = pypub.Epub('My First Epub')
# my_first_chapter = pypub.create_chapter_from_url('https://en.wikipedia.org/wiki/EPUB')
# my_first_epub.add_chapter(my_first_chapter)
# my_first_epub.create('./my-first-epub.epub')

def main():
    f = open("text.txt", "r", encoding="utf8")
    content = f.read()
    my_first_epub = pypub.Epub('First epub from text')
    my_first_chapter = pypub.create_chapter_from_text(content)
    my_first_epub.add_chapter(my_first_chapter)
    my_first_epub.create("./fromtxt.epub")
if __name__ == "__main__":
    main() 
