class MultiDimensionalRename(object):
    """
    This file is part of the MAXWELL software.
    https://doi.org/10.1038/s41598-022-13377-w
    
    File author(s): Sierra Dean <ccnd@live.com>
    
    Distributed under the GPLv3 Licence.
    See accompanying file LICENSE.txt or copy at
        http://www.gnu.org/licenses/gpl-3.0.html
        
    source: https://github.com/SierraD/MAXWELL
    
    Last Updated: July 10 2024
    """
    
    def __init__(self, path):
        """
        A technique to rename a stack of ordered images to include the positional 
        information of two changing dimensions. 
        
        Attributes:
        path: 
            The operating system path to the folder containing the files to be renamed.
            This must be formatted with an r before the path.
            Example: r"C:\\Users\\User\\Desktop\\Folder"
                    Please change \\ to \ for the actual path.
 
        Return:
            None.
        """
        
        self.path = path
        return 
    
    def Rename(self, sample_name="Sample", deg=0, Z_Num=10, X_Num=31):
        """
        A technique to rename the images to include the desired information.
        
        Attributes:
            sample_name: The desired sample information to be included in the naming.
            deg: The degree of rotation of the data, generally 0 or 90.
            Z_Num: The number of unique Z steps in the stack.
            X_Num: The number of Grating X steps per unique Z step.
            
        Return:
            None. Will rename the individual files.
        """
        
        if (Z_Num * X_Num) != len(os.listdir(self.path)):
            raise Exception("The number of images must be a multiple of the number of Z steps by the number of grating steps.")
        for file_name in os.listdir(self.path):
            if file_name[0] != "a":
                raise Exception("The file "+str(file_name)+" does not follow the general naming convention. Please remove and begin again")
            if ".tif" and "a" in file_name:
                old_name = file_name
                if "a000" in old_name:
                    new_name = file_name.replace("a000", "a_")
                elif "a00" in old_name:
                    new_name = file_name.replace("a00", "a_")
                elif "a0" in old_name:
                    new_name = file_name.replace("a0", "a_")
                elif "a" in old_name:
                    new_name = file_name.replace("a", "a_")
                os.rename(self.path+"\\"+old_name, self.path+"\\"+new_name)
        Z_count = 1
        X_count = 1
        for i in range(1, len(os.listdir(self.path))+1):
            old_name = "a_"+str(i)+".tif"
            new_name = sample_name+"_"+str(deg)+"Deg_"+"ZStep"+str(Z_count)+"_GratingX"+str(X_count)+".tif"
            X_count += 1
            if X_count == (X_Num+1):
                X_count = 1
                Z_count += 1
            os.rename(self.path+"\\"+old_name, self.path+"\\"+new_name)
        return 