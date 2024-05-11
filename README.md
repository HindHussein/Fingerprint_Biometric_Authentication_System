# Fingerprint Biometric Authentication System using SIFT and FLANN
The fingerprint biometric authentication system was done using the python language where both the SIFT and FLANN algorithms were deployed. The system would compare the user's real fingerprint with every altered fingerprint until the closest match was chosen.  



# SIFT Keypoints
<br>
<img width="300" alt="SIFT Keypoints" src="https://github.com/HindSuleimanHussein/Fingerprint_Biometric_Authentication_System/assets/118082388/83156256-a071-4ffe-90ea-4f1db39639fa">
<br>
The library cv2 used in order to provide functions for computer vision tasks, such as SIFT and FLANN, were imported. Cv2 allows loading, displaying, manipulating, and processing images, and detection and extraction of certain features within said images. The majority of image matching was done within a loop for threshold. Each threshold value (0.1 until 0.9) resulted in a different table of FNMR and FMR. The calculations of FNMR and FMR were done by loading the seven altered and seven real pictures and looping through the real pictures to determine if there was a match. The images were converted to grayscale for the main purpose of representing the intensity information since SIFT operates on intensity values. The SIFT algorithm will then detect each image’s key points. The images are matched using the FLANN matcher for the quickest way to find similarities between images. 

# FLANN Compare Keypoints
<br>
<img width="300" alt="FLANN Compare Keypoints" src="https://github.com/HindSuleimanHussein/Fingerprint_Biometric_Authentication_System/assets/118082388/76a40138-2008-4e66-bf85-d99c9441f550">
<br>

The good matches are filtered and dependent on the best match will be printed to inform the user of the real and altered image with the greater similarity. The match between the user’s real and altered image would then be stored in the FNMR, while the match between the user’s real image and another’s altered image would be stored in the FMR, as shown in Table 1 with a threshold equal to 0.9. The mathematical equations to determine the rates of each FNMR and FMR point were done for each threshold, and then plotted on the graph. The graph was done by importing a library matplot that draws the ROC curve based on the rate of the FNMR and FMR over an increasing threshold. 


# FNMR/FMR Rate over an Increasing Threshold
<br>
<img width="300" alt="FNMR/FMR Rate over an Increasing Threshold" src="https://github.com/HindSuleimanHussein/Fingerprint_Biometric_Authentication_System/assets/118082388/1c451d75-0c79-4996-8cf9-b9c1cf4ee1a5">
<br>
The graph shows how the FNMR increases and FMR decreases as the threshold decreases due to the system becoming more sensitive, meaning malicious users would not be able to enter the system. However, an increased FNMR would lead to many legitimate users being rejected from the system. The Error Enrollment Rate shows how the FNMR and FMR meet at a threshold of 0.2 before FNMR increases and FMR decreases. 

# Output
/Users/hindsuleiman/PycharmProjects/ComputerSecurity/venv/bin/python /Users/hindsuleiman/PycharmProjects/ComputerSecurity/venv/lib/python3.12/site-packages/pip/__main__.py 
current threshold: 0.1
Error: Unable to load target image '/Users/hindsuleiman/PycharmProjects/ComputerSecurity/pic/.DS_Store'
For image: 92__CR.BMP
Best match: 92__F.BMP
Score: 0.20689655172413793
Error: Unable to load target image '/Users/hindsuleiman/PycharmProjects/ComputerSecurity/pic/.DS_Store'
For image: 81__Obl.BMP
Best match: 81__F.BMP
Score: 0.3170731707317073
Error: Unable to load target image '/Users/hindsuleiman/PycharmProjects/ComputerSecurity/pic/.DS_Store'
For image: 6__Obl.BMP
Best match: 6__M.BMP
Score: 0.48148148148148145
Error: Unable to load target image '/Users/hindsuleiman/PycharmProjects/ComputerSecurity/pic/.DS_Store'
For image: 9__Zcut.BMP
Best match: 9__M.BMP
Score: 0.6379310344827587
Error: Unable to load target image '/Users/hindsuleiman/PycharmProjects/ComputerSecurity/pic/.DS_Store'
For image: 29__Obl.BMP
Best match: 29__F.BMP
Score: 0.21052631578947367
Error: Unable to load target image '/Users/hindsuleiman/PycharmProjects/ComputerSecurity/pic/.DS_Store'
For image: 54__CR.BMP
Best match: 54__M.BMP
Score: 0.6538461538461539
Error: Unable to load target image '/Users/hindsuleiman/PycharmProjects/ComputerSecurity/pic/.DS_Store'
For image: 35__Obl.BMP
Best match: 35__M.BMP
Score: 0.15555555555555556
               29__F.BMP      35__M.BMP      54__M.BMP      6__M.BMP       81__F.BMP      92__F.BMP      9__M.BMP       
