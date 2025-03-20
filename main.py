import customtkinter as CT
from lines import beziercurve
from app import cts, canvas

def on_click(event):
    """Records and displays the coordinates where the user clicks."""
    coords = f"Clicked at: ({event.x}, {event.y})"
    print(coords)
    coordinates.append((event.x, event.y))  # Store coordinates
    label.configure(text=coords)  # Update label
    canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill="white")  # Display the click

def display_bezier_curve(event):
    """Displays the bezier curve using the recorded coordinates."""
    if len(coordinates) < 2:
        label.configure(text="Please record at least 2 coordinates to display the Bezier Curve")
        return

    # Display the bezier curve
    nextpoint = beziercurve(coordinates, 0)
    canvas.create_line(coordinates[0], nextpoint, fill="black", width=2)
    for t in range(1, 101):
        previouspoint = nextpoint
        nextpoint = beziercurve(coordinates, t)
        canvas.create_line(previouspoint, nextpoint, fill="black", width=2)

        if t == 100:
            canvas.create_oval(coordinates[-1][0] - 5, coordinates[-1][1] - 5, coordinates[-1][0] + 5, coordinates[-1][1] + 5, fill="red")  # Display the last point
            canvas.create_oval(coordinates[0][0] - 5, coordinates[0][1] - 5, coordinates[0][0] + 5, coordinates[0][1] + 5, fill="red")  # Display the first point

    # Clear the recorded coordinates
    coordinates.clear()

if __name__ == "__main__":
    coordinates = []  # List to store click coordinates

    # Label to display coordinates
    label = CT.CTkLabel(cts, text="Click anywhere to record coordinates", font=("Arial", 16))
    label.pack(pady=20)

    # Bind left mouse button click to on_click function
    cts.bind("<s>", on_click)
    cts.bind("<d>", display_bezier_curve)
    cts.mainloop()