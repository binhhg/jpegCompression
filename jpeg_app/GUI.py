import tkinter as tk
from tkinter import filedialog
import os
from jpeg_app import logStatus
from . import JPEG_compress


class GUI:
    def __init__(self, root):
        self.root = root
        self.textColor = "#393e46"
        self.buttonColor = "#393e46"
        self.xForBtn = 430
        self.xForEntry = 120
        self.xForLabel = 10
        self.font = "Century Gothic"
        self.quality = 95
        self.fileName = ""
        self.log = tk.Label()

    def setWindow(self):
        self.root.title("Jpeg compress")
        width, height = 550, 360  # 500, 530
        self.root.geometry("%dx%d" % (width, height))

        # Display infor, title
        tk.Label(self.root, text="HUST - SOICT", font=(self.font, 10), fg=self.textColor).place(
            x=210, y=3)
        tk.Label(self.root, text="Multimedia Data Coding", font=(self.font, 10), fg=self.textColor).place(
            x=180, y=23)
        tk.Label(self.root, text="JPEG COMPRESSION", font=(self.font, 16, "bold"), fg=self.textColor).place(x=150, y=48)

    def drawUI(self):

        self.DPCM = None

        # Display open image
        tk.Label(self.root, text="File path", font=(self.font, 12, "bold"), fg=self.textColor).place(x=self.xForLabel,
                                                                                                     y=105)

        dirEntry = tk.Entry(self.root, textvariable="", font=(self.font, 12), width=32)
        dirEntry.pack()
        dirEntry.insert(0, "")
        dirEntry.place(x=self.xForEntry, y=105)

        btnOpenFile = tk.Button(self.root, text="Select File", width=10, height=1, bg=self.buttonColor, fg="#FFFFFF",
                                command=lambda: self.DirFileDialog(dirEntry))
        btnOpenFile.place(x=self.xForEntry+300, y=105)

        tk.Label(self.root, text="JPEG COMPRESSION", font=(self.font, 16, "bold"), fg=self.textColor).place(x=146, y=48)
        tk.Label(self.root, text="#2020", font=(self.font, 8), fg=self.textColor).place(x=460, y=511)

        btnLossy = tk.Button(self.root, text="Encode", width=10, height=2, bg=self.buttonColor, fg="#FFFFFF",
                             command=lambda: self.actionCompress())
        btnLossy.place(x=self.xForEntry, y=200)

        btnDeLossy = tk.Button(self.root, text="Decode", width=10, height=2, bg=self.buttonColor, fg="#FFFFFF",
                               command=lambda: self.actionDecompress(".jpg"))
        btnDeLossy.place(x=self.xForEntry + 105, y=200)

        #Endcode and decode 1 step
        btnProcess = tk.Button(self.root,  text = "Full Process", width = 10, height = 2, bg = self.buttonColor, fg = "#FFFFFF", command=lambda:self.actionProcess(".jpg"))
        btnProcess.place(x = self.xForEntry+210, y = 200)

        tk.Label(self.root, text="Option", font=(self.font, 12, "bold"), fg=self.textColor).place(x=self.xForLabel,
                                                                                                   y=150)

        self.var = tk.IntVar()
        self.var.set(2)
        r1 = tk.Radiobutton(self.root, text="Use DPCM on DC", variable=self.var, value=1, command=lambda:self.sellect(), font=(self.font, 10))
        r1.pack()
        r1.place(x=self.xForEntry, y = 150)

        r2 = tk.Radiobutton(self.root, text="Not use DPCM on DC", variable=self.var, value=2, command=lambda:self.sellect(), font=(self.font, 10))
        r2.pack()
        r2.place(x=self.xForEntry+150, y = 150)

        
                                                                                                  
        # tkScale = tk.Scale(self.root, orient=tk.HORIZONTAL, length=290, width=10, sliderlength=10, from_=1, to=4,
        #                    tickinterval=1, command=self.set_value)
        # tkScale.set(2)
        # tkScale.place(x=120, y=200)
    def sellect(self):
        if (self.var.get()==1):
            self.DPCM = True
        if (self.var.get()==2):
            self.DPCM = False
        # selection = "You selected the option " + str(self.var.get())
        # print(selection)

    def DirFileDialog(self, dirEntry):
        self.fileName = filedialog.askopenfilename(initialdir="/", title="Select Picture",
                                                   filetypes=(("All Files", "*.*"),
                                                              ("JPEG", "*.JPEG;*.JPG;*.JPE"),
                                                              ("Bitmap Image File", "*.BMP"),
                                                              ("PNG", "*.PNG"),
                                                              ("BIN", "*.BIN"),
                                                              ("Numpy array Python", "*.npy")))
        FileCSV = self.fileName
        dirEntry.delete(0, tk.END)
        dirEntry.insert(0, FileCSV)

    # def set_value(self, val):
    #     self.quality = int(val) - 1

    def actionCompress(self):
        # try:
        # print(self.DPCM)
        outputPath, log = JPEG_compress.JPEG().encodeJPEG(self.fileName, 0, self.DPCM)
        self.log.after(0, self.log.destroy)
        self.log = tk.Label(self.root, text=log, font=(self.font, 12), fg=self.textColor)
        self.log.place(x=120, y=250)

    def actionDecompress(self, typeFile):
        filename, fileExtension = os.path.splitext(self.fileName)

        fileToSave = filename + "_decode" + typeFile
        log = JPEG_compress.JPEG().decode(self.fileName, fileToSave, self.DPCM)
        self.log.after(0, self.log.destroy)
        self.log = tk.Label(self.root, text=log, font=(self.font, 12), fg=self.textColor)
        self.log.place(x=100, y=250)
    
    def actionProcess(self, typeFile):        
        inputPath = self.fileName
        compressedPath, log = JPEG_compress.JPEG().encodeJPEG(self.fileName, 0, self.DPCM)

        # self.fileName = compressedPath
        filename, fileExtension = os.path.splitext(compressedPath)
        outputPath = filename + "_decode" + typeFile

        JPEG_compress.JPEG().decode(compressedPath, outputPath, self.DPCM)

        log = logStatus.showMetric(inputPath, compressedPath, outputPath)
        self.log.after(0,self.log.destroy)
        self.log = tk.Label(self.root, text = log, font = (self.font, 12), fg = self.textColor)
        self.log.place(x = 120, y = 250)


if __name__ == "__main__":
    root = tk.Tk()
    h = GUI(root)
    h.setWindow()
    h.drawUI()
    root.mainloop()
