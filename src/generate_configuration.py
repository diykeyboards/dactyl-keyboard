import sys
import getopt
import os
import json

pi = 3.14159
d2r = pi / 180
r2d = 180 / pi


#################################
## BEGIN CONFIGURATION SECTION ##
#################################

shape_config = {

    # Emable Output of Test Models
    'test':  False, # If true, test models are rendered.

    # Enable Quick Rendering
    'quick_render':  True, # If true, only right main case is rendered.

    # Choose an engine for model generation.
    # 'ENGINE': 'solid',  # Solid Python / OpenSCAD
    'ENGINE': 'cadquery',  # CadQuery / OpenCascade


    ##############################
    ## Shape Parameters
    ##############################

    'save_dir': '', # Specify a custom save directory/path.
    'config_name': '', # Specify a custom config file name. Default is 'run_config.json'.
    'save_name': '', # Specify the output file name for your models.
    'overrides': '', # Specify a file containing config overrides.

    'ncols':  7, #6,  # Number of key columns
    'nrows':  5, #5,  # Number of key rows

    'alpha':  pi / 12.0,  # Curvature of the columns
    'beta':  pi / 36.0,  # Curvature of the rows

    'centercol':  3,  # Controls left_right tilt/tenting. (Higher number is more tenting.)
    'centerrow_offset':  3,  # Controls front/back tilt. (Higher number is more tilt.)
    'tenting_angle':  pi / 12.0,  # More precise tenting control.

    # Specify the column style. Options are:
    # "STANDARD" = Standard keyboard layout, with vertical offset between columns
    # "ORTHOGRAPHIC"
    # "FIXED"
    'column_style':  'STANDARD',  # options include :standard, :orthographic, and :fixed

    'thumb_offsets':  [6, -3, 7],
    'full_last_rows': False, # If True, will generate the bottom key(s) in the outside columns.
    'keyboard_z_offset': 10,  # Controls overall height


    'extra_width': 2.5,  # extra space between the base of keys# original= 2
    'extra_height': 0.8,  # original= 0.5


    'web_thickness': 4.0 + 1.1,
    'post_size': 0.1,
    # post_adj':  post_size / 2
    'post_adj': 0,

    ##############################
    # Experimental Parameters
    ##############################
    'pinky_1_5U': False,  # LEAVE AS FALSE, CURRENTLY BROKEN
    'first_1_5U_row': 0,
    'last_1_5U_row': 5,
    ##############################


    'extra_width':  2.7,  # Adds horizontal space between columns. Default = 2.
    'extra_height':  0,  # Adds vertical space between keys in a column. Default = 0.5

    'wall_z_offset':  15,  # length of the first downward_sloping part of the wall
    'wall_x_offset':  5,  # offset in the x and/or y direction for the first downward_sloping part of the wall (negative)
    'wall_y_offset':  6,  # offset in the x and/or y direction for the first downward_sloping part of the wall (negative)
    'left_wall_x_offset':  12,  # specific values for the left side due to the minimal wall.
    'left_wall_z_offset':  3,  # specific values for the left side due to the minimal wall.
    'left_wall_lower_y_offset': 0,  # specific values for the lower left corner.
    'left_wall_lower_z_offset': 0,
    'wall_thickness':  4.5,  # wall thickness parameter used on upper/mid stage of the wall
    'wall_base_y_thickness':  4.5,  # wall thickness at the lower stage
    'wall_base_x_thickness':  4.5,  # wall thickness at the lower stage

    'wall_base_back_thickness':  4.5,  # wall thickness at the lower stage in the specifically in back for interface.

    ## Settings for column_style == :fixed
    ## The defaults roughly matcFplh Maltron settings
    ##   http://patentimages.storage.googleapis.com/EP0219944A2/imgf0002.png
    ## fixed_z overrides the z portion of the column ofsets above.
    ## NOTE: THIS DOESN'T WORK QUITE LIKE I'D HOPED.
    'fixed_angles':  [d2r * 10, d2r * 10, 0, 0, 0, d2r * -15, d2r * -15],
    'fixed_x':  [-41.5, -22.5, 0, 20.3, 41.4, 65.5, 89.6],  # relative to the middle finger
    'fixed_z':  [12.1, 8.3, 0, 5, 10.7, 14.5, 17.5],
    'fixed_tenting':  d2r * 0,


    ###################################
    ## Switch Holes
    ###################################

    # A number of different styles of switch opening are available, as follows:
    # 'HOLE' = A simple square opening.
    # 'NUB' and 'HS-NUB' = Adds small side nubs to left and right of switch opening.
    # 'UNDERCUT' and 'HS-UNDERCUT' = Snap-fit undercut lip around the entire switch opening.
    # 'NOTCH' and 'HS-NOTCH'= Snap-fit undercut only near switch clip.

    # Versions with 'HS-' feature integrated Kailh hotswap socket mounts.
    # Tweak CLIP_THICKNESS/CLIP_UNDERCUT to perfect snap-fit on 'UNDERCUT', 'HS-UNDERCUT', 'NOTCH' and 'HS-NOTCH'

    'plate_style': 'NOTCH', # 'NOTCH' and 'HS-NOTCH' are recommended.
    'plate_thickness': 5, # Thickness of the switch plate. 5mm allows flush-mount of Amoeba PCBs.
    'plate_rim': 2 + 0.5, # Thickness of rim around switch opening.

    'hole_keyswitch_height':  14.0, # Height of key switch opening
    'hole_keyswitch_width':  14.0, # Width of key switch opening

    # NUB Style-Specific Dimensions
    'nub_keyswitch_height':  14.4, # Height of key switch opening
    'nub_keyswitch_width':  14.4, # Width of key switch opening

    # UNDERCUT/NOTCH Style-Specific Dimensions
    'undercut_keyswitch_height':  14.0, # Height of key switch opening
    'undercut_keyswitch_width':  14.0, # Width of key switch opening
    'clip_thickness':  1.4, # Depth of rim from switch mount surface
    'clip_undercut':  1.0, # Depth of undercut
    'notch_width': 6.0, # Width of cut for NOTCH styles.
    'undercut_transition':  0.2,  # Adds chamfer to undercut.Only works with Cadquery engine.

    # Hotswap / Custom Plate File Options
    'plate_file_name':  "diyk_hot_swap_plate_v2", # Custom hot swap plate STEP file. Place file in '/src/parts'.
    'plate_offset': -1, # Raise or lower plate relative to switch opening.
    'plate_thickness_hotswap':  7, # Thickness of main plate when using custom plate file.


    ##############################
    # Thumb Parameters
    ##############################
    # 'DEFAULT' 6-key, 'MINI' 5-key, 'CARBONFET' 6-key, 'MINIDOX' 3-key, 'VELVET' 2-key,
    #'TRACKBALL_ORBYL', 'TRACKBALL_CJ', 'TRACKBALL_WILD', 'TRACKBALL_BTU'
    'thumb_style': 'TRACKBALL_BTU',
    'default_1U_cluster': True, # only used with default, makes top right thumb cluster key 1U
    # Thumb key size.  May need slight oversizing, check w/ caps.  Additional spacing will be automatically added for larger keys.
    'minidox_Usize': 1.6,
    # Thumb plate rotations, anything other than 90 degree increments WILL NOT WORK.

    'mini_index_key': True,

    # Screw locations and extra screw locations for separable thumb, all from thumb origin
    # Pulled out of hardcoding as drastic changes to the geometry may require fixes to the screw mounts.
    # First screw in separable should be similar to the standard location as it will receive the same modifiers.
    'default_thumb_screw_xy_locations': [[-21, -58]],
    'default_separable_thumb_screw_xy_locations': [[-21, -58]],
    'mini_thumb_screw_xy_locations': [[-29, -52]],
    'mini_separable_thumb_screw_xy_locations': [[-29, -52], [-62, 10], [12, -25]],
    'minidox_thumb_screw_xy_locations': [[-37, -34]],
    'minidox_separable_thumb_screw_xy_locations': [[-37, -34], [-62, 12], [10, -25]],
    'carbonfet_thumb_screw_xy_locations': [[-48, -37]],
    'carbonfet_separable_thumb_screw_xy_locations': [[-48, -37], [-52, 10], [12, -35]],
    'orbyl_thumb_screw_xy_locations': [[-53, -68]],
    'orbyl_separable_thumb_screw_xy_locations': [[-53, -68], [-66, 8], [10, -40]],
    'tbcj_thumb_screw_xy_locations': [[-40, -75]],
    'tbcj_separable_thumb_screw_xy_locations': [[-40, -75], [-63, 10], [15, -40]],

    'thumb_plate_tr_rotation': 0.0,  # Top right plate rotation tweaks as thumb cluster is crowded for hot swap, etc.
    'thumb_plate_tl_rotation': 0.0,  # Top left plate rotation tweaks as thumb cluster is crowded for hot swap, etc.
    'thumb_plate_mr_rotation': 0.0,  # Mid right plate rotation tweaks as thumb cluster is crowded for hot swap, etc.
    'thumb_plate_ml_rotation': 0.0,  # Mid left plate rotation tweaks as thumb cluster is crowded for hot swap, etc.
    'thumb_plate_br_rotation': 0.0,  # Bottom right plate rotation tweaks as thumb cluster is crowded for hot swap, etc.
    'thumb_plate_bl_rotation': 0.0,  # Bottom right plate rotation tweaks as thumb cluster is crowded for hot swap, etc.
    ##############################
    # EXPERIMENTAL
    'separable_thumb': False,  #creates a separable thumb section with additional screws to hold it down.  Only attached at base.
    ##############################


    ###################################
    ## Trackball General
    ###################################
    # EXPERIMENTAL
    'trackball_modular': False, # May add removable trackball in subsequent releases, no current use.
    # END EXPERIMENTAL

    'trackball_Usize': 1.5,  # size for inner key near trackball
    'ball_side': 'right', #'left', 'right', or 'both'
    'other_thumb': '', # Cluster used for second thumb except if ball_side == 'both'
    'ball_diameter': 34.0,
    'ball_wall_thickness': 3,  # should not be changed unless the import models are changed.
    'ball_gap': 1.0,
    'trackball_hole_diameter': 36.5,
    'trackball_hole_height': 40,
    'trackball_plate_thickness': 2,
    'trackball_plate_width': 2,
    'tb_socket_translation_offset': (0, 0, 2.0),  # applied to the socket and sensor, large values will cause web/wall issues.
    'tb_socket_rotation_offset':    (0, 0, 0),  # applied to the socket and sensor, large values will cause web/wall issues.
    'tb_sensor_translation_offset': (0, 0, 0),  #deviation from socket offsets, for fixing generated geometry issues
    'tb_sensor_rotation_offset':    (0, 0, 0),  #deviation from socket offsets, for changing the sensor roll orientation
    'tb_cutter_translation_offset': (0, 0, 0),  # Applied to the cutting model (cylinder) used to cut socket hole in cluster, large values will cause web/wall issues.
    'tb_cutter_rotation_offset':    (0, 0, 0),  # Applied to the cutting model (cylinder) used to cut socket hole in cluster, large values will cause web/wall issues.
    'get_extras': False, # Generate support posts under trackball socket.


    ###################################
    ## Trackball in Wall
    ###################################
    'trackball_in_wall': False,  # Separate trackball option, placing it in the OLED area
    'tbiw_ball_center_row': 0.2, # up from cornerrow instead of down from top
    'tbiw_translational_offset': (0.0, 0.0, 0.0),
    'tbiw_rotation_offset': (0.0, 0.0, 0.0),
    'tbiw_left_wall_x_offset_override': 50.0,
    'tbiw_left_wall_z_offset_override': 0.0,
    'tbiw_left_wall_lower_x_offset': 0.0,
    'tbiw_left_wall_lower_y_offset': 0.0,
    'tbiw_left_wall_lower_z_offset': 0.0,

    'tbiw_oled_center_row': .75,  # not none, offsets are from this position
    'tbiw_oled_translation_offset': (-0.5, 0, 1.5),  # Z offset tweaks are expected depending on curvature and OLED mount choice.
    'tbiw_oled_rotation_offset': (0, 0, 0),


    ###################################
    ## Trackball BTU Thumb Cluster
    ###################################
    # Large values on the options below will cause web/wall issues.
    'tb_btu_socket_translation_offset': (3.5, 10, -7),  # Translation offsets applied to the BTU socket and sensor.
    'tb_btu_socket_rotation_offset':    (0, 0, -25),  # Rotation offsets applied to the BTU socket and sensor.
    'tb_btu_cutter_translation_offset': (-1, 0, 0),  # Applied to the cutting model (cylinder) used to cut socket hole in cluster, large values will cause web/wall issues.
    'tb_btu_cutter_rotation_offset':    (0, 0, 0),  # Applied to the cutting model (cylinder) used to cut socket hole in cluster, large values will cause web/wall issues.


    ###################################
    ## Trackball ORBYL Thumb Cluster
    ###################################
    'tbjs_key_diameter': 70,
    'tbjs_Uwidth': 1.2,  # size for inner key near trackball
    'tbjs_Uheight': 1.2,  # size for inner key near trackball

    # Offsets are per key and are applied before rotating into place around the ball
    # X and Y act like Tangential and Radial around the ball
    # 'tbjs_translation_offset': (0, 0, 10),  # applied to the whole assy
    # 'tbjs_rotation_offset': (0, 10, 0),  # applied to the whole assy
    'tbjs_translation_offset': (0, 0, 2),  # applied to the whole assy
    'tbjs_rotation_offset': (0, -8, 0),  # applied to the whole assy
    'tbjs_key_translation_offsets': [
        (0.0, 0.0, -3.0-5),
        (0.0, 0.0, -3.0-5),
        (0.0, 0.0, -3.0-5),
        (0.0, 0.0, -3.0-5),
    ],
    'tbjs_key_rotation_offsets': [
        (0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
    ],

    ###################################
    ## Trackball CJ Thumb Cluster
    ###################################
    'tbcj_inner_diameter': 42,
    'tbcj_thickness': 2,
    'tbcj_outer_diameter': 53,


    ###################################
    ## OLED Screen Mount
    ###################################

    # A number of different styles of switch opening are available, as follows:
    # 'NONE' = No OLED mount
    # 'UNDERCUT' = Simple rectangle with undercut for clip in item
    # 'SLIDING' = Features to slide the OLED in place and use a pin or block to secure from underneath.
    # 'CLIP' = Features to set the OLED in a frame a snap a bezel down to hold it in place.

    'oled_mount_type':  'NONE',
    'oled_center_row': 1.25, # if not None, this will override the oled_mount_location_xyz and oled_mount_rotation_xyz settings
    'oled_translation_offset': (0, 0, 4), # Z offset tweaks are expected depending on curvature and OLED mount choice.
    'oled_rotation_offset': (0, 0, 0),

    'oled_configurations': {
        'UNDERCUT':{
            # Common parameters
            'oled_mount_width': 15.0,
            'oled_mount_height': 35.0,
            'oled_mount_rim': 3.0,
            'oled_mount_depth': 6.0,
            'oled_mount_cut_depth': 20.0,
            'oled_mount_location_xyz': (-80.0, 20.0, 45.0), # will be overwritten if oled_center_row is not None
            'oled_mount_rotation_xyz': (13.0, 0.0, -6.0), # will be overwritten if oled_center_row is not None
            'oled_left_wall_x_offset_override': 28.0,
            'oled_left_wall_z_offset_override': 0.0,
            'oled_left_wall_lower_y_offset': 12.0,
            'oled_left_wall_lower_z_offset': 5.0,

            # 'UNDERCUT' Parameters
            'oled_mount_undercut': 1.0,
            'oled_mount_undercut_thickness': 2.0,
        },
        'SLIDING': {
            # Common parameters
            'oled_mount_width': 12.5,  # width of OLED, plus clearance
            'oled_mount_height': 25.0,  # length of screen
            'oled_mount_rim': 2.5,
            'oled_mount_depth': 8.0,
            'oled_mount_cut_depth': 20.0,
            'oled_mount_location_xyz': (-78.0, 10.0, 41.0), # will be overwritten if oled_center_row is not None
            'oled_mount_rotation_xyz': (6.0, 0.0, -3.0), # will be overwritten if oled_center_row is not None
            'oled_left_wall_x_offset_override': 24.0,
            'oled_left_wall_z_offset_override': 0.0,
            'oled_left_wall_lower_y_offset': 12.0,
            'oled_left_wall_lower_z_offset': 5.0,

            # 'SLIDING' Parameters
            'oled_thickness': 4.2,  # thickness of OLED, plus clearance.  Must include components
            'oled_edge_overlap_end': 6.5,  # length from end of viewable screen to end of PCB
            'oled_edge_overlap_connector': 5.5,  # length from end of viewable screen to end of PCB on connection side.
            'oled_edge_overlap_thickness': 2.5,  # thickness of material over edge of PCB
            'oled_edge_overlap_clearance': 2.5,  # Clearance to insert PCB before laying down and sliding.
            'oled_edge_chamfer': 2.0,
        },
        'CLIP': {
            # Common parameters
            'oled_mount_width': 12.5,  # whole OLED width
            'oled_mount_height': 39.0,  # whole OLED length
            'oled_mount_rim': 2.0,
            'oled_mount_depth': 7.0,
            'oled_mount_cut_depth': 20.0,
            'oled_mount_location_xyz': (-78.0, 20.0, 42.0), # will be overwritten if oled_center_row is not None
            'oled_mount_rotation_xyz': (12.0, 0.0, -6.0), # will be overwritten if oled_center_row is not None
            'oled_left_wall_x_offset_override': 24.0,
            'oled_left_wall_z_offset_override': 0.0,
            'oled_left_wall_lower_y_offset': 12.0,
            'oled_left_wall_lower_z_offset': 5.0,

            # 'CLIP' Parameters
            'oled_thickness': 4.2,  # thickness of OLED, plus clearance.  Must include components
            'oled_mount_bezel_thickness': 3.5,  # z thickness of clip bezel
            'oled_mount_bezel_chamfer': 2.0,  # depth of the 45 degree chamfer
            'oled_mount_connector_hole': 6.0,
            'oled_screen_start_from_conn_end': 6.5,
            'oled_screen_length': 24.5,
            'oled_screen_width': 10.5,
            'oled_clip_thickness': 1.5,
            'oled_clip_width': 6.0,
            'oled_clip_overhang': 1.0,
            'oled_clip_extension': 5.0,
            'oled_clip_width_clearance': 0.5,
            'oled_clip_undercut': 0.5,
            'oled_clip_undercut_thickness': 2.5,
            'oled_clip_y_gap': .2,
            'oled_clip_z_gap': .2,
        }
    },
    'post_size':  0.1,
    # post_adj':  post_size / 2
    'post_adj':  0,
    'screws_offset': 'INSIDE', #'OUTSIDE', 'INSIDE', 'ORIGINAL'

    'screw_insert_height': 4.5,
    'screw_insert_bottom_radius': 4.8 / 2,
    'screw_insert_top_radius': 4.6 / 2,

    'screw_insert_height': 4.5,

    'screw_insert_bottom_radius': 4.8 / 2,  #Designed for inserts
    'screw_insert_top_radius': 4.6 / 2,  #Designed for inserts

    # 'screw_insert_bottom_radius': 2.5 / 2,  # Designed for self tapping
    # 'screw_insert_top_radius': 2.5 / 2,  # Designed for self tapping

    'screw_insert_outer_radius': 4.25,  # Common to keep interface to base

    # Does anyone even use these?  I think they just get in the way.
    'wire_post_height': 7,
    'wire_post_overhang': 3.5,
    'wire_post_diameter': 2.6,


    ###################################
    ## SA Keycap / PCB Models
    ###################################

    # Use the SA keycap option to check clearances when making major edits to column/row/switch spacing.
    'show_caps': False,
    'sa_profile_key_height':  10, # Height of generated SA keycaps. Default is 12.7
    'sa_length': 18.5, # Width of generated 1u SA keycaps
    'sa_double_length': 37.5, # Height of generated 2u SA keycaps
    'show_pcbs': False, # Only runs if keycaps are shown.


    ###################################
    ## Controller Mount / Connectors
    ###################################
    # connector options are
    # 'RJ9_USB_WALL' = Standard internal plate with RJ9 opening and square cutout for connection.
    # 'USB_WALL' = Standard internal plate with a square cutout for connection, no RJ9.
    # 'RJ9_USB_TEENSY' = Teensy holder
    # 'USB_TEENSY' = Teensy holder, no RJ9
    # 'EXTERNAL' = square cutout for a holder such as the one from lolligagger.
    # 'BLACKPILL_EXTERNAL' = larger square cutout for lolligagger type holder modified for the blackpill.
    # 'NONE' = No openings in the back.
    'controller_mount_type':  'EXTERNAL',

    'external_holder_height':  12.5,
    'external_holder_width':  28.75,
    'external_holder_xoffset': -5.0,
    'external_holder_yoffset': -4.5, #Tweak this value to get the right undercut for the tray engagement.

    # Offset is from the top inner corner of the top inner key.

    ##### BLACKPILL EXTERNAL HOLDER
    ## To use, set
    "blackpill_holder_width": 32.0,
    "blackpill_holder_xoffset": -6.5,


    ###################################
    ## PCB Screw Mount               ##
    ###################################
    "pcb_mount_ref_offset": [0, -5, 0],
    "pcb_holder_size": [34.6, 7, 4],
    "pcb_holder_offset": [8.9, 0, 0],

    "pcb_usb_hole_size": [7.5, 10.0, 4],
    "pcb_usb_hole_offset": [15, 0, 4.5],

    "wall_thinner_size": [34, 7, 10],

    "trrs_hole_size": [3, 20],
    "trrs_offset": [0, 0, 1.5],

    "pcb_screw_hole_size": [.5, 10],
    "pcb_screw_x_offsets": [- 5.5, 7.75, 22], # for the screw positions off of reference
    "pcb_screw_y_offset": -2,


    ###################################
    ## Bottom Plate Dimensions
    ###################################
    'screw_hole_diameter': 3,
    # USED FOR CADQUERY ONLY
    'base_thickness': 3, # thickness in the middle of the plate
    'base_offset': 3, # Both start flat/flush on the bottom.  This offsets the base up (if positive)
    'base_rim_thickness': 3.0,  # thickness on the outer frame with screws
    'screw_cbore_diameter': 5.8,
    'screw_cbore_depth': 2.0, # Depth of counterbore. Must not be equal or greater than 'base_rim_thickness'.
    'screw_cbore_style':  'COUNTERSINK',# 'COUNTERSINK' (conical) or 'COUNTERBORE' (cylindrical)


    ###################################
    ## Bottom Plate Logo
    ###################################
    'logo_file':  'None', #Logo STEP file name. Logo should be extruded 1mm high. Origin should be in center. Leave empty for none.
    'logo_plates':  'RIGHT', #LEFT, RIGHT, or BOTH
    'logo_offsets': [-50, 5, -1],
    # Offset is from the top inner corner of the top inner key.


    ###################################
    ## Hole on Plate for PCB Mount
    ###################################
    'plate_holes':  False,
    'plate_holes_xy_offset': (0.0, 0.0),
    'plate_holes_width': 14.3,
    'plate_holes_height': 14.3,
    'plate_holes_diameter': 1.7,
    'plate_holes_depth': 20.0,


    ###################################
    ## Show PCB for Fit Check
    ###################################
    'pcb_width': 18.0,
    'pcb_height': 18.0,
    'pcb_thickness': 1.5,
    'pcb_hole_diameter': 2,
    'pcb_hole_pattern_width': 14.3,
    'pcb_hole_pattern_height': 14.3,


    ###################################
    ## Column Offsets
    ####################################

    'column_offsets':  [
        [0, 0, 0],
        [0, 0, 0],
        [0, 2.82, -4.5],
        [0, 0, 0],
        [0, -6, 5],# REDUCED STAGGER
        [0, -6, 5],# REDUCED STAGGER
        [0, -6, 5],# NOT USED IN MOST FORMATS (7th column)
        [0, -6, 5],# NOT USED IN MOST FORMATS (8th column)
        [0, -6, 5],# NOT USED IN MOST FORMATS (9th column)
    ],


    ###################################
    ## Screw Hole Offsets
    ####################################
    # Changes position of screw bosses (x,y,z)
    "screw_offsets": [
        [0, 0, 0],     # First Column Top
        [0, -2, 0],   # First Column Bottom
        [0, 0, 0],     # Center Column Top
        [0, -2, 0],    # Center Column Bottom
        [-1, -12, 0],     # Last Column Top
        [-1.5, 12, 0],     # Last Column Bottom
        [0, 0, 0],     # Thumb Cluster
    ],
}

    ####################################
    ## END CONFIGURATION SECTION
    ####################################

def save_config():
    # Check to see if the user has specified an alternate config
    opts, args = getopt.getopt(sys.argv[1:], "", ["config=", "update="])
    got_opts = False
    for opt, arg in opts:
        if opt in ('--update'):
            with open(os.path.join(r"..", "configs", arg + '.json'), mode='r') as fid:
                data = json.load(fid)
                shape_config.update(data)
            got_opts = True

    for opt, arg in opts:
        if opt in ('--config'):
            # If a config file was specified, set the config_name and save_dir
            shape_config['save_dir'] = arg
            shape_config['config_name'] = arg
            got_opts = True

    # Write the config to ./configs/<config_name>.json
    if got_opts:
        with open(os.path.join(r"..", "configs", shape_config['config_name'] + '.json'), mode='w') as fid:
            json.dump(shape_config, fid, indent=4)

    else:
        with open(os.path.join(r".", 'run_config.json'), mode='w') as fid:
            json.dump(shape_config, fid, indent=4)


if __name__ == '__main__':
    save_config()
