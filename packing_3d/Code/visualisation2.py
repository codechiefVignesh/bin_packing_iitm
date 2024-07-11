import numpy as np
import matplotlib.pyplot as plt
from colors import color
import json
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def visualise(items,truck_dim):
    # Define the corners of the container box (opposite corners)
    container_corners = np.array([[0, 0, 0], [truck_dim["length"], truck_dim["width"], truck_dim["height"]]])
    
    item_arrangements = json.loads(items)

    # Collecting the end points of each item
    items_coords = []
    for i in range(len(item_arrangements)):
        item = [[item_arrangements[i]["x"],item_arrangements[i]["y"],item_arrangements[i]["z"]],[item_arrangements[i]["x2"],item_arrangements[i]["y2"],item_arrangements[i]["z2"]]]
        items_coords.append(item)

    items_coords.sort()
    print(items_coords)

    # Define the corners of the blocks (each row is a pair of opposite corners)
    blocks_corners = np.array(items_coords)

    # Function to plot a cuboid given the corners
    def plot_cuboid(ax, corner1, corner2, color='blue', alpha=0.5,truck=False):
        if truck==True:
            x = [corner1[0], corner2[0] + 2]
        else:
            x = [corner1[0], corner2[0]]
        y = [corner1[1], corner2[1]]
        z = [corner1[2], corner2[2]]

        xx, yy = np.meshgrid(x, y)
        # Create 2D arrays for Z coordinates
        zz_bottom = np.full_like(xx, z[0])  # Bottom face
        zz_top = np.full_like(xx, z[1])    # Top face
        ax.plot_surface(xx, yy, zz_bottom, color=color, alpha=alpha)
        ax.plot_surface(xx, yy, zz_top, color=color, alpha=alpha)

        yy, zz = np.meshgrid(y, z)
        xx_left = np.full_like(yy, x[0])   # Left face
        xx_right = np.full_like(yy, x[1])  # Right face
        ax.plot_surface(xx_left, yy, zz, color=color, alpha=alpha)
        if truck==False:
            ax.plot_surface(xx_right, yy, zz, color=color, alpha=alpha)

        xx, zz = np.meshgrid(x, z)
        yy_front = np.full_like(xx, y[0])  # Front face
        yy_back = np.full_like(xx, y[1])   # Back face
        ax.plot_surface(xx, yy_front, zz, color=color, alpha=alpha)
        ax.plot_surface(xx, yy_back, zz, color=color, alpha=alpha)

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the container box
    plot_cuboid(ax, container_corners[0], container_corners[1], color='brown', alpha=0.5, truck=True)

    # Set labels
    ax.set_xlabel('Length')
    ax.set_ylabel('Width')
    ax.set_zlabel('Height')

    # Plot each block
    for i,block in enumerate(blocks_corners):
        plot_cuboid(ax, block[0], block[1], color=color[i], alpha=0.7)
        x_text = (block[0][0] + block[1][0]) / 2
        y_text = (block[0][1] + block[1][1]) / 2
        z_text = (block[0][2] + block[1][2]) / 2
        itemid = item_arrangements[i]["itemid"]
        location = item_arrangements[i]['location']
        ax.text(x_text, y_text, z_text, f'Item ID: {itemid} loc:{location}', color='black', fontsize=15, ha='center', va='center')
        plt.pause(2)

    plt.show()
        

    