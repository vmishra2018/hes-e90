### Project Report for E-90 Cloud Services Infrastructure and Computing(AWS).

Author: [Vivek Mishra](blpvivek@gmail.com)

#### Content:

[Project Statement](#project-statement)

[Git Location](#git-location)

[Youtube links](#youtube-links)

[Hardware Needed](#hardware-needed)

[Software Installations](#software-installations)

[Setup](#setup)

[Conclusion](#conclusion)

[Next Steps](#next-steps)

[References](#references)

#### Project statement 

Through this project I wanted to get some hands on experience with building  alexa skills and integrating them different devices (in this case raspberry pi and pi camera)

In this project I have built two skills

<li> Alexa Skill to turn the lights on and off.
<li> Alexa Skill to take a picture.

#### Git Location

https://github.com/vmishra2018/hes-e90

#### Youtube links

##### Project Summary https://youtu.be/G5Fb_8MANfM

##### Full Project Video https://youtu.be/boMzSNKP7Hk



#### Hardware Needed

<li> Amazon Echo device
<li> Raspberry pi 3b+
<li> Pi Camera 5mp
<li> 32 GB micro sd card
<li> Monitor for display
<li> Bread board
<li> LED emitter
<li> 330 ohm resister
<li> Jumper cables (male to female)

#### Software Installations

<li> Amazon developer account to setup alexa skill.
<li> Raspbian OS -- OS for raspberry pi
<li> Flask-ask  -- flask api to interact with alexa skills
<li> Ngrok -- making your local flask apis accessing thru a secured channel (giving a public url so alexa can call them)



#### Setup

##### Pi Setup

Pi Setup is very standard, I followed the below steps

<li> Download raspbian from [official site](https://www.raspberrypi.org/downloads/raspbian/) and unzip into your micro sd card and update the packages.

`sudo apt-get update && sudo apt-get upgrade -y` 

<li> Install flask-ask on raspberry pi

`sudo apt-get install flask-ask `

<li> install ngrok on raspberry pi from https://ngrok.com/ . Keep in mind that with ngrok free version you don't get a static url, everytime you restart you get a different url. you need to update that endpoint in alexa skill with that url.

##### Pi Camera  Setup

I used a youtube videos to basically setup the camera with raspberry pi and test if the camera was working or not.

Once the camera is attached to the pi, then we need to 

<li> enable camera from raspy-config

`sudo rasp-config` this will show the options

<li>test camera with following commands

`raspistill -o image-name` this will capture the image.

##### Breadboard setup

##### Alexa skill setup

I have created two skills, 

1. one is to send a gpio signal to turn the light on and off
2. Another one to take a picture using the camera module.



Skill Setup is very standard similar to what we have learnt int the class.

1. **Invocation name** raspberry pi
2. **Intents** Two intents for two skills
   1. gpiocontrol internt
   2. camera intent

Below is the complete json of the skill.

```yaml
{
    "interactionModel": {
        "languageModel": {
            "invocationName": "raspberry pi",
            "intents": [
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": [] 
                },
                {
                    "name": "AMAZON.NavigateHomeIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.FallbackIntent",
                    "samples": []
                },
                {
                    "name": "gpio",
                    "slots": [
                        {
                            "name": "status",
                            "type": "GPIO_CONTROL"
                        },
                        {
                            "name": "pin",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "turn gpio lights {status}",
                        "turn {status} the gpio lights"
                    ]
                },
                {
                    "name": "camera",
                    "slots": [],
                    "samples": [
                        "take a picture",
                        "take my picture"
                    ]
                }
            ],
            "types": [
                {
                    "name": "GPIO_CONTROL",
                    "values": [
                        {
                            "name": {
                                "value": "off"
                            }
                        },
                        {
                            "name": {
                                "value": "on"
                            }
                        }
                    ]
                }
            ]
        }
    }
} 
```





#### Testing.

I tried testing the skills using my echo device as well as through the test interface from developer console on amazon site

![image-20191214025717814](/images/alexa-test-1.png)

You can see the images being stored in the directory as well.

![image-20191214030000114](/images/alexa-test2.png)



**LED Test**



![image-20191214030210467](/images/alexa-test3.png)







#### Conclusion

I know I am just scratching the surface here. but i have learnt a lot about alexa skills and how we can integrate them with different devices.

#### Next Steps

- [ ] integrate s3 to store the images captured.
- [ ] build a voice remote skill with pi.
- [ ] Build a magic mirror to take a picture

#### References

https://www.hackster.io/user00317224/control-raspberry-pi-gpio-using-amazon-echo-ngrok-de41d1#toc-step-1--setup-0

https://www.youtube.com/watch?v=eObSqbe9aqU

https://youtu.be/qk1IVs5B1GI



