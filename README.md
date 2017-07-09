# Page Turner

A simple python web server which issues a key command to a windows process when the `/turn` route is requested.

An example usage would be for a pianist using a monitor to display music scores. The pianist would run the server on the machine displaying the scores, and connect from their smartphone (on the same network) to `http://[IP address of machine]`. Whenever they touch the screen, the page will turn on the PDF reader.

## Usage

1. Install `python`, `pywinauto`.
2. Configure `server.py`
    * `PORT` is the port the server runs on
    * `EXE_PATH` is the path to your PDF reader
    * `KEYSTROKE` is the [pywinauto keycode](http://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html) to issue to the PDF reader
3. Run `python server.py`
4. Navigate to `http://[SERVER_IP]:PORT` from a different device on the network.
5. Touch/click 'Turn page' to turn the page.

## Notes

A total of 15 minutes was spent creating this bare-bones server/page. It currently only runs on Windows, and has only been tested with SumatraPDF. Your mileage may vary.

Feel free to let me know if it was useful, or if you'd like more functionality.
