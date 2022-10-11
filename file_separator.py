import os
import shutil
import tkinter
from tkinter import messagebox
from tkinter.ttk import Progressbar


counter=0
def action():
    inp1 = p1.get()
    inp2 = p2.get()
    p3.set("")
    p4.set("")

    try:

        d = {'aif': 'AIF audio file', 'cda': 'CD audio track file', 'mid': ' MIDI audio file',
             'midi': 'MIDI audio file', 'mp3': 'MP3 audio file', 'mpa': 'MPEG-2 audio file',
             'ogg': 'Ogg Vorbis audio file', 'wav': 'WAV file', 'wma': 'WMA audio file',
             'wpl': 'Windows Media Player playlist', '7z': '7-Zip compressed file', 'arj': 'ARJ compressed file',
             'deb': 'Debian software package file', 'pkg': 'Package file', 'rar': 'RAR file',
             'rpm': 'Red Hat Package Manager', 'tar.gz': 'Tarball compressed file', 'z': 'Z compressed file',
             'zip': 'Zip compressed file', 'bin': 'Binary file', 'dmg': 'macOS X disk image', 'iso': 'ISO disc image',
             'toast': 'Toast disc image', 'vcd': 'Virtual CD', 'csv': 'Comma separated value file', 'dat': 'Data file',
             'db': 'Database file', 'dbf': 'Database file', 'log': 'Log file', 'mdb': 'Microsoft Access database file',
             'sav': 'Save file (e.g., game save file)', 'sql': 'SQL database file',
             'tar': 'Linux / Unix tarball file archive', 'xml': 'XML file',
             'email': 'Outlook Express e-mail message file.',
             'eml': 'E-mail message file from multiple e-mail clients, including Gmail.',
             'emlx': 'Apple Mail e-mail file.', 'msg': 'Microsoft Outlook e-mail message file.',
             'oft': 'Microsoft Outlook e-mail template file.', 'ost': 'Microsoft Outlook offline e-mail storage file.',
             'pst': 'Microsoft Outlook e-mail storage file.', 'vcf': 'E-mail contact file.',
             'apk': 'Android package file', 'bat': 'Batch file', 'cgi': 'Perl script file', 'pl': 'Perl script file.',
             'com': 'MS-DOS command file', 'exe': 'Executable file', 'gadget': 'Windows gadget',
             'jar': 'Java Archive file', 'msi': 'Windows installer package', 'py': 'Python file',
             'wsf': 'Windows Script File', 'fnt': 'Windows font file', 'fon': 'Generic font file',
             'otf': 'Open type font file', 'ttf': 'TrueType font file', 'ai': 'Adobe Illustrator file',
             'bmp': 'Bitmap image', 'gif': 'GIF image', 'ico': 'Icon file', 'jpeg': 'JPEG image', 'jpg': 'JPEG image',
             'png': 'PNG image', 'ps': 'PostScript file', 'psd': 'PSD image', 'svg': 'Scalable Vector Graphics file',
             'tif': 'TIFF image', 'tiff': 'TIFF image', 'asp': 'Active Server Page file',
             'aspx': 'Active Server Page file', 'cer': 'Internet security certificate', 'cfm': 'ColdFusion Markup file',
             'css': 'Cascading Style Sheet file', 'htm': 'HTML file', 'html': 'HTML file', 'js': 'JavaScript file',
             'jsp': 'Java Server Page file', 'part': 'Partially downloaded file', 'php': 'PHP file', 'rss': 'RSS file',
             'xhtml': 'XHTML file', 'key': 'Keynote presentation', 'odp': 'OpenOffice Impress presentation file',
             'pps': 'PowerPoint slide show', 'ppt': 'PowerPoint presentation',
             'pptx': 'PowerPoint Open XML presentation', 'c': 'C and C++ source code file', 'class': 'Java class file',
             'cpp': 'C++ source code file', 'cs': 'Visual C# source code file',
             'h': 'C, C++, and Objective-C header file', 'java': 'Java Source code file', 'sh': 'Bash shell script',
             'swift': 'Swift source code file', 'vb': 'Visual Basic file', 'ods': 'OpenOffice Calc spreadsheet file',
             'xls': 'Microsoft Excel file', 'xlsm': 'Microsoft Excel file with macros',
             'xlsx': 'Microsoft Excel Open XML spreadsheet file', 'bak': 'Backup file', 'cab': 'Windows Cabinet file',
             'cfg': 'Configuration file', 'cpl': 'Windows Control panel file', 'cur': 'Windows cursor file',
             'dll': 'DLL file', 'dmp': 'Dump file', 'drv': 'Device driver file', 'icns': 'macOS X icon resource file',
             'ini': 'Initialization file', 'lnk': 'Windows shortcut file', 'sys': 'Windows system file',
             'tmp': 'Temporary file', '3g2': '3GPP2 multimedia file', '3gp': '3GPP multimedia file', 'avi': 'AVI file',
             'flv': 'Adobe Flash file', 'h264': 'H.264 video file', 'm4v': 'Apple MP4 video file',
             'mkv': 'Matroska Multimedia Container', 'mov': 'Apple QuickTime movie file', 'mp4': 'MPEG4 video file',
             'mpg': 'MPEG video file', 'mpeg': 'MPEG video file', 'rm': 'RealMedia file', 'swf': 'Shockwave flash file',
             'vob': 'DVD Video Object', 'wmv': 'Windows Media Video file', 'doc': 'Microsoft Word file',
             'docx': 'Microsoft Word file', 'odt': 'OpenOffice Writer document file', 'pdf': 'PDF file',
             'rtf': 'Rich Text Format', 'tex': 'A LaTeX document file', 'txt': 'Plain text file',
             'wpd': 'WordPerfect document',
              'o' : 'Object file' }
        os.chdir(inp1)
        l = os.listdir()

        total = len(l)

        os.chdir(inp2)

        count = 0
        for i in l:
            global progress
            count = count + 1
            count = (count / total) * 100
            progress['value'] = count
            root.update_idletasks()
            di=str(count)+"%"
            p3.set(di)
            ind = i.rfind(".")
            if ind == -1:
                continue
            ext = i[ind + 1:len(i)]


            if ext in d.keys():
                l2 = os.listdir(inp2)
                if d.get(ext) not in l2:
                    os.mkdir(d.get(ext))
                des1=inp2+"\\"+d.get(ext)
                src1 = inp1 + "\\" + i
                shutil.move(src1,des1 )
                p4.set(l.pop(l.index(i)))



        progress['value'] = 100
        root.update_idletasks()
        p3.set("100%")
        messagebox.showinfo("DONE !!", "  FILES  HAS  BEEN SUCCESSFULLY  MOVED  TO  THEIR  RESPECTIVE FOLDERS  !!")


    except OSError as orr:

        messagebox.showerror("ERROR!!", orr)







