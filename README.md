📋 Features1. Point OperationsThese functions modify each pixel independently based on its current value:Addition & Subtraction: Used to adjust image Brightness.Division: Useful for contrast manipulation and lighting normalization.Complement: Generates the Negative of an image by inverting pixel intensities.2. Neighborhood Processing (Spatial Filtering)These functions determine a pixel's new value based on its surrounding neighbors using convolution masks:Smoothing (Low Pass Filters):average_filter: Uses a $3 \times 3$ mean kernel to reduce noise and blur the image.median_filter: A non-linear filter excellent for removing Salt & Pepper noise while preserving edges.mode_filter: Replaces the center pixel with the most frequent value in the neighborhood.Edge Detection (High Pass Filters):laplacian_filter: Highlights regions of rapid intensity change to detect object boundaries.Morphological Operations:max_filter (Dilation) & min_filter (Erosion): Used to enhance or shrink image features.🚀 How to UsePlace an image named image.jpg in the project root directory.Run the script or import the functions into your workflow:Pythonimport cv2

# Example: Applying a Median Filter to remove noise
noisy_img = cv2.imread("image.jpg", 0)
clean_img = median_filter(noisy_img)

cv2.imshow('Cleaned Image', clean_img)
cv2.waitKey(0)
💡 Technical NoteThe mode_filter implementation uses manual nested loops and scipy.stats for educational purposes. It is designed to illustrate the logic behind non-linear neighborhood operations.Developed as part of Digital Image Processing academic research.
---
# ==========================================
# TEST BLOCK:
# ==========================================
if __name__ == "__main__":
    if img_color is not None:
        # 1. عرض نتائج العمليات النقطية (Point Operations)
        cv2.imshow('1- Original Color', img_color)
        cv2.imshow('2- Added (Brightness +50)', added_image)
        cv2.imshow('3- Complement (Negative)', complement_image)
        cv2.imshow('4- Subtracted', subtracted_image)
        cv2.imshow('5- Average Filter (Blur)', average_filtered_image)
        cv2.imshow('6- Laplacian (Edges)', laplacian_filtered_image)
        cv2.imshow('7- Median Filter (No Noise)', median_filtered_image)  
        cv2.imshow('8- Mode Filter Result', mode_filtered_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("null img")
