for f in *.scad; do openscad -o ${f/scad/stl} $f; done
