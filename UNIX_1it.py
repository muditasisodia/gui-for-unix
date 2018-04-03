# All functions have been named according to their shell commands
# Replace every "-" with "_" while naming shell command functions
# Background colours have been added to frames only to give a clear idea of where the frames begin and end
# Discuss o/p frame with Prayag


from tkinter import *
from subprocess import call
import subprocess


class mainWindow:
    def __init__(self, root):

        # making root an instance variable
        self.root = root

        # Creating frames
        headFrame = Frame (root, bg="red")
        createFrame = Frame (root, bg="blue")
        utilityFrame = Frame (root, bg="green")
        funcFrame1 = Frame (root, bg="yellow")
        funcFrame2 = Frame (root, bg="purple")

        # Disaplying frames
        headFrame.grid (row=0, columnspan=3)
        createFrame.grid (row=1, columnspan=3)
        utilityFrame.grid (row=2, column=0)
        funcFrame1.grid (row=2, column=1)
        funcFrame2.grid (row=2, column=2)

        # Contents of headFrame
        proc = subprocess.Popen ('pwd', stdout=subprocess.PIPE)
        output = proc.stdout.read ().strip ()  # This is dummy text, how will we update the pwd? Ask Prayag #UPDATED
        pwd = Label (headFrame, text="Present Working Directory: " + str(output))
        pwd.pack ()

        # Contents of createFrame
        l1 = Label (createFrame, text="Creation and Deletion")
        b1 = Button (createFrame, text="New File", command=lambda: self.create_window (1))
        b2 = Button (createFrame, text="New Directory", command=lambda: self.create_window (2))
        b3 = Button (createFrame, text="Delete File", command=self.rm)
        b4 = Button (createFrame, text="Delete Directory", command=self.rm_r)
        l1.grid (row=0, columnspan=4)
        b1.grid (row=1, column=0)
        b2.grid (row=1, column=1)
        b3.grid (row=1, column=2)
        b4.grid (row=1, column=3)

        # Contents of utilityFrame
        l2 = Label (utilityFrame, text="Utility Functions: ")
        b5 = Button (utilityFrame, text="Username", command=self.whoami)
        b6 = Button (utilityFrame, text="Memory Status", command=self.free)
        b7 = Button (utilityFrame, text="RAM", command=self.free_g)
        b8 = Button (utilityFrame, text="Disk Usage by File System", command=self.df_k)
        b9 = Button (utilityFrame, text="System Information", command=self.uname_a)
        b10 = Button (utilityFrame, text="Time Duration of System Activity", command=self.uptime)
        b11 = Button (utilityFrame, text="Calculator", command=self.gnome)
        l2.grid (row=0)
        b5.grid (row=1)
        b6.grid (row=2)
        b7.grid (row=3)
        b8.grid (row=4)
        b9.grid (row=5)
        b10.grid (row=6)
        b11.grid (row=7)

        # Contents of funcFrame1
        l3 = Label (funcFrame1, text="Functions on Files: ")
        b12 = Button (funcFrame1, text="View Contents", command=self.catfilecontent)
        b13 = Button (funcFrame1, text="List Files", command=self.ls)
        b14 = Button (funcFrame1, text="View First 10 Lines", command=self.head)
        b15 = Button (funcFrame1, text="View Last 10 Lines", command=self.tail)
        b16 = Button (funcFrame1, text="Copy File", command=self.copy)
        b17 = Button (funcFrame1, text="Sort", command=self.sort)
        b18 = Button (funcFrame1, text="Give Word, Line, Character Count", command=self.wc)
        l3.grid (row=0, columnspan=2)
        b12.grid (row=1)
        b13.grid (row=2)
        b14.grid (row=3)
        b15.grid (row=4)
        b16.grid (row=5)
        b17.grid (row=6)
        b18.grid (row=7)

        # Contents of funcFrame2
        b19 = Button (funcFrame2, text="Give Longest Line", command=self.wc_l)
        b20 = Button (funcFrame2, text="Change Permissions", command=self.chmod)
        b21 = Button (funcFrame2, text="No. of Files", command=self.no_of_files)
        b22 = Button (funcFrame2, text="Compare two files", command=self.cmp)
        b23 = Button (funcFrame2, text="Compress File", command=self.gzip)
        b24 = Button (funcFrame2, text="Uncompress Files", command=self.ungzip)
        b25 = Button (funcFrame2, text="Check Current Permissions", command=self.ls_l)
        b26 = Button (funcFrame2, text="Rename", command=self.mv)
        b19.grid (row=0)
        b20.grid (row=1)
        b21.grid (row=2)
        b22.grid (row=3)
        b23.grid (row=4)
        b24.grid (row=5)
        b25.grid (row=6)
        b26.grid (row=7)


    def create_window(self, x):
        # Creating new window
        window = Toplevel (self.root)

        # Creating widgets for new window
        ipFrame = Frame (window)
        opFrame = Frame (window)

        ipFrame.grid (row=0)
        opFrame.grid (row=1)

        closeButton = Button (ipFrame, text="Close", command=window.destroy)
        # find maximum number of inputs from all commands and decide row number
        closeButton.grid (row=2, column=1)

        if (x == 1):
            applyButton = Button (ipFrame, text="Apply", command=self.prayag1)
            applyButton.grid (row=2, column=0)
            self.catcreatefile (window, ipFrame, opFrame, closeButton, applyButton)

        elif (x == 2):
            applyButton = Button (ipFrame, text="Apply", command=self.prayag2)
            applyButton.grid (row=2, column=0)
            self.mkdir (window, ipFrame, opFrame, closeButton, applyButton)

    # Functions for all onclick events where prayag's code should come
    def prayag2(self):
        call(["mkdir",self.mkdir_value.get()])

    def prayag1(self):
        call ([ "touch", self.file_name.get()])
        subprocess.call ("cat /path/to/file_A > file_B", shell=True)

    def catcreatefile(self, window, ipFrame, opFrame, closeButton, applyButton):

        self.file_name=StringVar()
        self.file_detail = StringVar ()
        l1 = Label (ipFrame, text="Enter name of file: ")
        fileName = Entry (ipFrame,textvariable=self.file_name)
        l2 = Label (ipFrame, text="Enter contents: ")
        fileContent = Entry (ipFrame,textvariable=self.file_detail)

        l1.grid (row=0, column=0)
        fileName.grid (row=0, column=1)
        l2.grid (row=1, column=0)
        fileContent.grid (row=1, column=1)

    def mkdir(self, window, ipFrame, opFrame, closeButton, applyButton):

        self.mkdir_value=StringVar()
        l1 = Label (ipFrame, text="Enter directory name: ")
        dirName = Entry (ipFrame,textvariable=self.mkdir_value)
        l1.grid (row=0, column=0)
        dirName.grid (row=0, column=1)

    def rm(self):
        pass

    def rm_r(self):
        pass

    def whoami(self):
        pass

    def free(self):
        pass

    def free_g(self):
        pass

    def df_k(self):
        pass

    def uname_a(self):
        pass

    def uptime(self):
        pass

    def gnome(self):
        pass

    def catfilecontent(self):
        pass

    def ls(self):
        pass

    def head(self):
        pass

    def tail(self):
        pass

    def copy(self):
        pass

    def sort(self):
        pass

    def wc(self):
        pass

    def wc_l(self):
        pass

    def chmod(self):
        pass

    def no_of_files(self):
        pass

    def cmp(self):
        pass

    def gzip(self):
        pass

    def ungzip(self):
        pass

    def ls_l(self):
        pass

    def mv(self):
        pass


root = Tk ()
obj = mainWindow (root)
root.mainloop ()