#!/usr/local/anaconda3/bin/python
import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title('Helooo')
    btn = Gtk.Button(label="Hello, World!")
    btn.connect('clicked', lambda x: win.destroy())
    win.add(btn)
    win.show_all()

app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)