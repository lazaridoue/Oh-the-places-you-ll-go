######################################################################
# Author: Eleni Lazaridou
# Username: lazaridoue
#

# Purpose:  To create a map of locations
#           where the user is originally from or has visited,
#           and to use tuples and lists correctly.
######################################################################
# Acknowledgements:
# T10: Oh, The Places You'll Go!
#
# Original Authors: Dr. Scott Heggen and Dr. Jan Pearce
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import turtle
import tkinter as tk
import tkinter.messagebox


class Place:
    """
Creates the place and assigns the name of the user, the name of the location as well as the location's latitude and longtitude
    """

    def __init__(self,name,location,lat, long, color):
        """
        Initializer method for the Place class.
        :param name: Name of the user string value
        :param location: Name of the location string
        :param lat: Latitude value float value
        :param long: Longtitude value float value
        :param color: Color of the ping String value
        """
        self.color = color
        self.location = location
        self.longtitude = long
        self.latitude = lat
        self.name = name

    def place_pin(self, window, place):
        """
        This function places a pin on the world map.
        :param window: the window object where the pin will be placed
        :param place: a tuple object describing a place to be put on the map
        :return: None
        """
        window.register_shape("star", "star.gif")
        pin = turtle.Turtle()
        pin.penup()
        if len(place) == 5:
            pin.color(self.color)  # Set the pin to user's chosen color
        pin.shape("triangle")  # Sets the pin to a circle shape

        # Logically, the denominator for longitude should be 360; lat should be 180.
        # These values (195 and 120) were determined through testing to account for
        # the extra white space on the edges of the map. You shouldn't change them!
        if len(place) == 5:
            pin.goto((self.longtitude / 195) * window.window_width() / 2, (self.latitude / 120) * window.window_height() / 2)
        pin.stamp()  # Stamps on the location

        text = "Unknown place"
        if len(place) == 5:
            text = "{0}'s place:\n    {1}".format(self.name, self.location)  # Setting up pin label
        pin.write(text, font=("Calibri", 12, "bold"))  # Stamps the text describing the location

    def adding(self, window):
        """
              This function places a pin on the world map.
              :param window: the window object where the pin will be placed
              :param place: a tuple object describing a place to be put on the map
              :return: None
        """
        if self.latitude >= -250 and self.latitude <= -237 and self.longtitude >= 105 and self.longtitude <= 120:
            image = "star.gif"
            window.addshape(image)
            self.winner = tk.messagebox.showinfo("Easter Egg!", "Great! This is Berea")
        else:
            image = "circle"

        pin = turtle.Turtle()
        pin.penup()

        pin.color(self.color)  # Set the pin to user's chosen color
        pin.shape(image)  # Sets the pin to a circle shape

        pin.goto(self.latitude, self.longtitude)
        pin.stamp()  # Stamps on the location


        text = "{0}'s place:\n    {1}".format(self.name, self.location)  # Setting up pin label
        pin.write(text, font=("Arial", 10, "bold"))  # Stamps the text describing the location


    def __str__(self):
        """
        Creates a string which is projected on the console
        :return: str
        """
        str = "Name: {0} \nLocation: {1}\nLatitude: {2}\nLongtitude: {3}\n".format(self.name,self.location,self.latitude, self.longtitude)

        return str
