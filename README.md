# video-to-cartoonStyle
This program converts a given video into an video that expresses a cartoon-like feeling well, and also converts it into an image that does not express a cartoon-like feeling well.

## How to Use
If you replace the character string variable `video_file` in the code with the name of the image in the same directory as the `.py` file and run the file, you can create a cartoon-style image and a non-cartoon-style image at the same time.<br>You can also modify the `target_format` variable in the code and convert it to the desired file extension name. The default file extension is `.mp4`.

## Limits of this algorithm
When it comes to making Cartoon-style videos, the conversion process is very slow, as each frame undergoes a total of three filtering sessions, which takes a long time to convert.<br>Therefore, I highly recommend that the video not exceed 20 seconds long.<br>And there is also a problem of increasing the capacity of converted files.


## Result
<center>
    <img width="70%" src="https://github.com/Kumauma/video-to-cartoonStyle/assets/51203951/1ff062bb-e854-451e-bd47-aa27c32198b8"/>
    <h4>Cartoon-Style video of a real person</h4>
    <img width="70%" src="https://github.com/Kumauma/video-to-cartoonStyle/assets/51203951/f2a4e750-662f-4a59-9469-daac8a7a1d07"/>
    <h4>Not Cartoon-Style video of an Animation</h4>
</center>
