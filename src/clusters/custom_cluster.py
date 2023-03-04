from clusters.default_cluster import DefaultCluster
import json
import os

class CustomCluster(DefaultCluster):

    @staticmethod
    def name():
        return "CUSTOM"

    def get_config(self):
        with open(os.path.join(r"..", "src", "clusters", "json", "CUSTOM.json"), mode='r') as fid:
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
        self.num_keys = 7
        super().__init__(parent_locals)
        # have to repeat this for all classes/namespaces
        for item in parent_locals:
            globals()[item] = parent_locals[item]

    def tl_place(self, shape):
        debugprint('tl_place()')
        shape = rotate(shape, [9.5, -12, 10])
        shape = translate(shape, self.thumborigin())
        shape = translate(shape, [-32.5, -17.5, -2.5])
        return shape

    def tr_place(self, shape):
        debugprint('tr_place()')
        shape = rotate(shape, [10, -9, 10])
        shape = translate(shape, self.thumborigin())
        shape = translate(shape, [-12, -16, 1])
        return shape

    def mr_place(self, shape):
        debugprint('mr_place()')
        shape = rotate(shape, [-6, -28, 48])
        shape = translate(shape, self.thumborigin())
        shape = translate(shape, [-29, -40, -9])
        return shape

    def ml_place(self, shape):
        debugprint('ml_place()')
        shape = rotate(shape, [6, -28, 45])
        shape = translate(shape, self.thumborigin())
        shape = translate(shape, [-49, -27, -8])
        return shape

    def br_place(self, shape):
        debugprint('br_place()')
        shape = rotate(shape, [-16, -27, 54])
        shape = translate(shape, self.thumborigin())
        shape = translate(shape, [-37.8, -55.3, -19.3])
        return shape

    def bl_place(self, shape):
        debugprint('bl_place()')
        shape = rotate(shape, [-4, -29, 52])
        shape = translate(shape, self.thumborigin())
        shape = translate(shape, [-56.3, -43.3, -18.5])
        return shape

    def thumb_1x_layout(self, shape, cap=False):
        debugprint('thumb_1x_layout()')
        if cap:
            shape_list = [
                self.mr_place(rotate(shape, [0, 0, self.thumb_plate_mr_rotation])),
                self.ml_place(rotate(shape, [0, 0, self.thumb_plate_ml_rotation])),
                self.br_place(rotate(shape, [0, 0, self.thumb_plate_br_rotation])),
                self.bl_place(rotate(shape, [0, 0, self.thumb_plate_bl_rotation])),
                self.tr_place(rotate(rotate(shape, (0, 0, 90)), [0, 0, self.thumb_plate_tr_rotation])),
                self.tl_place(rotate(rotate(shape, (0, 0, 90)), [0, 0, self.thumb_plate_tl_rotation]))
            ]

            # if default_1U_cluster:
            #     # shape_list.append(self.tr_place(rotate(rotate(shape, (0, 0, 90)), [0, 0, self.thumb_plate_tr_rotation])))
            #     shape_list.append(self.tr_place(rotate(rotate(shape, (0, 0, 90)), [0, 0, self.thumb_plate_tr_rotation])))
            #     shape_list.append(self.tl_place(rotate(rotate(shape, (0, 0, 90)), [0, 0, self.thumb_plate_tl_rotation])))
            shapes = add(shape_list)

        else:
            shape_list = [
                self.mr_place(rotate(shape, [0, 0, self.thumb_plate_mr_rotation])),
                self.ml_place(rotate(shape, [0, 0, self.thumb_plate_ml_rotation])),
                self.br_place(rotate(shape, [0, 0, self.thumb_plate_br_rotation])),
                self.bl_place(rotate(shape, [0, 0, self.thumb_plate_bl_rotation])),
                self.tr_place(rotate(shape, [0, 0, self.thumb_plate_tr_rotation])),
                self.tl_place(rotate(shape, [0, 0, self.thumb_plate_tl_rotation]))
            ]

            shapes = union(shape_list)
        return shapes

    def thumbcaps(self, side='right'):
        t1 = self.thumb_1x_layout(sa_cap(1), cap=True)
        if not default_1U_cluster:
            t1.add(self.thumb_15x_layout(sa_cap(1), cap=True))
        return t1

    def thumb(self, side="right"):
        print('thumb()')
        shape = self.thumb_1x_layout(rotate(single_plate(side=side), (0, 0, -90)))

        return shape

    def thumb_post_tr(self):
        debugprint('thumb_post_tr()')
        return translate(web_post(),
                         [(mount_width / 2) - post_adj, ((mount_height / 2)) - post_adj, 0]
                         )

    def thumb_post_tl(self):
        debugprint('thumb_post_tl()')
        return translate(web_post(),
                         [-(mount_width / 2) + post_adj, ((mount_height / 2)) - post_adj, 0]
                         )

    def thumb_post_bl(self):
        debugprint('thumb_post_bl()')
        return translate(web_post(),
                         [-(mount_width / 2) + post_adj, -((mount_height / 2)) + post_adj, 0]
                         )

    def thumb_post_br(self):
        debugprint('thumb_post_br()')
        return translate(web_post(),
                         [(mount_width / 2) - post_adj, -((mount_height / 2)) + post_adj, 0]
                         )
