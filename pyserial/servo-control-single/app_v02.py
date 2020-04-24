# Imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

import time
import serial
import struct
"""
3>> import struct
3>> print(struct.pack('>B', 0))
b'\x00'
3>> print(struct.pack('>B', 255))
b'\xff'
3>> print(struct.pack('>2B', 255, 0))
b'\xff\x00'
3>> print(struct.pack('>H', 9000))
b'#('
"""
class ArduinoSerialComm():

    def __init__(self):
        port = serial.Serial(
                "COM3",
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )

        if self.port.isOpen(): # try to open port, if possible print message and proceed with 'while True:'
            print ("port is opened!")

    def arduino_comm_open(self):
        print("port test opened")
        pass

    def arduino_comm_config(self):
        print("port test confiugured")

    def arduino_comm_close(self):
        """
        if(self.port.isOpen()):
            self.port.close()
        else:
            print("port already closed")
        """
        print("port test closed")
        #pass

    def arduino_comm_getData(self):
        """
        value = self.ser.readline()  # read line (single value) from the serial port
        decoded_bytes = str(value[0:len(value) - 2].decode("utf-8"))
        # print(decoded_bytes)
        valor = decoded_bytes.split(",")
        return valor
        """
        pass

    def arduino_comm_isOpen(self):
        #return self.ser.isOpen()
        pass

    def arduino_comm_get_ports():
        """
        #get a list of all active ports on PC
        self.ports = serial.tools.list_ports.comports()

        #print(portData)
        print("total COM ports = " + str(len(self.ports))) #number of COM ports on computer

        #get name of single port print(portData[0]), print(portData[1])
        return self.ports
        """
        pass

    def arduino_comm_find(portsFound):
        #initialize variables
        """
        commPort='none'
        numConnections = len(portsFound)

        for i in range(0,numConnections):
            port = portsFound[i]
            strPort = str(port)

        if numConnections == 0:
            strPort = ""
        if 'Arduino' in strPort:
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])
            print("Arduino found on " + str(splitPort[0]))
        else:
            print("Arduino not found")
        return commPort
        """
        pass

    def hello_test(self):
        print("hello from SerialComm class")

class Application():

    def __init__(self, parent, *args, **kwargs):
        self.servo_pos = 0

        self.parent = parent
        self.parent.title("Arduino Servo Control GUI")

        # make Esc to exit program
        self.parent.bind('<Escape>', self._quit)

        self._init_gui_menu()
        self._init_gui_config_frame()
        self._init_gui_send_frame()
        self._init_gui_receive_frame()
        self._init_gui_status_frame()

        self.arduino_connect()

    def servo_increment(self):
        pass

    def servo_decrement(self):
        pass

    def servo_update(self):
        self.servo_pos = self.entry.get()
        #print(self.servo_pos)
        #servo_pos_string = "b"+"'"+str(self.servo_pos)+"'"
        print(self.servo_pos.encode())
        self.port.write(self.servo_pos.encode())
        #self.port.write(struct.pack('>B', self.servo_pos))
        #self.port.write(b'20')
        #pass "1".encode()

    def servo_set_to_origin(self):
        self.arduno_serial_comm.hello_test()
        pass

    def _init_gui_config_frame(self):
        # embed frame
        self.config_frame = ttk.LabelFrame(self.parent, text = "Configuration")
        self.config_frame.grid(column=0, row=0, padx=8, pady=4)

        # dropdown menu
        # Dictionary with options
        baud_rate_list = [300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200]

        baud_rate_value = tk.StringVar()
        baud_rate_value.set(baud_rate_list[5]) #set first options to default value

        #myButton = Button(root, text='show selection').pack()

        baud_drop_menu = ttk.OptionMenu(self.config_frame, baud_rate_value,*baud_rate_list) #pointer to optins
        baud_drop_menu.grid(column = 0, row = 0)

    def _init_gui_send_frame(self):
        # embed frame
        self.send_frame = ttk.LabelFrame(self.parent, text = "Send")
        self.send_frame.grid(column=0, row=1, padx=8, pady=4)

        self.btn_inc = ttk.Button(self.send_frame, text="Inc", command = self.servo_increment) # command=self.servo_inc_pos
        self.btn_dec = ttk.Button(self.send_frame, text="Dec", command = self.servo_decrement)
        self.btn_update = ttk.Button(self.send_frame, text="Update", command = self.servo_update)
        self.btn_origin = ttk.Button(self.send_frame, text="Origin", command = self.servo_set_to_origin)

        self.entry = ttk.Entry(self.send_frame)

        self.btn_inc.grid(column = 0, row = 0)
        self.btn_dec.grid(column = 1, row = 0)
        self.entry.grid(column = 2, row = 0)
        self.btn_update.grid(column = 3, row = 0)
        self.btn_origin.grid(column = 4, row = 0)

    def _init_gui_receive_frame(self):
        # embed frame
        self.receive_frame = ttk.LabelFrame(self.parent, text = "Receive")
        self.receive_frame.grid(column=0, row=2, padx=8, pady=4)

        #----scrolled text--------------
        scroll_w = 40
        scroll_h = 5
        text = scrolledtext.ScrolledText(self.receive_frame, width=scroll_w, height=scroll_h, wrap=tk.WORD)

        text.grid(column = 0, row = 0)

    def _init_gui_status_frame(self):
        # embed frame
        self.status_frame = ttk.LabelFrame(self.parent, text = "Status")
        self.status_frame.grid(column=0, row=3, padx=8, pady=4)

        #----scrolled text--------------
        scroll_w = 40
        scroll_h = 2
        status = scrolledtext.ScrolledText(self.status_frame, width=scroll_w, height=scroll_h, wrap=tk.WORD)

        status.grid(column = 0, row = 0)

    def _init_gui_menu(self):
        # creating a menu bar
        menu_bar = Menu(self.parent)
        self.parent.config(menu = menu_bar)

        # create menu and add menu items
        file_menu = Menu(menu_bar, tearoff=0) # remove default dashed line separator
        help_menu = Menu(menu_bar, tearoff = 0)

        # create dropdown menus
        menu_bar.add_cascade(label="File", menu = file_menu)
        menu_bar.add_cascade(label ="Help", menu = help_menu)

        # add commands to file menu
        file_menu.add_command(label = "New")
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = self._quit)

        # add commands to Help menu
        help_menu.add_command(label = "normal_msg") # command=_normal_msgBox

    def _quit(self, *args):
        self.arduino_disconnect()
        time.sleep(1)
        print ("application closing!")
        self.parent.quit()
        self.parent.destroy()
        exit()

    def arduino_connect(self):
        try:
            self.port = serial.Serial(
                "COM3",
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
            self.port.isOpen() # try to open port, if possible print message and proceed with 'while True:'
            print ("port is opened!")

        except IOError: # if port is already opened, close it and open it again and print message
          self.port.close()
          self.port.open()
          print ("port was already open, was closed and opened again!")

    def arduino_disconnect(self):
        self.port.flush()
        self.port.flushInput()
        self.port.flushOutput()
        self.port.close()
        print("Port COM3 is closed")

if __name__ == "__main__":

    # create tkinter instance
    root = tk.Tk()

    app = Application(root)

    # put root window in front of others
    root.attributes("-topmost", True)
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)

    # disable closing application by (x)
    root.protocol("WM_DELETE_WINDOW", lambda: print("cant close") )
    # start main loop
    root.mainloop()