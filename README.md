strain-amplitude-volume-fraction
================================
*Craig Bonsignore*

*Nitinol Devives & Components, Inc*

Resources related to strain amplitude volume fraction method for evaluating nitinol fatigue durability.

1. **SMST_2014_Volume_Fraction.pdf** [Stain Amplitude Volume Fraction Method for Evaluation of Nitinol Fatigue Durability](https://asm.confex.com/asm/smst14/webprogram/Paper36277.html) presentation from SMST-2014 explaining the method, using the resources available here.

2. **Step_By_Step_Volume_Fraction.pdf** Detailed explanation of the process used to generate volume fraction data from a set of metallographic cross section images.

3. **Sample_Image.jpg** A sample metallographic cross section. The scale of this image is 500x. 250 pixels = 500 microns.

4. **Results_from_ImageJ_Particle_Analysis.txt** Results exported from ImageJ, after importing Sample_Image.jpg, applying a default threshold setting to isolate inclusions, and applying "analyze particles" to quantify the number of inclusions. ImageJ saves this data with a default extension of .XLS, but the format is actually just a tab deliniated text file.

5. **2014_Sample_Data.jmp** JMP data table containing the sample data from above, plus some additional columns to calculate area, volume, and histogram information. (JMP 10.0 http://jmp.com 30-day trial available)

6. **SMST_2014_data.xlsx** All of the raw data, summary tables, calculations, and charts included in the presentation. Includes both the material analysis, and strain amplitude data from the FEA example.

7. **Abaqus_6.12-1_Example.inp** Abaqus input deck used to generatre the FEA sample data used in the presentation. 

8. **ivol.py** Python script using Abaqus API's to detect and measure regions of the model having a strain amplitude exceeding a specified threshold.

CREDIT
------
Thanks for Payman Saffari, Payam Saffari, Karthik Sentilnathan, Scott Robertson, and Scott Schlegel for their contributions to this research.

LICENSE
-------

These materials are publicly shared under the permissive terms of the MIT license. Suggestions and improvements are welcomed, and attribution is appreciated. Please credit NDC, and link to https://github.com/cbonsig/strain-amplitude-volume-fraction. Please use the "Issues" panel for comments and suggestions [1].

The MIT License (MIT)

Copyright (c) 2013-2014 Nitinol Devices & Components, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

footnotes
---------

[1]: Forks or pull requests are also welcome, if you are weird enough to know what those are.
