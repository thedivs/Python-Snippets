import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup

BASE = "https://www.moneycontrol.com/stocks/marketstats/indcomp.php"
GAIN_URL = "https://www.moneycontrol.com/stocks/marketstats/cont_gainers/bse/index.php"
LOSS_URL = "https://www.moneycontrol.com/stocks/marketstats/cont_losers/bse/index.php"

def get_sectors():
    r = requests.get(BASE)
    soup = BeautifulSoup(r.text, "html.parser")
    options = soup.find_all("option")
    return {opt.text.strip(): opt['value'] for opt in options if opt['value']}

def fetch_list(url, code):
    r = requests.get(url, params={'indcode': code})
    soup = BeautifulSoup(r.text, "html.parser")
    rows = soup.find_all("tr")[1:11]
    data = []
    for row in rows:
        cols = [td.text.strip() for td in row.find_all("td")]
        if cols:
            data.append(cols[:4])
    return data

def on_fetch():
    sec = combo.get()
    if not sec:
        messagebox.showwarning("Select Sector", "Please choose a sector.")
        return
    code = sectors[sec]
    gain = fetch_list(GAIN_URL, code)
    loss = fetch_list(LOSS_URL, code)
    
    def populate(tree, data):
        for i in tree.get_children():
            tree.delete(i)
        for row in data:
            tree.insert("", "end", values=row)

    populate(tree_gain, gain)
    populate(tree_loss, loss)

root = tk.Tk()
root.title("Weekly Top 10 – Moneycontrol")

sectors = get_sectors()
tk.Label(root, text="Sector:").grid(row=0, column=0, padx=5, pady=5)
combo = ttk.Combobox(root, values=list(sectors.keys()), width=30)
combo.grid(row=0, column=1, padx=5, pady=5)

ttk.Button(root, text="Fetch Weekly Stats", command=on_fetch).grid(row=0, column=2, padx=5)

cols = ("Company", "Last Price", "Change%", "Volume")
tk.Label(root, text="🔺 Top 10 Gainers").grid(row=1, column=0, columnspan=3)
tree_gain = ttk.Treeview(root, columns=cols, show="headings", height=10)
for c in cols:
    tree_gain.heading(c, text=c)
tree_gain.grid(row=2, column=0, columnspan=3, pady=5)

tk.Label(root, text="🔻 Top 10 Losers").grid(row=3, column=0, columnspan=3)
tree_loss = ttk.Treeview(root, columns=cols, show="headings", height=10)
for c in cols:
    tree_loss.heading(c, text=c)
tree_loss.grid(row=4, column=0, columnspan=3, pady=5)

root.mainloop()
