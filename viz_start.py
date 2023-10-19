import tkinter as tk
import matplotlib.pyplot as plt
import seaborn as sns
from celebrity_heights import famous_peeps_heights, custom_colors  # Import data

# Function to generate a bar plot
def generate_chart():
    user_height = float(height_entry.get())
    
    # Create a list of celebrities 
    celebrities = list(famous_peeps_heights.keys())
    
    # Create a corresponding list of heights for the celebrities
    celebrity_heights = [famous_peeps_heights[celeb] for celeb in celebrities]
    
    # Append the user's height
    celebrities.append("You")
    celebrity_heights.append(user_height)
    
    plt.figure(figsize=(8, 6))
    
    # Use the custom_colors list for the bar colors
    ax = sns.barplot(y=celebrity_heights, x=celebrities, palette=custom_colors, hue=celebrities) 
    ax.set(ylabel='Height (cm)', xlabel='Celebrities')
    plt.title('Height Comparison with Celebrities')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility

    plt.show()

# Create the main window
root = tk.Tk()
root.title("Height Comparison Chart")
root.geometry("600x400")  # Set window size to 600x400

# Create input label and entry
height_label = tk.Label(root, text="Enter your height (in cm):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Create the Generate Chart button
generate_button = tk.Button(root, text="Generate Chart", command=generate_chart)
generate_button.pack()

# Start the Tkinter main loop
root.mainloop()




