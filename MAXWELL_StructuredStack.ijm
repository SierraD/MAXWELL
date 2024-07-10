// MAXWELL_StructuredStack (ImageJ Macro)
//
// This file is part of the MAXWELL software.
// https://doi.org/10.1038/s41598-022-13377-w
//
// File author(s): Sierra Dean <ccnd@live.com>
//
// Distributed under the GPLv3 License.
// See accompanything file LICENSE.txt or copy at
//       http://www.gnu.org/licenses/gpl-3.0.html
// 
// source: https://github.com/SierraD/MAXWELL
//
// Last Updated: July 10 2024

// A technique to restructure a stack of ordered images open
// in ImageJ to properly visualize the information of two
// changing dimensions.

Dialog.create("Experiment Information");
Dialog.addNumber("Number of unique Z Steps:", "1");
Dialog.addNumber("Number of Grating Steps per unique Z Step:", "1");
Dialog.addString("Z Step distance [nm]:", "1");
Dialog.addNumber("Grating Step distance [nm]:", "1");
Dialog.addString("Pixel Size [nm]:", "1");
Dialog.show();

Z = Dialog.getNumber();
X = Dialog.getNumber();
Z_nm = Dialog.getString();
X_nm = Dialog.getNumber();
Pixel_nm = Dialog.getString();
S = nSlices;

if (X*Z != S) {
	print("The number of images must be a multiple of the number of Z steps by the number of Grating steps.");
} 
else {
	Stack.setDimensions(1, Z, X);
	Stack.setUnits("nm", "nm", "nm", "nm", 1);
	Stack.setFrameInterval(X_nm);
	run("Properties...", "pixel_width="+Pixel_nm);
	run("Properties...", "pixel_height="+Pixel_nm);
	run("Properties...", "voxel_depth="+Z_nm);
	
	run("Stack to Hyperstack...", "order=xyctz");
}