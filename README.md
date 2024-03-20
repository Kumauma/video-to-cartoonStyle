# video-to-cartoonStyle
This program converts a given video into an video that expresses a cartoon-like feeling well, and also converts it into an image that does not express a cartoon-like feeling well.

## How to Use
If you replace the character string variable `video_file` in the code with the name of the image in the same directory as the `.py` file and run the file, you can create a cartoon-style image and a non-cartoon-style image at the same time.<br>You can also modify the `target_format` variable in the code and convert it to the desired file extension name. The default file extension is `.mp4`.

## Limits of this algorithm
When it comes to making Cartoon-style videos, the conversion process is very slow, as each frame undergoes a total of three filtering sessions, which takes a long time to convert.<br>Therefore, I highly recommend that the video not exceed 20 seconds long.

## Result
<center>
    https://user-images.githubusercontent.com/51203951/9f3a9896-66ad-4ae3-aa35-7aa10e7efb73.mp4
    <h4>A Cartoon-Style video of a real person</h4>
    https://user-images.githubusercontent.com/51203951/5563ec9b-0ded-4aa1-9e20-49ddad8c99ac.mp4
    <h4>Transform animations so that they don't feel Cartoon-Style</h4>
</center>
