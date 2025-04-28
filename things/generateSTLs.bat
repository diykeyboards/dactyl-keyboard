@echo off
SetLocal EnableDelayedExpansion

echo -----------------------------------------
echo --== PROCESSING FILES IN THIS FOLDER ==--
echo -----------------------------------------
echo .                 
echo ....%cd%\	        

FOR %%f in (*.scad)  DO (

echo -----------------------------------------
echo ---------- PROCESSING NEXT FILE --------- ... !time! ... 
echo -----------------------------------------
echo .  
echo         %%~nf.scad
echo .  
echo _________________________________________
openscad -o "%%~nf.stl" "%%f"
echo .

)

echo                 ...BATCH COMPLETED        ... !time! ... 

pause

EndLocal