class MyTkinter:
    def __init__(self,x,y, windowtext=""):
        """
        Initializer method for the MyTkinter class.
        :param x: x coordinate of the onclick function float
        :param y: y coordinate of the onclick function float
        :param windowtext: Text on the top of the screen string
        """
        self.root=tk.Tk()
        self.root.minsize(width=250, height=180)  # Sets the window's minimum size
        self.root.maxsize(width=250, height=180)
        self.root.title(windowtext)

        self.TextLabel1 = tk.StringVar()
        self.Label1 = None
        # self.TextLabel1 = "Hello"
        self.Textbox1 = tk.Entry(self.root)

        self.Label2 = None
        self.TextLabel2 = tk.StringVar()
        self.Textbox2 = tk.Entry(self.root)

        self.Label3 = None
        self.TextLabel3 = tk.StringVar()
        self.Textbox3 = tk.Entry(self.root)

        self.SubmitButton=None
        self.x = x
        self.y = y

    def crLabel1(self, text):
        """
        Creating Label 1 and its text
        :param text: String
        :return: None
        """
        self.TextLabel1.set("")        # Sets the Tkinter string variable
        self.Label1 = tk.Label(self.root, text= text)
        self.Label1.pack()                    # pack means add to window

    def crLabel2(self, text):
        """
        Creating Label 2 and its text
        :param text: String
        :return: None
        """
        self.TextLabel2.set("")        # Sets the Tkinter string variable
        self.Label2 = tk.Label(self.root, text=text)
        self.Label2.pack()                    # pack means add to window

    def crLabel3(self, text):
        """
        Creating Label 3 and its text
        :param text: String
        :return: None
        """
        self.TextLabel3.set("")        # Sets the Tkinter string variable
        self.Label3 = tk.Label(self.root, text=text)
        self.Label3.pack()                    # pack means add to window

    def createTextbox1(self):
        """
        Creating Textbox 1
        :return:
        """
        self.Textbox1.pack()

    def createTextbox2(self):
        """
        Creating Textbox 2
        :return:
        """
        self.Textbox2.pack()

    def createTextbox3(self):
        """
        Creating Textbox 3
        :return:
        """
        self.Textbox3.pack()

    def Create_Submit(self, Buttontext=""):
        """
        Creating Submit button on the screen
        :param Buttontext: string value of the text on the button
        :return: None
        """
        self.SubmitButton = tk.Button(self.root, text =Buttontext, command=self.button1_handler)
        self.SubmitButton.pack()

    def button1_handler(self):
        """
        Handler of the Submit Button
        Calls a different class to pin the location.
        :return: None
        """
        global wn, name, location, color

        name = self.Textbox1.get()  # Retrieves the text entered by the user
        location = self.Textbox2.get()
        color = self.Textbox3.get()
        self.root.destroy()
        p1 = Place(name, location, self.x, self.y, color)
        p1.adding(wn)


def parse_file(filename):
    """
    Iterates through the file, and creates the list of places
    :param filename: the name of the file to be opened
    :return: a list representing multiple places
    """

    #####################################################
    # You do not need to modify this function!
    #####################################################

    file_content = open(filename, 'r')           # Opens file for reading

    str_num = file_content.readline()           # The first line of the file, which is the number of entries in the file
    str_num = int(str_num[:-1])                 # The '/n' character needs to be removed

    places_list = []
    for i in range(str_num):
        places_list.append(extract_place(file_content))         # Assembles the list of places

    file_content.close()

    return places_list
def extract_place(file_content):
    """
    This function extracts five lines out of file_content,
    which is a variable holding all of the file content from the calling function. Each extracted line represents,
    in order, the place's name, location, latitude, longitude, and user color. The function returns the five elements
    to the function call as a tuple.
    :param file_content: contents of the file which represents all places
    :return: a tuple representing a single place.
    """
    name = file_content.readline().strip()
    location = file_content.readline().strip()
    latitude = file_content.readline().strip()
    longtitude = file_content.readline().strip()
    user_color = file_content.readline().strip()

    place_tuple = (name, location, float(latitude), float(longtitude), user_color)      # Finish assembling the tuple!
    return place_tuple
def create(x,y):
    """
    When map is getting clicked this function is getting called.
    Creates the tkinter window and places the pin.
    :param x: x coordinate of the onclick function float
    :param y: y coordinate of the onclick function float
    :return: None
    """
    WinTk = MyTkinter(x,y,"Add Point!")
    WinTk.crLabel1("What's your name?")
    WinTk.createTextbox1()
    WinTk.crLabel2("Location:")
    WinTk.createTextbox2()
    WinTk.crLabel3("Color of Pin:")
    WinTk.createTextbox3()
    WinTk.Create_Submit("Submit")
def xt():
    """
    Gets called when button q is pressed. Exits the screen.
    :return: None
    """
    quit()


def main():
    """
    This program is designed to place pins on a world map.
    Each place is represented as a tuple.
    Each tuple is then added to a list.
    The list of tuples is used to populate the map.

    The map firsts receives data form the file named places.txt
    Then places the 5 pins on the screen. User can quit by pressing q.
    User can clic on the screen and add new places.
    :return: None
    """
    global wn
    wn = turtle.Screen()
    wn.setup(width=1100, height=650, startx=0, starty=0)
    wn.bgpic("world-map.gif")
    wn.title("Oh, The Places You'll Go!")

    place_list = parse_file("places.txt")        # Generates place_list from the file
    # Iterates through each item in the place_list list, calling the place_pin() function
    for place in place_list:
        p1 = Place(place[0],place[1],place[2],place[3],place[4])
        p1.place_pin(wn, place)  # Adds ONE place to the map for each loop iteration
        print(p1)
    print("Map created!")

    wn.onclick(create)
    wn.onkey(xt, "q")
    wn.listen()

    wn.mainloop()
if __name__ == "__main__":
    main()