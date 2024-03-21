# Video to Cartoon Style Program
This program converts a given video into an video that expresses a cartoon-like feeling well, and also converts it into an image that does not express a cartoon-like feeling well.
![image](https://github.com/Kumauma/video-to-cartoonStyle/assets/51203951/f749ece5-2d32-4372-828d-46619142b728)
![image](https://github.com/Kumauma/video-to-cartoonStyle/assets/51203951/34f34a8f-1b44-4a99-aeee-8bb2300a9343)
![image](https://github.com/Kumauma/video-to-cartoonStyle/assets/51203951/cb0daa19-0e71-48fa-9c99-5abd718db26f)
![image](https://github.com/Kumauma/video-to-cartoonStyle/assets/51203951/8b901c45-6489-4c11-bca2-74fc5429a538)

## How to Use
If you replace the string variable `video_file` in the code with the name of the video in the same directory as the `.py` file or the absolute path of the video and run the file, you can create a cartoon-style video and a non-cartoon-style video at the same time.<br>You can also modify the `target_format` variable in the code and convert it to the desired file extension name. The default file extension is `.mp4`.

## Limits of this algorithm
When it comes to making Cartoon-style videos, the conversion process is very slow, as each frame undergoes a total of three filtering sessions, which takes a long time to convert.<br>Therefore, I highly recommend that the video not exceed 20 seconds long.<br>And there is also a problem of increasing the capacity of converted files.


## Result
<center>
    <img width="70%" src="https://github.com/Kumauma/video-to-cartoonStyle/assets/51203951/1ff062bb-e854-451e-bd47-aa27c32198b8"/>
    <h4>Cartoon-Style video of a real person</h4>
    <img width="70%" src="https://github.com/Kumauma/video-to-cartoonStyle/assets/51203951/f2a4e750-662f-4a59-9469-daac8a7a1d07"/>
    <h4>Not Cartoon-Style video of an Animation</h4>
</center>
