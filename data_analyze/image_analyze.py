import cv2
import numpy as np
import os

# Define the path to your images folder
image_folder_path = 'data_analyze'

def load_images_from_folder(folder):
    """
    Load all image paths from the specified folder.
    """
    images = []
    valid_extensions = ["png", "jpg", "jpeg"]
    for filename in os.listdir(folder):
        file_extension = filename.split(".")[-1].lower()
        if file_extension in valid_extensions:
            images.append(os.path.join(folder, filename))
    return images

# Load all images from the specified directory
table_images_paths = load_images_from_folder(image_folder_path)

# Define the lower and upper bounds for the blue color
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([140, 255, 255])

def count_blue_rectangles(image_path):
    """
    Function to count blue rectangles in a given image and display them.
    """
    print(f"Analyzing image: {image_path}")
    
    # Load the image
    img = cv2.imread(image_path)
    
    # Convert the image to HSV color space
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Segment the blue region using a mask
    blue_mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
    
    # Find contours in the blue mask
    contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter out small contours which are likely noise
    min_contour_area = 1000  # Adjust based on the scale of the image
    filtered_contours = [c for c in contours if cv2.contourArea(c) > min_contour_area]
    
    # Draw the contours on the image
    img_with_contours = cv2.drawContours(img.copy(), filtered_contours, -1, (0, 255, 0), 2)  # -1 means drawing all contours. (0, 255, 0) is green color for contours
    
    # Show the image with marked contours
    cv2.imshow(f"Detected rectangles in {image_path}", img_with_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return len(filtered_contours)


# Count blue rectangles for each image
tables_count_per_image = [count_blue_rectangles(img_path) for img_path in table_images_paths]

# Total number of tables
total_tables = sum(tables_count_per_image)

print("\nSummary:")
print("Number of tables in each image:", tables_count_per_image)
print("Total number of tables:", total_tables)
