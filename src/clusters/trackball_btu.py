from clusters.trackball_wilder import TrackballWild
import json
import os

class TrackballBTU(TrackballWild):

    post_offsets = [
            [14, 0, -2],
            [1, -12, -7],
            [-11, 0, -10],
            [-1, 15, 0]
        ]

    @staticmethod
    def name():
        return "TRACKBALL_BTU"

    def get_config(self):
        with open(os.path.join(r"..", "src", "clusters", "json", "TRACKBALL_WILD.json"), mode='r') as fid:
            data = json.load(fid)

        superdata = super().get_config()

        # overwrite any super variables with this class' needs
        for item in data:
            superdata[item] = data[item]

        for item in superdata:
            if not hasattr(self, str(item)):
                print(self.name() + ": NO MEMBER VARIABLE FOR " + str(item))
                continue
            setattr(self, str(item), superdata[item])

        return superdata

    def __init__(self, parent_locals):
        super().__init__(parent_locals)
        for item in parent_locals:
            globals()[item] = parent_locals[item]

    def has_btus(self):
        return True

    def get_extras(self, shape, pos):
        posts = [shape]
        all_pos = []
        for i in range(len(pos)):
            all_pos.append(pos[i] + tb_socket_translation_offset[i])
        z_pos = abs(pos[2])
        for post_offset in self.post_offsets:
            support_z = z_pos + post_offset[2]
            new_offsets = post_offset.copy()
            new_offsets[2] = -z_pos
            support = cylinder(1.5, support_z, 10)
            support = translate(support, all_pos)
            support = translate(support, new_offsets)
            base = cylinder(4, 1, 10)
            new_offsets[2] = 0.5 - all_pos[2]
            base = translate(base, all_pos)
            base = translate(base, new_offsets)
            posts.append(base)
            support = union([support, base])
            posts.append(support)
        return union(posts)
