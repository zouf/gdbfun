#!/home/zouf/archer/install/bin/gdb -P
import gdb, threading, Queue, gtk, glib, os, pynotify

(read_pipe, write_pipe) = os.pipe()

event_queue = Queue.Queue()

def send_to_gtk(func):
    event_queue.put(func)
    os.write(write_pipe, 'x')

def on_stop_event(event):
    n = pynotify.Notification('Your program stopped in gdb')
    n.show()

class GtkThread(threading.Thread):
    def handle_queue(self, source, condition):
        global event_queue
        os.read(source, 1)
        func = event_queue.get()
        func()

    def run(self):
        global read_pipe
        glib.io_add_watch(read_pipe, glib.IO_IN, self.handle_queue)
        gtk.main()

gdb.events.stop.connect(on_stop_event)

gtk.gdk.threads_init()

pynotify.init('gdb')

t = GtkThread()
t.setDaemon(True)
t.start()
