import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")

    def kuva_sisestus():
        # Sisestused
        laenusumma = int(sisestus1.get())
        kuuintressimäär = float(sisestus2.get())/12/100
        maksete_arv = int(sisestus3.get())*12

        igakuine_makse = laenusumma * kuuintressimäär / (1 - (1 + kuuintressimäär) ** -maksete_arv)
        # print(igakuine_makse)

        vastus = tk.Label(aken, text=f"Igakuine makse: {maksete_arv:.2f}")
        vastus.pack

    #Esimene sisestusväli
    label = tk.Label(aken, text="Laenusumma (€)",).pack(pady=(10, 0))
    sisestus1 = tk.Entry(aken)
    sisestus1.pack()

    #Teine sisestusväli
    label = tk.Label(aken, text="Aastane Intressimäär (%)",).pack(pady=(10, 0))
    sisestus2 = tk.Entry(aken)
    sisestus2.pack()

    #Kolmas sisestusväli
    label = tk.Label(aken, text="Laenu periood (aastates)",).pack(pady=(10, 0))
    sisestus3 = tk.Entry(aken)
    sisestus3.pack()

    #Nupp
    nupp = tk.Button(aken, text="Arvuta", command=kuva_sisestus)
    nupp.pack()

    aken.mainloop()

    if __name__ == "__main__":
        main()