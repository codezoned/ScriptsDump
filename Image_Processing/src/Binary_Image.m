%Binary Image by Master-Fury

clear all;

%Setting up the directory
fpath1=fullfile('C:\Users\Manish (Master)\Desktop\images');  % Add your directory   
addpath(fpath1);
basefile=sprintf('*.png');                                   % Add format of image
all_images=fullfile(fpath1,basefile);
fnames=dir(all_images);


% READING OF IMAGE 
for i = 1:length(fnames)
    all_images = fullfile(fnames(i).folder, fnames(i).name);
    I = imread(all_images);  % Image reading using imread
    figure
    imshow(I)                  % To see original image
    title('Original Image');
    % The original image contains colors RGB (in matlab it stores in the format RBG)
    % Conversion of image into gray-scale image can be done by removing any one color from image. 

    Gray_Scale=I(:,:,2);           % Green color removed. 
    figure
    imshow(Gray_Scale)
    title('Grey-Scale Version of Image')

    % Conversion of GRAY-SCALE to BINARY IMAGE
    Binary_Image = imbinarize(Gray_Scale,'adaptive','ForegroundPolarity','dark','Sensitivity',0.4); 
    % You can use different methods like instead of adaptive you can use global(by default).
    % Foreground Polarity can be dark or bright (refer documentaion for more info)
    % Sensitivity can be from 0 to 1 , by default it is 0.5
    figure
    imshow(Binary_Image)
    title('Binary Version of Image')
end
% SPECIAL NOTE
% There is major difference between gray-scale image and binary image. The
% differnce is - binary images consists only 0 & 1 (refer workspace) matrix
% 1 represents white and 0 represents black. 
% A binary image is a digital image that has only two possible values for each pixel.
% In the case of gray scale image, 
% for example 8-bit gray scale image (2^8=256) pixel value may vary between 0 to 256.
