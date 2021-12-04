import sdl2.ext

def create_window():
    sdl2.ext.init()

    window = sdl2.ext.Window("Hello World!", size=(1280, 720))
    window.show()

    processor = sdl2.ext.TestEventProcessor()
    processor.run(window)
