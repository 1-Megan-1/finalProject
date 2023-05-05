import tkinter as tk
from movieDB import MovieDB
class MovieApp:
    def __init__(self, master, searchList=[]):
        self.master = master
        self.searchList = searchList
        self.currentOverview = ""
        #creating instance of Movie Database
        self.movieDB = MovieDB()
        master.title("Movie Lookup - Created By Elliot O'Connor")
        #Rendering the layout of the application on start
        self.createLayout()

    def createLayout(self):
        # Sizing Window better
        self.master.geometry("800x800")
        self.master.configure(bg="#252525")

        # Header layout
        self.headerFrame = tk.Frame(self.master, bg="#252525")
        self.headerFrame.pack(side=tk.TOP, pady=20)

        self.titleLabel = tk.Label(self.headerFrame, text="Movie Lookup", font=("Arial", 24, "bold"), fg='white',
                                   bg="#252525")
        self.titleLabel.pack(side=tk.LEFT, padx=20)

        self.logoLabel = tk.Label(self.headerFrame, text=":]", font=("Arial", 24), fg='#c62828', bg="#252525")
        self.logoLabel.pack(side=tk.LEFT)

        # Search layout
        self.searchFrame = tk.Frame(self.master, bg="#252525")
        self.searchFrame.pack(side=tk.TOP, pady=20)

        self.searchLabel = tk.Label(self.searchFrame, text="Search for a movie:", font=("Arial", 12), fg='white',
                                    bg="#252525")
        self.searchLabel.pack(side=tk.LEFT, padx=20)

        self.searchEntry = tk.Entry(self.searchFrame, width=75, bg='#424242', fg='white')
        self.searchEntry.pack(side=tk.LEFT)

        self.searchButton = tk.Button(self.searchFrame, text="Search", command=self.searchMovies, bg='#c62828',
                                      fg='white')
        self.searchButton.pack(side=tk.LEFT, padx=10)

        # Results Layout
        self.resultsFrame = tk.Frame(self.master, bg="#252525")
        self.resultsFrame.pack(side=tk.TOP, pady=10)

        self.resultsLabel = tk.Label(self.resultsFrame, text="Search results:", font=("Arial", 12), fg='white',
                                     bg="#252525")
        self.resultsLabel.pack(side=tk.LEFT, padx=10)

        self.results_listbox = tk.Listbox(self.resultsFrame, width=90, height=20, bg='#424242', fg='white')
        self.results_listbox.pack(side=tk.LEFT)

        # Sort buttons
        self.sortFrame = tk.Frame(self.master, bg="#252525")
        self.sortFrame.pack(side=tk.TOP, pady=10)

        self.sortLabel = tk.Label(self.sortFrame, text="Sort by:", font=("Arial", 12), fg='white', bg="#252525")
        self.sortLabel.pack(side=tk.LEFT, padx=10)

        self.ratingButton = tk.Button(self.sortFrame, text="Rating", command=self.sortRating, bg='#c62828', fg='white')
        self.ratingButton.pack(side=tk.LEFT)

        self.yearButton = tk.Button(self.sortFrame, text="Release year", command=self.sortYear, bg='#c62828',
                                    fg='white')
        self.yearButton.pack(side=tk.LEFT, padx=10)

        self.titleButton = tk.Button(self.sortFrame, text="Title", command=self.sortTitle, bg='#c62828', fg='white')
        self.titleButton.pack(side=tk.LEFT)

        # Movie details layout
        self.detailFrame = tk.Frame(self.master, bg="#252525")
        self.detailFrame.pack(side=tk.TOP, pady=10)

        self.detailLabel = tk.Label(self.detailFrame, text="Movie details:", font=("Arial", 12), fg='white',
                                    bg="#252525")
        self.detailLabel.pack(side=tk.LEFT, padx=10)

        self.detailText = tk.Text(self.detailFrame, width=75, height=10, bg='#424242', fg='white')
        self.detailText.pack(side=tk.LEFT)

    def searchMovies(self):
        query = self.searchEntry.get()
        results = self.movieDB.searchMovie(query)
        #Save overview to new Variable and delete to display in additional information box instead
        if not results == "No Results":
            self.currentOverview = results["overview"]
            del results["overview"]
            self.detailText.delete(1.0, tk.END)
            self.detailText.insert(tk.END, self.currentOverview)

        self.searchList.append(results)
        self.reloadSearchBox(self.searchList)
    def sortRating(self):
        sortedRate = sorted(self.searchList, key=lambda x: x['vote_average'], reverse=True)
        self.reloadSearchBox(sortedRate)
    def sortYear(self):
        sortedYear = sorted(self.searchList, key=lambda x: x['release_date'], reverse=True)
        self.reloadSearchBox(sortedYear)
    def sortTitle(self):
        sortedTitle = sorted(self.searchList, key=lambda x: x['original_title'])
        self.reloadSearchBox(sortedTitle)
    def reloadSearchBox(self, list):
        self.results_listbox.delete(0, tk.END)
        for x in list:
            if x != "No Results":
                y = "Title:{} |  Release Date:{} |  ID:{} |  Average Rating:{}".format(
                x['original_title'], x['release_date'], x['id'], x['vote_average'])
                self.results_listbox.insert(tk.END, y)
            else:
                self.results_listbox.insert(tk.END, x)

    def run(self):
        self.master.mainloop()
