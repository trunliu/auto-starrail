import cv2

import test
from basic.img import cv2_utils
from basic.img.os import get_debug_image
from sr.context import get_context
from sryolo.detector import draw_detections


class DebugDetector(test.SrTestBase):

    def __init__(self, *args, **kwargs):
        test.SrTestBase.__init__(self, *args, **kwargs)

    def test_debug_image(self):
        ctx = get_context()
        ctx.init_yolo_detector()

        img = get_debug_image('2')
        results = ctx.yolo_detector.sim_uni_yolo.detect(img, conf=0.7,
                                                        cates=['界面提示被锁定', '界面提示可攻击'])
        cv2_utils.show_image(draw_detections(results), wait=0)
        cv2.destroyAllWindows()
