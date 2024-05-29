import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

# a variable to store the path for altered pictures
folder_path = "/Users/hindsuleiman/PycharmProjects/ComputerSecurity/alt"

# a variable to store the path for altered pictures
target_dir = "/Users/hindsuleiman/PycharmProjects/ComputerSecurity/pic"
target_file_names = sorted(os.listdir(target_dir))
FNMR_rates = []
FMR_rates = []
ALL_FNMR_RATES = []
ALL_FMR_RATES = []
threshold_values = [i / 10 for i in range(1, 10)]  # creating an array containing all threshold values
for threshold_value in threshold_values: # looping through threshold to get each value for each threshold
    FNMR_Values = 0
    FMR_Values = 0
    table = []
    FNMR = []
    FMR = []
    print("current threshold: " + str(threshold_value)) # printing the current threshold
    # Loop through altered pictures to check if there's any matches
    for file in os.listdir(folder_path):
        # Check if the file is a BMP file to make sure it's a fingerprint picture
        if file.lower().endswith(".bmp"):
            # store the path for image to call it
            image_path = os.path.join(folder_path, file)

            # Load the BMP image
            image = cv2.imread(image_path)

            # Check if the image loaded successfully if not stop the program
            if image is None:
                print(f"Error: Unable to load image '{image_path}'")
                exit(0)

            # Initialize variables to know what image is the best one
            score = 0
            best_match_file = None

            # looping through all real images to check if there's a match
            for target_file in target_file_names:
                target_image_path = os.path.join(target_dir, target_file)
                target_image = cv2.imread(target_image_path)

                # Check if target image loaded successfully
                if target_image is None:
                    print(f"Error: Unable to load target image '{target_image_path}'")
                    continue

                # Convert images to grayscale
                source_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                target_gray = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

                # Initialize SIFT detector
                sift = cv2.SIFT_create()

                # Detect keypoints and compute descriptors
                kp1, des1 = sift.detectAndCompute(source_gray, None)
                kp2, des2 = sift.detectAndCompute(target_gray, None)

                # Match keypoints using FLANN
                matcher = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), dict())
                matches = matcher.knnMatch(des1, des2, k=2)

                # Filter good matches
                good_matches = []
                for m, n in matches:
                    if m.distance < threshold_value * n.distance:
                        good_matches.append(m)

                # Calculate score
                match_score = len(good_matches) / len(kp1)

                # Update score if current score is higher
                if match_score > score:
                    score = match_score
                    best_match_file = target_file
                    curr_image = target_image

                # checking if the score is FMR or not
                if match_score > threshold_value:
                    FMR_Values += 1

                # Store the altered image, score and real image to print them as a table
                table.append([file, "{:.2f}".format(match_score), target_file])
            # print the current image the is being checking with
            print("For image:", file)
            if best_match_file:
                # print best match for the current image
                print("Best match:", best_match_file)
                # print the score for the match
                print("Score:", score)
                # storing the score in FNMR
                FNMR.append(score)
                # check if the score is below or equal to the threshold to check if it's an FNMR or not
                if score <= threshold_value:
                    FNMR_Values += 1
                # using built-in function to show the current image and its best match and draw lines with the
                # matching points

                result = cv2.drawMatches(image, kp1, curr_image, kp2, good_matches, None)
                result = cv2.resize(result, None, fx=2.5, fy=2.5)
                cv2.imshow(f"Result for {file} and {curr_image}", result)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    # Calculate rates for FNMR and FMR
    FNMR_rate = FNMR_Values / len(FNMR)
    FMR_rate = FMR_Values / (len(table) - len(FNMR))

    # Store rates in array so we can use them at the end
    ALL_FMR_RATES.append(FMR_rate)
    ALL_FNMR_RATES.append(FNMR_rate)

    # Initialize dictionaries to store scores
    file_to_scores = {}
    target_file_to_scores = {}

    # Iterate through the table data and populate the dictionaries
    for file, score, target_file in table:
        if file not in file_to_scores:
            file_to_scores[file] = {}
        file_to_scores[file][target_file] = score

        if target_file not in target_file_to_scores:
            target_file_to_scores[target_file] = {}
        target_file_to_scores[target_file][file] = score

    # Get unique file and target file names
    file_names = sorted(file_to_scores.keys())
    target_file_names = sorted(target_file_to_scores.keys())

    # Print table header with target file names
    print("".ljust(15), end="")  # Empty space for alignment
    for target_file in target_file_names:
        print(target_file.ljust(15), end="")
    print()

    # Print table body with file names and scores
    for file_name in file_names:
        print(file_name.ljust(15), end="")
        for target_file in target_file_names:
            score = file_to_scores[file_name].get(target_file, "-")
            print(str(score).ljust(15), end="")
        print()

    print()
    print("FNMR: {}/{}".format(FNMR_Values, len(FNMR)))
    print("FMR: {}/{}".format(FMR_Values, (len(table) - len(FNMR))))
    print()
    print()

# Plot FNMR and FMR rates against thresholds
plt.plot(threshold_values, ALL_FNMR_RATES, color='blue', lw=2, label='FNMR')
plt.plot(threshold_values, ALL_FMR_RATES, color='red', lw=2, label='FMR')

eer_threshold = threshold_values[np.argmin(np.abs(np.array(ALL_FNMR_RATES) - np.array(ALL_FMR_RATES)))]
plt.scatter(eer_threshold, ALL_FNMR_RATES[threshold_values.index(eer_threshold)], color='orange',
            marker='o',
            label='EER')

plt.xlabel('Threshold')
plt.ylabel('Rate')
plt.title('False Negative Rate (FNMR) and False Positive Rate (FMR) vs Threshold')
plt.legend(loc="upper right")
plt.grid(True)
plt.show()