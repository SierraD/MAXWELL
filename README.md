# About MAXWELL
https://doi.org/10.1038/s41598-022-13377-w

MAXWELL (Microscopy by Achromatic X-rays With Emission of Laminar Light) is a tandem use X-ray/visible light microscopy technique designed and implemented at BL29XU at the RIKEN SPring-8 Center, Japan. This repository contains several scripts, primarily in Python and Java, which are intended to be used for experimentation and analysis on output from the MAXWELL microscopy system. 

## Instructions for MAXWELL_MultiDimensionalRename: 
> [!WARNING]  
> I RECOMMEND DOING THIS ONLY FOR COPIED DATA AND NOT THE ORIGINAL, AS THERE IS NO UNDO.

> [!IMPORTANT]  
> Must have Python, Anaconda powershell, or Jupyter Notebook, etc installed.

- Download MAXWELL_MultiDimensionalRename.py from Github
- Open python command line
- cd into the folder containing the downloaded file
- Type "python" to open the python environment
- Type the following then click enter:
  - ```ruby
    from MAXWELL_MultiDimensionalRename import Rename
    ```
- Type the following then click enter: (The path should be the path to your stack. It is important to include the r outside of the quotation marks)
  - ```ruby
    a = Rename(r"C:\Users\User\Desktop\Folder")
    ```
- Type the following then click enter: (Please change the name and numbers to reflect the data)
  - ```ruby
    a.Execute(sample_name="YourSample", deg=0, Z_Num=10, X_Num=31)
    ```
     
Finished. Check the folder to ensure the name was changed correctly.

## Instructions for MAXWELL_StructuredStack:

> [!IMPORTANT]  
> Must have ImageJ or Fiji installed

- Download MAXWELL_StructuredStack.ijm from Github
- (In ImageJ) File -> Import -> Image Sequence -> Select your data
- Plugins -> Macros -> Run -> Select MAXWELL_StructuredStack.ijm
- Imput all information from your stack


Finished. Check the data. <br />
<br />
MAXWELL Software developed by Sierra Dean @ RIKEN SPring-8 Center (JAPAN) 2024 <br />
Email: ccnd@live.com
