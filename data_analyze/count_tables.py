import cv2
import numpy as np
import os

def load_images_from_folder(folder):
    images = []
    valid_extensions = ["png", "jpg", "jpeg"]
    for filename in os.listdir(folder):
        file_extension = filename.split(".")[-1].lower()
        if file_extension in valid_extensions:
            images.append(os.path.join(folder, filename))
    return images

def count_blue_rectangles(image_path):
    print(f"Analyzing image: {image_path}")
    img = cv2.imread(image_path)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])
    blue_mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
    contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    min_contour_area = 1000
    filtered_contours = [c for c in contours if cv2.contourArea(c) > min_contour_area]
    return len(filtered_contours)


def main(repositories_dir):
    for owner_name in os.listdir(repositories_dir):
        owner_path = os.path.join(repositories_dir, owner_name)  # Get the full path for owner
        if os.path.isdir(owner_path):  # Ensure that owner_path is a directory before listing
            for repo_name in os.listdir(owner_path):
                repo_path = os.path.join(owner_path, repo_name)  # Corrected repo_path
                if os.path.isdir(repo_path):
                    tables_count = sum([count_blue_rectangles(img_path) for img_path in load_images_from_folder(repo_path)])

                    summary_path = os.path.join(repo_path, 'summary.txt')
                    if os.path.exists(summary_path):
                        with open(summary_path, 'a') as summary_file:  # 'a' mode for appending
                            summary_file.write(f'Number of Tables: {tables_count}\n')
                        print(f"Updated summary file with tables count for repository: {repo_name}")
                    else:
                        print(f"summary.txt not found for repository: {repo_name}")
    print("Number of tables added to summaries for all repositories.")
    
if __name__ == '__main__':
    main()