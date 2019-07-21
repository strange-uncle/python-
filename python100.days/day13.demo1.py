import time
import tkinter
import tkinter.messagebox
from threading import Thread


def download():
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成')
    

def show_about():
    tkinter.messagebox.showinfo('关于', 'this is a demo')
    

def main():
    top = tkinter.Tk()
    top.title('single threading')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)
    
    panel = tkinter.Frame(top)
    
    btn_download = tkinter.Button(panel, text='download', command=download)
    btn_download.pack(side='left')
    
    btn_about = tkinter.Button(panel, text='about', command=show_about)
    btn_about.pack(side='right')
    
    panel.pack(side='bottom')
    
    tkinter.mainloop()
    

def multi_threading_main():
    class DownloadTaskHandler(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('download', ' download completed')
            btn_download.config(state=tkinter.NORMAL)
    
    def download2():
        btn_download.config(state=tkinter.DISABLED)
        DownloadTaskHandler(daemon=True).start()
    
    def show_about2():
        tkinter.messagebox.showinfo('about', 'this is multi-threading about')
    
    top = tkinter.Tk()
    top.title('use another threading to download')
    top.geometry('200x250')
    top.wm_attributes('-topmost', True)
    
    panel = tkinter.Frame(top)
    btn_download = tkinter.Button(panel, text='download', command=download2)
    btn_download.pack(side='left')
    
    btn_about = tkinter.Button(panel, text='show about', command=show_about2)
    btn_about.pack(side='right')
    
    panel.pack(side='bottom')
    
    tkinter.mainloop()


if __name__ == '__main__':
    # main()
    multi_threading_main()
