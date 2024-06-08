import tkinter as tk
from tkinterweb import HtmlFrame


def open_webpage():
    url = entry.get()
    frame.load_website(url)


app = tk.Tk()
app.title("BROWSER")
app.state('zoomed')

entry = tk.Entry(app, width=50)
entry.pack(pady=10)

open_button = tk.Button(app, text="Open", command=open_webpage)
open_button.pack(pady=5)

frame = HtmlFrame(app)
frame.pack(fill="both", expand=True)

frame.load_website("about:blank")

app.mainloop()
