# video-to-cartoonStyle
This program converts a given video into an video that expresses a cartoon-like feeling well, and also converts it into an image that does not express a cartoon-like feeling well.

<center>
    <h4>A Cartoon-Style video of a real person</h4>
    <h4>Transform animations so that they don't feel Cartoon-Style</h4>
</center>

<h3> How to Use</h3>
If you replace the character string variable `video_file` in the code with the name of the image in the same directory as the `.py` file and run the file, you can create a cartoon-style image and a non-cartoon-style image at the same time.<br>You can also modify the `target_format` variable in the code and convert it to the desired file extension name. The default file extension is `.mp4`.

<h3>Limits of this algorithm</h3>
When it comes to making Cartoon-style videos, the conversion process is very slow, as each frame undergoes a total of three filtering sessions, which takes a long time to convert.<br>Therefore, I highly recommend that the video not exceed 20 seconds long.