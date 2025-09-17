#Importing Relevant Modules
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Creating a dataframe and storing the data from the file within it.
data = pd.read_csv("Python Workshop Challenge 2 Sample Data.csv")

# Select all rows from the first column of the dataframe and stores within a list.
x = data.iloc[:,0].tolist()

# Select all rows from the second column of the dataframe and stores within a list.
y = data.iloc[:,1].tolist()

# Opens a PDF file called "charts.pdf" for writing. Everything in the block below is saved to it.
with PdfPages("charts.pdf") as pdf:
    # Starts a new blank figure
    plt.figure()
    # Create the first chart as a line chart in red.
    plt.plot(x, y, color="red", label="Data Line")
    plt.title("Line Chart")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.legend()
    # Saves this chart as a page in the PDF.
    pdf.savefig()
    # Closes the figure from memory.
    plt.close()

    # Create a new blank figure.
    plt.figure()
    # Creates a scatterplot.
    plt.scatter(x, y, color="green", label="Data Points")
    plt.title("Scatter Plot")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.legend()
    pdf.savefig()
    plt.close()

    plt.figure()
    # Creates a bar chart.
    plt.bar(x, y, color="blue", label="Data Bars")
    plt.title("Bar Graph")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.legend()
    pdf.savefig()
    plt.close()
