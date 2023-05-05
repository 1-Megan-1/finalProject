import tkinter
from movie import MovieApp

def main():
    root = tkinter.Tk()
    app = MovieApp(root)
    app.run()

if __name__ == '__main__':
    main()