29__Obl.BMP    0.21           0.00           0.00           0.00           0.00           0.00           0.00           
35__Obl.BMP    0.00           0.16           0.00           0.00           0.00           0.00           0.00           
54__CR.BMP     0.00           0.00           0.65           0.00           0.00           0.00           0.00           
6__Obl.BMP     0.00           0.00           0.00           0.48           0.00           0.00           0.00           
81__Obl.BMP    0.00           0.00           0.00           0.00           0.32           0.00           0.00           
92__CR.BMP     0.00           0.00           0.00           0.00           0.00           0.21           0.00           
9__Zcut.BMP    0.00           0.00           0.00           0.00           0.00           0.00           0.64           

FNMR: 0/7
FMR: 7/42


current threshold: 0.2
For image: 92__CR.BMP
Best match: 92__F.BMP
Score: 0.2413793103448276
For image: 81__Obl.BMP
Best match: 81__F.BMP
Score: 0.3170731707317073
For image: 6__Obl.BMP
Best match: 6__M.BMP
Score: 0.48148148148148145
For image: 9__Zcut.BMP
Best match: 9__M.BMP
Score: 0.7758620689655172
For image: 29__Obl.BMP
Best match: 29__F.BMP
Score: 0.24561403508771928
For image: 54__CR.BMP
Best match: 54__M.BMP
Score: 0.6923076923076923
For image: 35__Obl.BMP
Best match: 35__M.BMP
Score: 0.17777777777777778
               29__F.BMP      35__M.BMP      54__M.BMP      6__M.BMP       81__F.BMP      92__F.BMP      9__M.BMP       
29__Obl.BMP    0.25           0.00           0.00           0.00           0.00           0.00           0.00           
35__Obl.BMP    0.00           0.18           0.00           0.00           0.00           0.00           0.00           
54__CR.BMP     0.00           0.00           0.69           0.00           0.00           0.00           0.00           
6__Obl.BMP     0.00           0.00           0.00           0.48           0.00           0.00           0.00           
81__Obl.BMP    0.00           0.00           0.00           0.00           0.32           0.00           0.01           
92__CR.BMP     0.00           0.00           0.00           0.00           0.00           0.24           0.00           
9__Zcut.BMP    0.00           0.00           0.00           0.00           0.03           0.00           0.78           

FNMR: 1/7
FMR: 6/42


current threshold: 0.3
For image: 92__CR.BMP
Best match: 92__F.BMP
Score: 0.27586206896551724
For image: 81__Obl.BMP
Best match: 81__F.BMP
Score: 0.34146341463414637
For image: 6__Obl.BMP
Best match: 6__M.BMP
Score: 0.48148148148148145
For image: 9__Zcut.BMP
Best match: 9__M.BMP
Score: 0.7931034482758621
For image: 29__Obl.BMP
Best match: 29__F.BMP
Score: 0.2631578947368421
For image: 54__CR.BMP
Best match: 54__M.BMP
Score: 0.6923076923076923
For image: 35__Obl.BMP
Best match: 35__M.BMP
Score: 0.17777777777777778
               29__F.BMP      35__M.BMP      54__M.BMP      6__M.BMP       81__F.BMP      92__F.BMP      9__M.BMP       
29__Obl.BMP    0.26           0.00           0.00           0.00           0.00           0.00           0.00           
35__Obl.BMP    0.00           0.18           0.00           0.00           0.00           0.00           0.00           
54__CR.BMP     0.00           0.00           0.69           0.00           0.00           0.00           0.00           
6__Obl.BMP     0.00           0.00           0.00           0.48           0.00           0.00           0.00           
81__Obl.BMP    0.00           0.00           0.00           0.00           0.34           0.00           0.02           
92__CR.BMP     0.00           0.00           0.00           0.00           0.00           0.28           0.00           
9__Zcut.BMP    0.00           0.00           0.00           0.00           0.03           0.00           0.79           

FNMR: 3/7
FMR: 4/42


