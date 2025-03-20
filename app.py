import customtkinter as CT

# Initialize customtkinter
cts = CT.CTk()
cts.title("Click Recorder")
cts.geometry("1000x720")

# Create a canvas
canvas = CT.CTkCanvas(cts, width=1000, height=720, bg="#102030")
canvas.pack()