# All functions have been named according to their shell commands
# Replace every "-" with "_" while naming shell command functions
# Background colours have been added to frames only to give a clear idea of where the frames begin and end
# Discuss o/p frame with Prayag


from tkinter import *
from subprocess import call
import subprocess
import os


class mainWindow:
    def __init__(self, root):

        # making root an instance variable
        self.root = root

        # Creating frames
        headFrame = Frame(root, bg="red")
        createFrame = Frame(root, bg="blue")
        utilityFrame = Frame(root, bg="green")
        funcFrame1 = Frame(root, bg="yellow")
        funcFrame2 = Frame(root, bg="purple")
        outputFrame = Frame(root, bg="black")

        # Disaplying frames
        headFrame.grid(row=0, columnspan=3)
        createFrame.grid(row=1, columnspan=3)
        utilityFrame.grid(row=2, column=0)
        funcFrame1.grid(row=2, column=1)
        funcFrame2.grid(row=2, column=2)
        outputFrame.grid(rowspan=5, columnspan=3)

        # Contents of headFrame
        self.pwd1 = StringVar()
        proc = subprocess.Popen('pwd', stdout=subprocess.PIPE)
        output = proc.stdout.read().strip()
        dire = output
        self.pwd = Label(headFrame, text="Present Working Directory: " + str(dire), textvariable=self.pwd1)
        self.pwd.grid(row=0, column=0)

        cd = Label(headFrame, text="Change Directory to: ")
        self.changeDirectory = StringVar()
        directoryName = Entry(headFrame, textvariable=self.changeDirectory)
        cdButton = Button(headFrame, text="ENTER", command=self.prayagChangeDirectory)

        cd.grid(row=1, column=0)
        directoryName.grid(row=1, column=1)
        cdButton.grid(row=1, column=3)

        # Contents of Output frame
        op = "output"  # dummy
        output = Label(outputFrame, text="Output: " + op)
        output.pack()
        # Contents of createFrame
        clearButton = Button(outputFrame, text="Clear", command=self.prayagClear())
        clearButton.pack()

        l1 = Label(createFrame, text="Creation and Deletion")
        b1 = Button(createFrame, text="New File", command=lambda: self.create_window(1))
        b2 = Button(createFrame, text="New Directory", command=lambda: self.create_window(2))
        b3 = Button(createFrame, text="Delete File", command=lambda: self.create_window(3))
        b4 = Button(createFrame, text="Delete Directory", command=lambda: self.create_window(4))
        l1.grid(row=0, columnspan=4)
        b1.grid(row=1, column=0)
        b2.grid(row=1, column=1)
        b3.grid(row=1, column=2)
        b4.grid(row=1, column=3)

        # Contents of utilityFrame
        l2 = Label(utilityFrame, text="Utility Functions: ")
        b5 = Button(utilityFrame, text="Username", command=lambda: self.whoami(outputFrame))
        b6 = Button(utilityFrame, text="Memory Status", command=lambda: self.free(outputFrame))
        b7 = Button(utilityFrame, text="RAM", command=lambda: self.free_g(outputFrame))
        b8 = Button(utilityFrame, text="Disk Usage by File System", command=lambda: self.df_k(outputFrame))
        b9 = Button(utilityFrame, text="System Information", command=lambda: self.uname_a(outputFrame))
        b10 = Button(utilityFrame, text="Time Duration of System Activity", command=lambda: self.uptime(outputFrame))
        b11 = Button(utilityFrame, text="Calculator", command=lambda: self.gnome(outputFrame))
        l2.grid(row=0)
        b5.grid(row=1)
        b6.grid(row=2)
        b7.grid(row=3)
        b8.grid(row=4)
        b9.grid(row=5)
        b10.grid(row=6)
        b11.grid(row=7)

        # Contents of funcFrame1
        l3 = Label(funcFrame1, text="Functions on Files: ")
        b12 = Button(funcFrame1, text="View Contents", command=lambda: self.create_window(12))
        b13 = Button(funcFrame1, text="List Files", command=lambda: self.ls(outputFrame))
        b14 = Button(funcFrame1, text="View First 10 Lines", command=lambda: self.create_window(14))
        b15 = Button(funcFrame1, text="View Last 10 Lines", command=lambda: self.create_window(15))
        b16 = Button(funcFrame1, text="Copy File", command=lambda: self.create_window(16))
        b17 = Button(funcFrame1, text="Sort", command=lambda: self.create_window(17))
        b18 = Button(funcFrame1, text="Give Word, Line, Character Count", command=lambda: self.create_window(18))
        l3.grid(row=0, columnspan=2)
        b12.grid(row=1)
        b13.grid(row=2)
        b14.grid(row=3)
        b15.grid(row=4)
        b16.grid(row=5)
        b17.grid(row=6)
        b18.grid(row=7)

        # Contents of funcFrame2
        b19 = Button(funcFrame2, text="Give Longest Line", command=lambda: self.create_window(19))
        b20 = Button(funcFrame2, text="Change Permissions", command=lambda: self.create_window(20))
        b21 = Button(funcFrame2, text="No. of Files", command=lambda: self.create_window(21))
        b22 = Button(funcFrame2, text="Compare two files", command=lambda: self.create_window(22))
        b23 = Button(funcFrame2, text="Compress File", command=lambda: self.create_window(23))
        b24 = Button(funcFrame2, text="Uncompress Files", command=lambda: self.create_window(24))
        b25 = Button(funcFrame2, text="Check Current Permissions", command=lambda: self.create_window(25))
        b26 = Button(funcFrame2, text="Rename", command=lambda: self.create_window(26))
        b19.grid(row=0)
        b20.grid(row=1)
        b21.grid(row=2)
        b22.grid(row=3)
        b23.grid(row=4)
        b24.grid(row=5)
        b25.grid(row=6)
        b26.grid(row=7)

    def create_window(self, x):
        # Creating new window
        window = Toplevel(self.root)

        # Creating widgets for new window
        ipFrame = Frame(window)
        ipFrame.grid(row=0)
        closeButton = Button(ipFrame, text="Close", command=window.destroy)
        # find maximum number of inputs from all commands and decide row number
        closeButton.grid(row=2, column=1)

        if (x == 1):  # createfile
            applyButton = Button(ipFrame, text="Create", command=self.prayagCreateFile)
            applyButton.grid(row=2, column=0)
            self.catcreatefile(window, ipFrame, closeButton, applyButton)

        if (x == 2):  # mkdir
            applyButton = Button(ipFrame, text="Apply", command=self.prayagMkdir)
            applyButton.grid(row=2, column=0)
            self.mkdir(window, ipFrame, closeButton, applyButton)

        if (x == 3):  # rm
            applyButton = Button(ipFrame, text="Delete", command=self.prayagRm)
            applyButton.grid(row=2, column=0)
            self.rm(window, ipFrame, closeButton, applyButton)

        if (x == 4):  # rmr
            applyButton = Button(ipFrame, text="Delete", command=self.prayagRmr)
            applyButton.grid(row=2, column=0)
            self.rm_r(window, ipFrame, closeButton, applyButton)

        if (x == 12):  # View catfilecontent
            applyButton = Button(ipFrame, text="View Content", command=lambda: self.prayagFileContent(ipFrame))
            applyButton.grid(row=2, column=0)
            self.catfilecontent(window, ipFrame, closeButton, applyButton)

        if (x == 14):  # head i.e. first 10 lines
            applyButton = Button(ipFrame, text="View lines", command=lambda: self.prayagFirstTen(ipFrame))
            applyButton.grid(row=2, column=0)
            self.head(window, ipFrame, closeButton, applyButton)

        if (x == 15):  # tail i.e. last 10 lines
            applyButton = Button(ipFrame, text="View lines", command=lambda: self.prayagLastTen(ipFrame))
            applyButton.grid(row=2, column=0)
            self.tail(window, ipFrame, closeButton, applyButton)

        if (x == 16):  # copy
            applyButton = Button(ipFrame, text="Copy", command=lambda: self.prayagCopy(ipFrame))
            applyButton.grid(row=2, column=0)
            self.copy(window, ipFrame, closeButton, applyButton)

        if (x == 17):  # sort in ascending order
            applyButton = Button(ipFrame, text="Sort", command=lambda: self.prayagSortAsce(ipFrame))
            applyButton.grid(row=2, column=0)
            self.sort(window, ipFrame, closeButton, applyButton)

        if (x == 18):  # wc
            applyButton = Button(ipFrame, text="View Count", command=lambda: self.prayagWc(ipFrame))
            applyButton.grid(row=2, column=0)
            self.wc(window, ipFrame, closeButton, applyButton)

        if (x == 19):  # longest line
            applyButton = Button(ipFrame, text="View Longest Line", command=lambda: self.prayagLongest(ipFrame))
            applyButton.grid(row=2, column=0)
            self.wc_l(window, ipFrame, closeButton, applyButton)

        if (x == 20):  # change permissions
            applyButton = Button(ipFrame, text="Change Permissions", command=lambda: self.prayagChange(ipFrame))
            applyButton.grid(row=2, column=0)
            self.chmod(window, ipFrame, closeButton, applyButton)

        if (x == 21):  # no. of files in directory
            applyButton = Button(ipFrame, text="View No. of Files", command=lambda: self.prayagNoOfFiles(ipFrame))
            applyButton.grid(row=2, column=0)
            self.no_of_files(window, ipFrame, closeButton, applyButton)

        if (x == 22):  # compare two files
            applyButton = Button(ipFrame, text="View Result", command=lambda: self.prayagCompare(ipFrame))
            applyButton.grid(row=2, column=0)
            self.cmp(window, ipFrame, closeButton, applyButton)

        if (x == 23):  # compress file
            applyButton = Button(ipFrame, text="Compress", command=lambda: self.prayagCompress(ipFrame))
            applyButton.grid(row=2, column=0)
            self.gzip(window, ipFrame, closeButton, applyButton)

        if (x == 24):  # uncompress file
            applyButton = Button(ipFrame, text="Uncompress", command=lambda: self.prayagUncompress(ipFrame))
            applyButton.grid(row=2, column=0)
            self.ungzip(window, ipFrame, closeButton, applyButton)

        if (x == 25):  # check current permission status of files
            applyButton = Button(ipFrame, text="Get Status", command=lambda: self.prayagCurrentPermission(ipFrame))
            applyButton.grid(row=2, column=0)
            self.ls_l(window, ipFrame, closeButton, applyButton)

        if (x == 26):  # rename file
            applyButton = Button(ipFrame, text="Rename", command=lambda: self.prayagRename(ipFrame))
            applyButton.grid(row=2, column=0)
            self.mv(window, ipFrame, closeButton, applyButton)

    # Dummy function for all onclick events where prayag's code should come

    def prayagChangeDirectory(self):
        os.chdir(self.changeDirectory.get())
        self.pwd1.set("The Present Working Directory is: " + self.changeDirectory.get())

    def prayagCreateFile(self):
        call(["touch", self.createFile.get()])

    def prayagMkdir(self):
        call(["mkdir", self.makeDirectory.get()])

    def prayagRm(self):
        call(["rm", self.removeFile.get()])

    def prayagRmr(self):
        call(["rm", "-r", self.removeDirectory.get()])

    def prayagClear(self):

        pass

    def prayagFileContent(self, ipFrame):
        call ([ "open", self.catfile.get()])
        l1 = Label(ipFrame, text="Opened")
        l1.grid(row=5)

    def prayagFirstTen(self, ipFrame):
        proc="head -10 "+self.first.get()
        free = subprocess.Popen (proc, stdout=subprocess.PIPE, shell=True)
        details = free.stdout.read ().strip ()
        l1 = Label(ipFrame, text=details)
        l1.grid(row=5)

    def prayagLastTen(self, ipFrame):
        proc="tail -10 "+self.last.get()
        free = subprocess.Popen (proc, stdout=subprocess.PIPE, shell=True)
        details = free.stdout.read ().strip ()
        l1 = Label(ipFrame, text=details)
        l1.grid(row=5)

    def prayagCopy(self, ipFrame):
        call ("cat "+self.oneFile.get()+" >> "+self.twoFile.get(), shell=True)
        l1 = Label(ipFrame, text="Content Copied")
        l1.grid(row=5)

    def prayagSortAsce(self, ipFrame):
        call ([ "sort", self.sortFile.get()])
        l1 = Label(ipFrame, text="Sorted")
        l1.grid(row=5)

    def prayagWc(self, ipFrame):
        proc="wc "+self.wordCount.get()
        free = subprocess.Popen (proc, stdout=subprocess.PIPE, shell=True)
        details = free.stdout.read ().strip ()
        l1 =Text(ipFrame,height=10,width=50)
        l1.insert(END, details)
        l1.grid(row=5)

    def prayagLongest(self, ipFrame):
        proc="wc -l "+self.wordCountLongest.get()
        free = subprocess.Popen (proc, stdout=subprocess.PIPE, shell=True)
        details = free.stdout.read ().strip ()
        l1 =Text(ipFrame,height=10,width=50)
        l1.insert(END, details)
        l1.grid(row=5)

    def prayagChange(self, ipFrame):
        call("chmod "+self.user.get()+self.group.get()+self.others.get()+" "+self.fileChmod.get(), shell=True)
        l1 = Label(ipFrame, text="Changed Permissions Successfully.")
        l1.grid(row=5)

    def prayagNoOfFiles(self, ipFrame):
        l1 = Label(ipFrame, text="Count: ")
        l1.grid(row=5)

    def prayagCompare(self, ipFrame):
        proc="cmp "+self.fileOne.get()+" "+self.fileTwo.get()
        free = subprocess.Popen (proc, stdout=subprocess.PIPE, shell=True)
        details = free.stdout.read ().strip ()
        l1 = Label(ipFrame, text="Result:  "+str(details))
        l1.grid(row=5)

    def prayagCompress(self, ipFrame):
        call("gzip "+self.compressFile.get(), shell=True)
        l1 = Label(ipFrame, text="File Compressed. ")
        l1.grid(row=5)

    def prayagUncompress(self, ipFrame):
        call ("gzip -d " + self.uncompressFile.get (), shell=True)
        l1 = Label(ipFrame, text="File Uncompressed. ")
        l1.grid(row=5)

    def prayagCurrentPermission(self, ipFrame):
        proc="ls -l "+self.currentFile.get()
        free = subprocess.Popen (proc, stdout=subprocess.PIPE, shell=True)
        details = free.stdout.read ().strip ()
        l1 = Label(ipFrame, text="Permissions: "+str(details))
        l1.grid(row=5)

    def prayagRename(self, ipFrame):
        call("mv "+self.oldFile.get()+" "+self.newFile.get(),shell=True)
        l1 = Label(ipFrame, text="File Renamed. ")
        l1.grid(row=5)

    def catcreatefile(self, window, ipFrame, closeButton, applyButton):
        self.createFile = StringVar()
        l1 = Label(ipFrame, text="Enter name of file: ")
        fileName = Entry(ipFrame, textvariable=self.createFile)

        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)

    def mkdir(self, window, ipFrame, closeButton, applyButton):
        self.makeDirectory = StringVar()
        l1 = Label(ipFrame, text="Enter directory name: ")
        dirName = Entry(ipFrame, textvariable=self.makeDirectory)

        l1.grid(row=0, column=0)
        dirName.grid(row=0, column=1)

    def rm(self, window, ipFrame, closeButton, applyButton):
        self.removeFile = StringVar()
        l1 = Label(ipFrame, text="Enter file name: ")
        fileName = Entry(ipFrame, textvariable=self.removeFile)

        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)

    def rm_r(self, window, ipFrame, closeButton, applyButton):
        self.removeDirectory = StringVar()
        l1 = Label(ipFrame, text="Enter directory name: ")
        dirName = Entry(ipFrame, textvariable=self.removeDirectory)

        l1.grid(row=0, column=0)
        dirName.grid(row=0, column=1)

    def whoami(self, outputFrame):
        whoAmI = subprocess.Popen('whoami', stdout=subprocess.PIPE)
        username = whoAmI.stdout.read().strip()
        l1 = Label(outputFrame, text="Username: " + str(username))
        l1.pack()

    def free(self, outputFrame):  # memory deets in bytes
        free = subprocess.Popen('free', stdout=subprocess.PIPE)
        details = free.stdout.read().strip()
        l1 = Text(outputFrame, height=10, width=100)
        l1.insert(END, details)
        l1.pack()

    def free_g(self, outputFrame):  # memory deets in GB
        proc = "free -g"
        free = subprocess.Popen(proc, stdout=subprocess.PIPE)
        details = free.stdout.read().strip()
        l1 = Text(outputFrame, height=10, width=100)
        l1.insert(END, details)
        l1.pack()

    def df_k(self, outputFrame):  # disk usage by file system
        proc = "df -k"
        free = subprocess.Popen(proc, stdout=subprocess.PIPE, shell=True)
        usage = free.stdout.read().strip()
        l1 = Text(outputFrame, height=10, width=100)
        l1.insert(END, usage)
        l1.pack()

    def uname_a(self, outputFrame):  # system information
        proc = "uname -a"
        free = subprocess.Popen(proc, stdout=subprocess.PIPE, shell=True)
        information = free.stdout.read().strip()
        l1 = Label(outputFrame, text="System Information: " + str(information))
        l1.pack()

    def uptime(self, outputFrame):  # runtime information
        free = subprocess.Popen('uptime', stdout=subprocess.PIPE)
        runningTime = free.stdout.read().strip()
        l1 = Label(outputFrame, text="System Activity Time Duration: " + str(runningTime))
        l1.pack()

    # def gnome(self,outputFrame): #calculator
    #     l1 = Label(outputFrame, text="Calculator Opened")
    #     l1.pack()

    def catfilecontent(self, window, ipFrame, closeButton, applyButton):
        self.catfile=StringVar()
        l1 = Label(ipFrame, text="Enter file name: ")
        fileName = Entry(ipFrame,textvariable=self.catfile)

        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)

    def ls(self, outputFrame):  # ls for pwd
        Ls = subprocess.Popen('ls', stdout=subprocess.PIPE)
        list = Ls.stdout.read().strip()
        l1 = Text(outputFrame, height=10, width=100)
        l1.insert(END, list)
        l1.pack()

    def head(self, window, ipFrame, closeButton, applyButton):
        self.first = StringVar ()
        l1 = Label(ipFrame, text="Enter file name: ")
        fileName = Entry(ipFrame,textvariable=self.first)

        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)

    def tail(self, window, ipFrame, closeButton, applyButton):
        self.last= StringVar ()
        l1 = Label(ipFrame, text="Enter file name: ")
        fileName = Entry(ipFrame,textvariable=self.last)

        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)

    def copy(self, window, ipFrame, closeButton, applyButton):
        self.oneFile=StringVar()
        self.twoFile = StringVar ()
        l1 = Label(ipFrame, text="Copy from (file name): ")
        fileName = Entry(ipFrame,textvariable=self.oneFile)

        l2 = Label(ipFrame, text="Copy to (file name): ")
        fileName2 = Entry(ipFrame,textvariable=self.twoFile)

        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)
        l2.grid(row=1, column=0)
        fileName2.grid(row=1, column=1)

    def sort(self, window, ipFrame, closeButton, applyButton):
        self.sortFile=StringVar()
        l1 = Label(ipFrame, text="Enter File Name:  ")
        fileName = Entry(ipFrame,textvariable=self.sortFile)
        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)

    def wc(self, window, ipFrame, closeButton, applyButton):
        self.wordCount = StringVar ()
        l1 = Label(ipFrame, text="Enter File Name:  ")
        fileName = Entry(ipFrame,textvariable=self.wordCount)
        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)

    def wc_l(self, window, ipFrame, closeButton, applyButton):
        self.wordCountLongest = StringVar ()
        l1 = Label(ipFrame, text="Enter File Name:  ")
        fileName = Entry(ipFrame,textvariable=self.wordCountLongest)
        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)

    def chmod(self, window, ipFrame, closeButton, applyButton):

        self.fileChmod=StringVar()
        l1 = Label(ipFrame, text="Enter File Name:  ")
        fileName = Entry(ipFrame,textvariable=self.fileChmod)

        self.user=StringVar()
        self.group = StringVar ()
        self.others = StringVar ()


        l2 = Label(ipFrame, text="USER: ")
        user = Entry(ipFrame,textvariable=self.user)
        l3 = Label(ipFrame, text="GROUP: ")
        group = Entry(ipFrame,textvariable=self.group)
        l4 = Label(ipFrame, text="OTHERS: ")
        others = Entry(ipFrame,textvariable=self.others)

        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)
        l2.grid(row=1, column=0)
        user.grid(row=1, column=1)
        l3.grid(row=1, column=2)
        group.grid(row=1, column=3)
        l4.grid(row=1, column=4)
        others.grid(row=1, column=5)

    def no_of_files(self, window, ipFrame, closeButton, applyButton):
        l1 = Label(ipFrame, text="Enter directory name: ")
        dirName = Entry(ipFrame)

        l1.grid(row=0, column=0)
        dirName.grid(row=0, column=1)

    def cmp(self, window, ipFrame, closeButton, applyButton):
        self.fileOne=StringVar()
        self.fileTwo = StringVar ()
        l1 = Label(ipFrame, text="Compare (file name): ")
        fileName = Entry(ipFrame,textvariable=self.fileOne)

        l2 = Label(ipFrame, text="with (file name): ")
        fileName2 = Entry(ipFrame,textvariable=self.fileTwo)

        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)
        l2.grid(row=1, column=0)
        fileName2.grid(row=1, column=1)

    def gzip(self, window, ipFrame, closeButton, applyButton):
        self.compressFile=StringVar()
        l1 = Label(ipFrame, text="Enter file name: ")
        fileName = Entry(ipFrame,textvariable=self.compressFile)

        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)

    def ungzip(self, window, ipFrame, closeButton, applyButton):
        self.uncompressFile = StringVar ()
        l1 = Label(ipFrame, text="Enter file name: ",textvariable=self.uncompressFile)
        fileName = Entry(ipFrame)

        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)

    def ls_l(self, window, ipFrame, closeButton, applyButton):
        self.currentFile=StringVar()
        l1 = Label(ipFrame, text="Enter file name: ")
        fileName = Entry(ipFrame,textvariable=self.currentFile)

        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)

    def mv(self, window, ipFrame, closeButton, applyButton):
        self.oldFile=StringVar()
        self.newFile=StringVar()
        l1 = Label(ipFrame, text="Change (file name): ")
        fileName = Entry(ipFrame,textvariable=self.oldFile)

        l2 = Label(ipFrame, text="to ( new file name): ")
        fileName2 = Entry(ipFrame,textvariable=self.newFile)

        l1.grid(row=0, column=0)
        fileName.grid(row=0, column=1)
        l2.grid(row=1, column=0)
        fileName2.grid(row=1, column=1)


root = Tk()
obj = mainWindow(root),
root.mainloop()

