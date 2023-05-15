# predi-health-app
A real-time diagnostic and predictive application that collects and evaluates data from your Fitbit watchFor more information about me, please visit my LinkedIn:

[![LinkedIn][LinkedIn.js]][LinkedIn-url]

<!-- ABOUT THE PROJECT -->

## About The Project:

### Introduction:

In America alone, 12 million people are impacted by misdiagnosis errors. This can be caused by human error, outdated treatment practices, or a knowledge gap between a patient and their doctor. Doctors may prescribe medication or advise patients without having knowledge of their daily routines, leading to uncertainty about whether their instructions have been followed.

Fortunately, 84% of Americans own smartphones and 45% regularly use smartwatches like Apple Watches and Fitbits, which can provide unique insights into a user's health data. Our team recognized the potential of this data to improve the diagnostic process in America and beyond. This led us to create Predi, a live diagnostics and predictive app that aims to bridge the gap between doctors and their patients.

The app offers three main functions to enhance communication between patients and their doctors. 

1. It provides real-time reporting of health-related data, including Fitbit data and user search queries, directly to the patient's doctor.
2. Users can search the app for any symptoms they are experiencing, and the app can report these searches to the doctor with informed guesses on potential causes.
3. The app can track the user's Fitbit health data to identify any trends or information in their health records that may not be immediately apparent to their doctor.

### How is it different?

Predi sets itself apart from current technology in several key ways. First, it offers a more personalized approach to symptom identification. While traditional methods rely on manual input of symptoms into a search bar, Predi leverages user search queries and Fitbit data to make more informed decisions about what a user might be experiencing.

Second, Predi is highly accessible and affordable. Users only need a smartphone and smartwatch to record, monitor, and report their health data, eliminating the need for expensive or complicated technologies.

Third, while the accuracy of data collected by smartwatches may vary, Predi's continuous monitoring and analysis of a user's health data helps bridge the knowledge gap between patients and doctors, providing doctors with a more comprehensive understanding of their patients' health status over time.

Finally, Predi's reporting system is designed to allow doctors to access and verify patient data. Unlike other apps that simply make guesses about a user's symptoms, Predi enables doctors to review and confirm the app's findings, providing a more reliable and trustworthy source of health information.

<b> Group of people it serves: </b>

1. Doctors who want a more comprehensive understanding of their patients' health and a faster, more accurate diagnosis of their conditions.
2. Regular users who wish to monitor their health continuously and receive prompt assistance for any health-related issues they may encounter.
3. Regular users who aim to establish a connection with their doctor outside of the hospital.

## Getting Started:

To get the project running, there's a few programs and steps needed.

### Built With:

* <img src="https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white">
* <img src="https://img.shields.io/badge/-Flutter-02569B?style=flat&logo=flutter&logoColor=white">
* <img src="https://img.shields.io/badge/-FastAPI-009688?style=flat&logo=fastapi&logoColor=white">
* <img src="https://img.shields.io/badge/-Redis-DC382D?style=flat&logo=redis&logoColor=white">
* <img src="https://img.shields.io/badge/-TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white">

### Prerequisites:

* A computer with a supported operating system (Windows, macOS, or Linux)
* Flutter SDK
* Integrated development environment (IDE) 
* Android SDK or Xcode (Android or iOS)
* A device or emulator to test the app on
* Basic knowledge of programming concepts and the Dart programming language.

### System Design

To simplify and allocate dedicated resources to the system, it was divied into four distinct components: 

1. Front-end (mobile app)
2. Back-end (controller)
3. AI model
4. Database

The controller and AI model were further separated into two distinct components to minimize complexity. They can communicate with each other only through a message broker.

### Steps to run the code:

 Download the "predi-health-app" zip file found in the uploaded files.
 
To do that, simply press on the zip file, then press "view raw" as shown below to download it:

![image](https://github.com/SaliElloh/predi-health-app/assets/112829375/d2292731-c6a6-4f65-ae87-51a248e1124f)

# User Stories:

The table below outlines the app's objectives and the corresponding achievements:

<table>
  <tr>
    <th>As an...</th>
    <th>I want to...</th>
    <th>So that...</th>
  </tr>
  <tr>
    <td>Doctor</td>
    <td>keep track of my patients drug intake</td>
    <td>they are not prescribed drugs that could have negative interactions</td>
  </tr>
  <tr>
    <td>Doctor</td>
    <td>monitor my patients possible negative interactions</td>
    <td>so that I can warn them correctly</td>
  </tr>
  <tr>
    <td>New user</td>
    <td>create an account on the app and link with my Fitbit watch</td>
    <td>I can track my health through the app</td>
  </tr>
  <tr>
    <td>Regular user</td>
    <td>link my account with my Google account</td>
    <td>The app can access my search history</td>
  </tr>
  <tr>
    <td>Regular user</td>
    <td>get suggestions based on my search history and Fitbit data</td>
    <td>I can get suggestions on what's the best course of action</td>
  </tr>
  <tr>
    <td>Doctor</td>
    <td>view my patient's search history and Fitbit data</td>
    <td>I can correlate it with their health record</td>
  </tr>
  <tr>
    <td>Doctor</td>
    <td>get notified if one of my patients has a serious accident</td>
    <td>I can assist them at the earliest</td>
  </tr>
  <tr>
    <td>Regular user</td>
    <td>use the app to Google my symptoms</td>
    <td>The app sends warnings of serious health issues to my assigned doctor</td>
  </tr>
  <tr>
    <td>Doctor</td>
    <td>be able to validate or deny the serious warnings</td>
    <td>My assigned patient can receive only the valid warnings</td>
  </tr>
  <tr>
    <td>Regular user</td>
    <td>have access to a set of articles</td>
    <td>Can have an idea about the app's diagnosis</td>
  </tr>
  <tr>
    <td>Regular user</td>
    <td>get suggestions based on my search history and Fitbit data</td>
    <td>I can get suggestions on what's the best course of action</td>
  </tr>
</table>

### Screen shots from demo

![image](https://github.com/SaliElloh/predi-health-app/assets/112829375/21cbba24-2782-4043-98ef-e8c9e16e213b)


<!-- LICENSE -->
## License:

No License used.

<!-- CONTACT -->
## Contact:

Sali E-loh - [@Sali El-loh](https://www.linkedin.com/in/salielloh12/) - ellohsali@gmail.com

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments:

* Special thanks to Professor Jin Lu at the University of Michigan - Dearborn for assigning and helping with this project in his Algorithm Analysis and Design class. 

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[LinkedIn.js]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[LinkedIn-url]: https://www.linkedin.com/in/salielloh12/



