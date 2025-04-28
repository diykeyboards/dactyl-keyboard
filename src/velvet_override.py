    ############################################
    ## Overrides for Velvet "Thin Wall" Cases ##
    ############################################

shape_config = {
    
    'centercol':  1,  # controls left_right tilt / tenting (higher number is more tenting)
    'centerrow_offset':  2.5,  # rows from max, controls front_back tilt
    'tenting_angle':  pi / 18.0,  # or, change this for more precise tenting control

    'reduced_outer_cols': 1,


    'thumb_offsets':  [6, -1, -1],
    'keyboard_z_offset':  (
        6  # controls overall height# original=9 with centercol=3# use 16 for centercol=2
    ),


    'extra_width': 2,  # extra space between the base of keys# original= 2
    'extra_height': 0.5,  # original= 0.5


    'web_thickness': 3 + 1.1,
    'minidox_Usize': 1.2,

    'wall_z_offset':  2,  # length of the first downward_sloping part of the wall
    'wall_x_offset':  2,  # offset in the x and/or y direction for the first downward_sloping part of the wall (negative)
    'wall_y_offset':  2,  # offset in the x and/or y direction for the first downward_sloping part of the wall (negative)
    'left_wall_x_offset':  0,  # specific values for the left side due to the minimal wall.
    'left_wall_z_offset':  0,  # specific values for the left side due to the minimal wall.
    'left_wall_lower_x_offset': 0,  # specific values for the lower left corner.
    'left_wall_lower_y_offset': 0,  # specific values for the lower left corner.
    'left_wall_lower_z_offset': 0,
    'wall_thickness':  2,  # wall thickness parameter used on upper/mid stage of the wall
    'wall_base_y_thickness':  2,  # wall thickness at the lower stage
    'wall_base_x_thickness':  2,  # wall thickness at the lower stage

    'wall_base_back_thickness':  2,  # wall thickness at the lower stage in the specifically in back for interface.

   ###################################
    ## PCB Screw Mount               ##
    ###################################
    "pcb_mount_ref_offset": [0.5, -5, 0],
    "pcb_holder_size": [34.6, 0.1, 3],
    "pcb_holder_offset": [9.9, 3, 0],

    "pcb_usb_hole_size": [9.3, 10.0, 4.5],
    "pcb_usb_hole_offset": [16.5, 0, 4.5],
    "pcb_usb_hole_z_offset": 2.5,

    "support_planck_size": [33, 7, 2],

    "wall_thinner_size": [41, 5.5, 15],

    "trrs_hole_size": [3, 20],
    "trrs_offset": [0, 0, 7], #left
    #"trrs_offset": [1, 0, 7], #right

    "pcb_screw_hole_size": [.7, 5],
    "pcb_screw_hole_cap_size": [1, 1],

    "pcb_screw_x_offsets": [- 4.5, 8.75, 23], # for the screw positions off of reference
    "pcb_screw_y_offset": -1.5,


    ###################################
    ## HOLES ON PLATE FOR PCB MOUNT
    ###################################
    'plate_holes':  True,
    'plate_holes_xy_offset': (0.0, 0.0),
    'plate_holes_width': 14.3,
    'plate_holes_height': 14.3,
    'plate_holes_diameter': 1.3,
    'plate_holes_depth': 4.0,

    ###################################
    ## COLUMN OFFSETS
    ####################################

    'column_offsets':  [
        [0, 0, 3],
        [0, 0, 3],
        [0, 2.82, 1],
        [0, 0, 2],
        [0, -9, 3],# REDUCED STAGGER
        [0, -9, 5],# REDUCED STAGGER
        [0, -6, 5],# NOT USED IN MOST FORMATS (7th column)
    ],

}
