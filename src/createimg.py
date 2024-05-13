import numpy as np
import matplotlib.pyplot as plt

def create_noise(arr, name):
    # Example array with values between 0 and 1
    array = np.array(arr)

    plt.gca().set_axis_off()
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
                hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    plt.imshow(array, cmap='gray')
    plt.savefig(f'{name}.png', bbox_inches="tight", pad_inches=0)  # Save the figure to a file
    plt.close()  # Close the figure window to free up memory