import tkinter as tk
from tkinter import filedialog
from PIL import Image
import requests


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")

        # Create a canvas widget
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Track last cursor position
        self.last_x, self.last_y = None, None

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

        # Label at the bottom right corner
        self.label = tk.Label(self.root, text="Draw something!", bg="lightgrey")
        self.label.pack(side=tk.BOTTOM, anchor=tk.E)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        clear_btn = tk.Button(btn_frame, text="Clear", command=self.clear_canvas)
        clear_btn.pack(side=tk.LEFT, padx=5)

        save_btn = tk.Button(btn_frame, text="Save", command=self.save_canvas)
        save_btn.pack(side=tk.LEFT, padx=5)

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(
                self.last_x,
                self.last_y,
                event.x,
                event.y,
                fill="black",
                width=3,
                capstyle=tk.ROUND,
                smooth=True,
            )
        self.last_x, self.last_y = event.x, event.y

    def stop_draw(self, event):
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        # Ask user for file location
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        )
        if not file_path:
            return

        # Save canvas to PostScript
        ps_file = file_path.replace(".png", ".ps")
        self.canvas.postscript(file=ps_file)

        # Convert PostScript to PNG
        img = Image.open(ps_file)
        img.save(file_path, "png")
        # post to server
        with open(file_path, "rb") as img_file:
            response = requests.post(
                "http://localhost:8000/annotate", files={"file": img_file}
            )
            if response.status_code == 200:
                annotation = response.json().get("annotation", "")
                self.label.config(text=f"Annotation: {annotation}")
        print(f"Canvas saved as {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
