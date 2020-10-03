# Median Filtering on Image(SMF)
Median Filtering is a neighborhood filtering technique used in order to remove noise from images and enhance its quality.

Often during Image capturing and acquisition(specially in medical images) the image is disturbed by Salt and Pepper Noise(SPN)[Original pixel replaced by either maximum intenstiy pixel
or minimum intensity pixel] which mainly occurs due to certain faults in sensors
while capturing the image. Having noise in image makes it difficult for Computer Aided Detection(CAD). Nowadays, many Machine Learning and Deep Learning techniques are being applied on 
medical images for computer aided diagnosis to reduce human error. Image Preprocessing is an important stage before the image can be fed to the model. Not restricting to that itself,
Image Enhancement plays an important role in improving the quality of images and removing errors/noises from them.

## Algorithm 
The main idea of the median filter is to run through the signal entry by entry, replacing each entry with the median of neighboring entries. 
The pattern of neighbors is called the "window", which slides, entry by entry, over the entire signal. For one-dimensional signals, the most obvious window is just the
first few preceding and following entries, whereas for two-dimensional (or higher-dimensional) data the window 
must include all entries within a given radius or ellipsoidal region (i.e. the median filter is not a separable filter).

In Median filtering the edge detection becomes a bit difficult but that again is improved as we switch to fuzzy removal of noise. Median Filter is the most commonly used filter
just for the fact that it is computationally faster than other existing techniques.

## Metric Calculation
The popular metrics for judging the quality of enhancement technique are - RMSE, PSNR, SSIM, & IEF. 

These are statistical measures that judge the quality of output relying on data and mathematics. 

Check on the links to have a brief idea about the concepts. In *Median_Filter.c* these concepts are applied for images where each pixel acts as a data point.

1. Root Mean Squared Error(RMSE) - [Click To Know More](https://en.wikipedia.org/wiki/Root-mean-square_deviation)

2. Peak Signal to Noise Ratio(PSNR) - [Click To Know More](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio)

3. Structural Similarity(SSIM) - [Click To Know More](https://en.wikipedia.org/wiki/Structural_similarity)

4. Image Enhancement Factor(IEF) - [Click To Know More](https://in.mathworks.com/matlabcentral/answers/450377-how-to-calculate-enhancement-factor-for-an-image)

## Results
The SMF technique is used for removal of Salt and Pepper Noise but works well with other noises as well. SMF works well for upto 60% noise percentage. Above that it fails, new algorithms such as
fuzzy median technique, Adaptive Weighted Mean Filtering technique and a lot more have been introduced as an add on of this algorithm and that works upto 85% noise.