current threshold: 0.4
For image: 92__CR.BMP
Best match: 92__F.BMP
Score: 0.27586206896551724
For image: 81__Obl.BMP
Best match: 81__F.BMP
Score: 0.35365853658536583
For image: 6__Obl.BMP
Best match: 6__M.BMP
Score: 0.48148148148148145
For image: 9__Zcut.BMP
Best match: 9__M.BMP
Score: 0.7931034482758621
For image: 29__Obl.BMP
Best match: 29__F.BMP
Score: 0.2631578947368421
For image: 54__CR.BMP
Best match: 54__M.BMP
Score: 0.7692307692307693
For image: 35__Obl.BMP
Best match: 35__M.BMP
Score: 0.17777777777777778
               29__F.BMP      35__M.BMP      54__M.BMP      6__M.BMP       81__F.BMP      92__F.BMP      9__M.BMP       
29__Obl.BMP    0.26           0.00           0.00           0.00           0.00           0.00           0.00           
35__Obl.BMP    0.00           0.18           0.00           0.00           0.00           0.00           0.00           
54__CR.BMP     0.00           0.00           0.77           0.00           0.00           0.00           0.00           
6__Obl.BMP     0.00           0.00           0.00           0.48           0.00           0.00           0.00           
81__Obl.BMP    0.01           0.00           0.00           0.00           0.35           0.00           0.02           
92__CR.BMP     0.00           0.00           0.00           0.00           0.00           0.28           0.00           
9__Zcut.BMP    0.00           0.00           0.00           0.00           0.03           0.02           0.79           

FNMR: 4/7
FMR: 3/42


current threshold: 0.5
For image: 92__CR.BMP
Best match: 92__F.BMP
Score: 0.27586206896551724
For image: 81__Obl.BMP
Best match: 81__F.BMP
Score: 0.3780487804878049
For image: 6__Obl.BMP
Best match: 6__M.BMP
Score: 0.5
For image: 9__Zcut.BMP
Best match: 9__M.BMP
Score: 0.8275862068965517
For image: 29__Obl.BMP
Best match: 29__F.BMP
Score: 0.2631578947368421
For image: 54__CR.BMP
Best match: 54__M.BMP
Score: 0.8461538461538461
For image: 35__Obl.BMP
Best match: 35__M.BMP
Score: 0.2
               29__F.BMP      35__M.BMP      54__M.BMP      6__M.BMP       81__F.BMP      92__F.BMP      9__M.BMP       
29__Obl.BMP    0.26           0.00           0.00           0.00           0.00           0.00           0.02           
35__Obl.BMP    0.00           0.20           0.00           0.00           0.00           0.00           0.00           
54__CR.BMP     0.04           0.08           0.85           0.00           0.00           0.00           0.00           
6__Obl.BMP     0.02           0.02           0.00           0.50           0.00           0.00           0.00           
81__Obl.BMP    0.01           0.00           0.00           0.00           0.38           0.00           0.02           
92__CR.BMP     0.00           0.00           0.00           0.00           0.00           0.28           0.00           
9__Zcut.BMP    0.00           0.00           0.00           0.00           0.03           0.03           0.83           

FNMR: 5/7
FMR: 2/42


current threshold: 0.6
For image: 92__CR.BMP
Best match: 92__F.BMP
Score: 0.27586206896551724
For image: 81__Obl.BMP
Best match: 81__F.BMP
Score: 0.3902439024390244
For image: 6__Obl.BMP
Best match: 6__M.BMP
Score: 0.5
For image: 9__Zcut.BMP
Best match: 9__M.BMP
Score: 0.8448275862068966
For image: 29__Obl.BMP
Best match: 29__F.BMP
Score: 0.2631578947368421
For image: 54__CR.BMP
Best match: 54__M.BMP
Score: 0.8461538461538461
For image: 35__Obl.BMP
Best match: 35__M.BMP
Score: 0.2222222222222222
               29__F.BMP      35__M.BMP      54__M.BMP      6__M.BMP       81__F.BMP      92__F.BMP      9__M.BMP       
29__Obl.BMP    0.26           0.00           0.00           0.00           0.05           0.00           0.02           
35__Obl.BMP    0.00           0.22           0.00           0.00           0.00           0.00           0.00           
54__CR.BMP     0.08           0.19           0.85           0.00           0.00           0.00           0.00           
6__Obl.BMP     0.04           0.04           0.00           0.50           0.02           0.00           0.00           
81__Obl.BMP    0.05           0.02           0.00           0.00           0.39           0.01           0.02           
92__CR.BMP     0.00           0.00           0.00           0.00           0.00           0.28           0.00           
9__Zcut.BMP    0.03           0.00           0.00           0.00           0.07           0.05           0.84           

FNMR: 5/7
FMR: 2/42


