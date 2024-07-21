# Documentation

## Table of Contents

| Section       | Description                         |
|---------------|-------------------------------------|
| [Introduction](#introduction) | Bin Packing Codes          |
| [Installation Guide](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document7.md) | Required software installation          |
| [Basic packing](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document1.md)       | Packing without constraints             |
| [Fragility](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document2.md)       | Added Fragility Constraint            |
| [Visualisation](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document3.md)       | Visualising the packing            |
| [Demo codes](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document4.md)       |  Demo codes for execution of codes             |
| [Flask Server](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document5.md)       | Flask Server for backend API             |
| [Input generation](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document6.md)       | Input generation codes             |

## Introduction
This documentation contains an exhaustive overview of the project and setting up the codes for 3d packing with visualisation. This documentation shall provide a comprehensive explanation to all codes and shall help in to proceed with future work as well. The whole project is present inside the directory named packing.

## Installation Guide
It contains the necessary installation of the software require to run the code. To see the step by step installation of the softwares pleas click the link provided in the tables of contents. [Installation Guide](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document7.md)

## Basic Packing
Basic packing involves placing items inside a container efficiently. Given the dimensions of the container and the dimensions of the items, the code will provide the coordinates for each item, showing how and where to place them inside the container for optimal space utilization. We need to consider constraints such as the weight constraint, ensuring the total weight does not exceed the container's maximum capacity, and the no overlapping constraint, which prevents any two items from overlapping. To view the code explanation, please click the link provided in the table of contents. [Basic packing](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document1.md) 

## Fragility
In addition to normal packing. In this code we have implemented an addition constraint to the packing of items i.e. fragility of the items. It helps in the prevention of damage to delicate items by not placing heavier object above them. Here we have defined fragility as the maximum weight an item can withstand. To view the code explanation, please click the link provided in the table of contents. [Fragility](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document2.md)  

## Visualisation
This section of the code deals with the visualisation of the output. We tried to depict the output in form of image for clear understanding of the output for the end users. To view the code explanation, please click the link provided in the table of contents. [Visualisation](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document3.md)

## Demo codes
These are provide for the usage of the above codes. In each of the demo code we have mentioned how to import the necesaary libraries and run the code on a sample input. Also how to get the visualisation of the output. To view the code explanation, please click the link provided in the table of contents. [Demo codes](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document4.md)

## Flask Server
We have created a flask server for the request through APIs. By running the flask server we will be able to get the output in the json form without the overhead of running the code in our local machine. As of now the flask server will run in the local machine. But in future we can have a dedicated server for handling such requests.  To view the code explanation, please click the link provided in the table of contents. [Flask Server](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document5.md)        

## Input generation
The folder called Data preprocessing contains all the input generation files. We have codes for generating inputs for both normal packing and fragility constraints. To view the code explanation, please click the link provided in the table of contents. [Input generation](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document6.md)

