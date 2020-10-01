# Perspective Transform
using OpenCV methods
## How It Works
On selecting dimensions for a quadrilateral section, the code finds the maximum height and width of that selection and warps the selected area into a rectangle of dimensions `maxHeight * maxWidth`
## Usage
`python3 script.py --path image.jpg`

- It opens the image for you need to select coordinates in clockwise manner
 (top left -> top right -> bottom right -> bottom left).<br><br>
<img src = "https://drive.google.com/u/0/uc?id=1-ojbLqqCncITEmPw80TU_mTqJCOZvL-I&export=download"/><br><br>
- on pressing enter, it transforms the document.<br><br>
<img src = "https://drive.google.com/u/0/uc?id=102QeYDxNEw8-vYaBniKexzlXw_-WkL-I&export=download"/>