current threshold: 0.7
For image: 92__CR.BMP
Best match: 92__F.BMP
Score: 0.27586206896551724
For image: 81__Obl.BMP
Best match: 81__F.BMP
Score: 0.4024390243902439
For image: 6__Obl.BMP
Best match: 6__M.BMP
Score: 0.5
For image: 9__Zcut.BMP
Best match: 9__M.BMP
Score: 0.8448275862068966
For image: 29__Obl.BMP
Best match: 29__F.BMP
Score: 0.2631578947368421
For image: 54__CR.BMP
Best match: 54__M.BMP
Score: 0.8461538461538461
For image: 35__Obl.BMP
Best match: 35__M.BMP
Score: 0.2222222222222222
               29__F.BMP      35__M.BMP      54__M.BMP      6__M.BMP       81__F.BMP      92__F.BMP      9__M.BMP       
29__Obl.BMP    0.26           0.04           0.02           0.02           0.07           0.02           0.05           
35__Obl.BMP    0.04           0.22           0.04           0.00           0.02           0.00           0.00           
54__CR.BMP     0.15           0.23           0.85           0.04           0.08           0.04           0.00           
6__Obl.BMP     0.06           0.13           0.00           0.50           0.04           0.00           0.00           
81__Obl.BMP    0.06           0.05           0.01           0.04           0.40           0.01           0.02           
92__CR.BMP     0.00           0.00           0.03           0.00           0.00           0.28           0.03           
9__Zcut.BMP    0.07           0.03           0.00           0.02           0.09           0.05           0.84           

FNMR: 5/7
FMR: 2/42


current threshold: 0.8
For image: 92__CR.BMP
Best match: 92__F.BMP
Score: 0.3103448275862069
For image: 81__Obl.BMP
Best match: 81__F.BMP
Score: 0.4146341463414634
For image: 6__Obl.BMP
Best match: 6__M.BMP
Score: 0.5185185185185185
For image: 9__Zcut.BMP
Best match: 9__M.BMP
Score: 0.8620689655172413
For image: 29__Obl.BMP
Best match: 29__F.BMP
Score: 0.2982456140350877
For image: 54__CR.BMP
Best match: 54__M.BMP
Score: 0.8461538461538461
For image: 35__Obl.BMP
Best match: 35__M.BMP
Score: 0.2222222222222222
               29__F.BMP      35__M.BMP      54__M.BMP      6__M.BMP       81__F.BMP      92__F.BMP      9__M.BMP       
29__Obl.BMP    0.30           0.12           0.09           0.07           0.12           0.04           0.11           
35__Obl.BMP    0.07           0.22           0.07           0.07           0.04           0.04           0.02           
54__CR.BMP     0.23           0.31           0.85           0.12           0.15           0.15           0.12           
6__Obl.BMP     0.11           0.20           0.02           0.52           0.09           0.04           0.02           
81__Obl.BMP    0.07           0.06           0.05           0.06           0.41           0.05           0.09           
92__CR.BMP     0.14           0.07           0.03           0.03           0.00           0.31           0.07           
9__Zcut.BMP    0.14           0.07           0.05           0.03           0.14           0.12           0.86           

FNMR: 5/7
FMR: 2/42


current threshold: 0.9
For image: 92__CR.BMP
Best match: 92__F.BMP
Score: 0.4482758620689655
For image: 81__Obl.BMP
Best match: 81__F.BMP
Score: 0.5365853658536586
For image: 6__Obl.BMP
Best match: 6__M.BMP
Score: 0.5740740740740741
For image: 9__Zcut.BMP
Best match: 9__M.BMP
Score: 0.8793103448275862
For image: 29__Obl.BMP
Best match: 29__F.BMP
Score: 0.42105263157894735
For image: 54__CR.BMP
Best match: 54__M.BMP
Score: 0.8461538461538461
For image: 35__Obl.BMP
Best match: 35__M.BMP
Score: 0.37777777777777777
               29__F.BMP      35__M.BMP      54__M.BMP      6__M.BMP       81__F.BMP      92__F.BMP      9__M.BMP       
29__Obl.BMP    0.42           0.30           0.30           0.23           0.32           0.23           0.23           
35__Obl.BMP    0.20           0.38           0.24           0.22           0.24           0.24           0.20           
54__CR.BMP     0.35           0.42           0.85           0.27           0.35           0.31           0.38           
6__Obl.BMP     0.28           0.43           0.26           0.57           0.33           0.24           0.09           
81__Obl.BMP    0.26           0.17           0.23           0.23           0.54           0.32           0.26           
92__CR.BMP     0.28           0.31           0.24           0.14           0.21           0.45           0.17           
9__Zcut.BMP    0.28           0.43           0.26           0.24           0.26           0.29           0.88           

FNMR: 7/7
FMR: 0/42
