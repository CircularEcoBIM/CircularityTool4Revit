# CircularityTool4Revit

**Enabling a Circular Construction model with BIM based tools**

The Circular EcoBIM project aims to create a set of BIM based tools to enable a circular construction model. The three tools that are proposed will help architects and building managers to improve the environmental performance and increase the amount of reused, recovered and recycled construction materials.

Read more at https://circularecobim.eu/

## Instructions 

### 1.	Prerequisites:
- Revit 2022+
- Revit model prepared
- this tool package. This can be done by cloning or downloading it from the GitHub repository: https://github.com/CircularEcoBIM/CircularityTool4Revit

    <img src="https://user-images.githubusercontent.com/22922395/188671413-b859f36d-6270-4614-8726-6d9ce0f7b889.png" alt="drawing" width="300"/>

### 2.	Add a shared parameter file to the Revit project
- Go to `Insert/Insert from File/Insert Views from File`

    <img src="https://user-images.githubusercontent.com/22922395/188668340-e1054290-333c-4f04-b141-241dad926040.png" alt="drawing" width="500"/>    
-	Point to the template/RevitParameterTemplate.rvt file.
-	Select all three schedules from that file.
-	A schedule (table) will appear, but you can close that tab and go back to the desired 3d view.

Now all the required Revit categories in your model will have appropriate parameters.

### 3.	Fill in the parameter values with your project data:
-	Is internal – to mark the external walls (default: Yes)
-	Design for Disassembly parameters:
    - Form containment  
      0 - not applicable  
      1 - Open, no inclusions  
      2 - Overlaps on one side  
      3 - Closed on one side  
      4 - Closed on several sides (default)  
    -	Connection accessibility
      0 - not applicable  
      1 - Freely Accessible  
    	2 - Accessibility with additional actions that do not cause damage  
    	3 - Accessibility with additional actions with reparable damage  
    	4 - Not accessible irreparable damage to objects (default)  
    -	Connection type  
    	0 - not applicable  
    	1 - Dry Connection  
    	2 - Connection with added elements  
    	3 - Direct integral connection  
    	4 - Soft chemical compound  
      5 - Hard chemical connection (default)  
    - Crossings  
    	0 - not applicable  
    	1 - Modular zoning of objects  
    	2 - Crossings between one or more objects  
    	3 - Full integration of objects (default)  
-	Source of the material (all are by default zero):
    - Reused material – the percentage of reused material – coming from preowned elements
    - Recycled material – the percentage of recycled material content
    -	Biological material – the percentage of sustainable biological material
-	End-of-life scenario (all are by default zero):
    -	EoL recycling – the percentage of material planned to be recycled
    -	EoL reuse –  the percentage of material planned to be reused

### 4. Open the desired 3D view for visualization. Make sure it is in ‘Shaded’ or ‘Consistent Colors’ mode, as only those display colours.  You can change the display mode on the bottom-left bar in Revit.

<img src="https://user-images.githubusercontent.com/22922395/188670432-7e9b7fdd-b4e3-4986-8c23-ff5ae7a846dd.png" alt="drawing" width="250"/>

### 5. Make sure that your Revit model doesn’t contain Model Groups as they deny access to write back values of individual element parameters.

### 6.	In Revit, open Dynamo Player:

<img src="https://user-images.githubusercontent.com/22922395/188670575-05b20dea-81aa-464f-aa59-dc46e1804c8f.png" alt="drawing" width="600"/>

<img src="https://user-images.githubusercontent.com/22922395/188670587-276174c5-166a-49f8-88d1-3fa494e78d5e.png" alt="drawing" width="250"/>

### 7.	Before running each script you can edit the input values by clicking on Edit inputs:

<img src="https://user-images.githubusercontent.com/22922395/188670637-90d616a3-502d-4873-8b1a-f3d8a4c5dfba.png" alt="drawing" width="200"/>

### 8.	Once ready press play button on the Dynamo Player to run the script:  
<img src="https://user-images.githubusercontent.com/22922395/188670751-f9a35fcf-e4d4-46aa-b0aa-6b34f9e1985f.png" alt="drawing" width="30"/>

Scripts are based on 4 types of data: 
-	Revit model parameters
-	Inputs from the GUI
-	Hardcoded values in the script
-	External files from the JSON files from /data folder

### 9.	The result, depending on the script, are written back to dedicated Revit parameters, exported to a predefined Excel file or visualized with colors in active Revit view.

