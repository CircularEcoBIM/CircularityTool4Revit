# CircularityTool4Revit

**Enabling a Circular Construction model with BIM based tools**

The Circular EcoBIM project aims to create a set of BIM based tools to enable a circular construction model. The three tools that are proposed will help architects and building managers to improve the environmental performance and increase the amount of reused, recovered and recycled construction materials.

Read more at https://circularecobim.eu/

# Instructions 

## Prerequisites:
- Revit 2022+
- Revit model prepared
- MS Excel
- this tool package. This can be done by cloning or downloading it as .zip from the GitHub repository: https://github.com/CircularEcoBIM/CircularityTool4Revit

    <img src="https://user-images.githubusercontent.com/22922395/188671413-b859f36d-6270-4614-8726-6d9ce0f7b889.png" alt="drawing" width="300"/>

## Preparing the data 

### 1.	Add a shared parameter file to the Revit project
- Go to `Insert/Insert from File/Insert Views from File`

    <img src="https://user-images.githubusercontent.com/22922395/188668340-e1054290-333c-4f04-b141-241dad926040.png" alt="drawing" width="500"/>    
-	Point to the template/RevitParameterTemplate.rvt file.
-	Select all three schedules from that file.
    
    <img src="https://user-images.githubusercontent.com/22922395/188679958-febc5294-6a84-49d9-9e19-6950cfd3dee9.png" alt="drawing" width="500"/>    
-	A schedule (table) will appear, but you can close that tab and go back to the desired 3d view.

Now all the required Revit categories in your model will have appropriate parameters.

### 2.	Fill in the parameter values with your project data:
-	Is internal – to mark the external walls (default: Yes)
-	Design for Disassembly parameters - if an element has multiple connections with others, select the parameter that describes the worst of the connections (the higher number, the worse):
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

### 3. Open the desired 3D view for visualization. Make sure it is in ‘Shaded’ or ‘Consistent Colors’ mode, as only those display colours.  You can change the display mode on the bottom-left bar in Revit.

<img src="https://user-images.githubusercontent.com/22922395/188670432-7e9b7fdd-b4e3-4986-8c23-ff5ae7a846dd.png" alt="drawing" width="250"/>

### 4. Make sure that your Revit model doesn’t contain Model Groups as they deny access to write back values of individual element parameters.

Grops are not preventing the tool from working, but all elements belonging to a group will be omitted in the calculations. You can ungroup existing groups by selecting them and using `Ungroup`

<img src="https://user-images.githubusercontent.com/22922395/188673574-04a0d1f6-c612-484b-bde6-433fd1d9fb1c.png" alt="drawing" width="250"/>

## Using the tool

### 5. In Revit, open Dynamo Player:

<img src="https://user-images.githubusercontent.com/22922395/188670575-05b20dea-81aa-464f-aa59-dc46e1804c8f.png" alt="drawing" width="600"/>

<img src="https://user-images.githubusercontent.com/22922395/188670587-276174c5-166a-49f8-88d1-3fa494e78d5e.png" alt="drawing" width="250"/>

Before running each script you can edit the input values by clicking on Edit inputs:

<img src="https://user-images.githubusercontent.com/22922395/188670637-90d616a3-502d-4873-8b1a-f3d8a4c5dfba.png" alt="drawing" width="200"/>

Scripts are based on 4 types of data: 
-	Revit model parameters
-	Inputs from the GUI
-	Hardcoded values in the script
-	External files from the JSON files from /data folder

Once ready press play button on the Dynamo Player to run the script:  
<img src="https://user-images.githubusercontent.com/22922395/188670751-f9a35fcf-e4d4-46aa-b0aa-6b34f9e1985f.png" alt="drawing" width="30"/>

The result, depending on the script, are written back to dedicated Revit parameters, exported to a predefined Excel file or visualized with colors in active Revit view.

### 6. Run the script `1_AssignLayer`

<img src="https://user-images.githubusercontent.com/22922395/188679095-702dcf8a-7784-4286-bde4-a6c48e8fb800.png" alt="drawing" width="300"/>

By default, the script will preview the assignment with colors, for example:

<img src="https://user-images.githubusercontent.com/22922395/190914271-1c20da65-afb8-4499-8225-c52b2097118a.png" alt="drawing" width="450"/>

and the colors correspond to layers:

<img src="https://user-images.githubusercontent.com/22922395/190913976-4aabc63a-c218-49a0-9406-6b7f6be7f675.png" alt="drawing" width="500"/>
* Only those three layers are included in the calculations.


### 7. Run the script `2_MeasureCircularity` 

<img src="https://user-images.githubusercontent.com/22922395/188701345-3a697810-3d51-446e-af14-afd2c78edd8b.png" alt="drawing" width="300"/>

Those are examplar results of running the circularity calculations tool:

<img src="https://user-images.githubusercontent.com/22922395/188701679-a06b6dcc-5337-4385-a3eb-e2c2a61c2b6c.png" alt="drawing" width="450"/>

The tool will create an Excel file in the choosen directory, and it will contain 3 tabs: MCI results, PCI results and one with general results.

The `OriginalMaterial` and `Material` columns in MCI tab show the material name mapping that is based on the predefined mapping pattern available here: 
https://github.com/CircularEcoBIM/CircularityTool4Revit/blob/main/data/Material_mapping.json
If some materials are not found please change Revit material names to the one that is present on the mapping pattern. If some materials are missing please contact the authors or suggest Pull Reqest to the mapping file on GitHub.

Example of a correct Excel export:  

<img src="https://user-images.githubusercontent.com/22922395/188704350-8bc03e1b-c29f-40f5-b6f2-5644628c31d5.png" alt="drawing" width="1100"/>  
<img src="https://user-images.githubusercontent.com/22922395/188704114-2627bf10-9e35-4693-a56d-e80874eff25e.png" alt="drawing" width="700"/>  
<!-- <img src="https://user-images.githubusercontent.com/22922395/188703974-5394e3a6-8772-47e5-99a9-ae589e77cdc5.png" alt="drawing" width="1100"/> -->
<img src="https://user-images.githubusercontent.com/22922395/190928035-23cff713-4d92-4468-82ed-881f5cd73055.png" alt="drawing" width="1100"/>

### 8. Run the script `3_VisualizeResults`

<img src="https://user-images.githubusercontent.com/22922395/188700900-96468c68-c0a3-452c-8112-779dd41ff79c.png" alt="drawing" width="200"/>

Colors represent result ranges as shown below:

<img src="https://user-images.githubusercontent.com/22922395/190914335-d61bb3a7-bd38-40dc-9338-75b9a7d4e60c.png" alt="drawing" width="400"/>

This is the example how the results could look, where top floor is most and bottom least circular:

<img src="https://user-images.githubusercontent.com/22922395/188701190-16f88e14-49bd-4e72-b35f-f1a52ef30b30.png" alt="drawing" width="300"/>

# Disclaimer
The authors of this code reserve the right to track usage statistics, such as IP and city of the user for research purposes. Another data collected is the list of unique material names in user project, for the purpose of improving the material matching algorithm in the future. Please have that in mind and do not use if you do not want to share your IP, location or project contains confidential material names. Administrators for this service reserve the right to moderate all information used, shared, or stored with this service at any time. 

The material embodied in this software is provided to you "as-is" and without warranty of any kind, express, implied or otherwise, including without limitation, any warranty of fitness for a particular purpose. 

# Contact
In case of questions, please contact Artur Tomczak - artomczak@gmail.com