root = tkinter.Tk()
root.title("FILE COMBINER")
root.geometry("750x499")
root.wm_maxsize(750, 499)
root.wm_minsize(750, 499)
progress = Progressbar(root, orient=tkinter.HORIZONTAL,
                       length=100, mode='determinate')
p1 = tkinter.StringVar()
p2 = tkinter.StringVar()
p3 = tkinter.StringVar()
p4 = tkinter.StringVar()
per = tkinter.Label(root, textvariable=p3).place(x=210, y=300)
fname = tkinter.Label(root, textvariable=p4, width=100).place(x=10, y=350)

# image=Image.open("photo1.png")
# photo=ImageTk.PhotoImage(image)
src = tkinter.Label(root, text="ENTER SOURCE FOLDER PATH").place(x=50, y=100)
des = tkinter.Label(root, text="ENTER DESTINATION FOLDER PATH").place(x=50, y=150)
src2 = tkinter.Entry(root, width=50, textvariable=p1).place(x=280, y=100)
des2 = tkinter.Entry(root, width=50, textvariable=p2).place(x=280, y=150)
sub = tkinter.Button(root, text="SUBMIT", command=action, bg="pink", width=15, height=2).place(x=300, y=260)
progress.place(x=100, y=300)

# b=tkinter.Button(root,text="h").place(x=100,y=100)
# l= tkinter.Label(image=photo).pack(side=tkinter.RIGHT)


root.mainloop()

