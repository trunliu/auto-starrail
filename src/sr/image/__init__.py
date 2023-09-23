from typing import Union, List

import cv2
import numpy as np

from basic.img import MatchResultList


class ImageMatcher:

    def match_template(self, source: cv2.typing.MatLike, template_id: str, template_type: str = 'origin',
                       threshold: float = 0.5,
                       mask: np.ndarray = None,
                       ignore_inf: bool = True) -> MatchResultList:
        """
        在原图中 匹配模板
        :param source: 原图
        :param template_id: 模板id
        :param template_type: 使用哪种类型模板
        :param threshold: 匹配阈值
        :param mask: 掩码
        :param ignore_inf: 是否忽略无限大的结果
        :return: 所有匹配结果
        """
        pass

    def match_template_with_rotation(self, source: cv2.typing.MatLike, template_id: str,
                                     threshold: float = 0.5,
                                     mask: np.ndarray = None,
                                     ignore_inf: bool = True) -> dict:
        """
        在原图中 对模板进行360度旋转匹配
        :param source: 原图
        :param template_id: 模板id
        :param threshold: 匹配阈值
        :param mask: 掩码
        :param ignore_inf: 是否忽略无限大的结果
        :return: 每个选择角度的匹配结果
        """
        pass


class OcrMatcher:

    def run_ocr(self, image: cv2.typing.MatLike, threshold: float = 0.5) -> dict:
        """
        对图片进行OCR 返回所有匹配结果
        :param image: 图片
        :param threshold: 匹配阈值
        :return: {key_word: []}
        """
        pass

    def match_words(self, image: cv2.typing.MatLike, words: List[str], threshold: float = 0.5) -> dict:
        """
        在图片中查找关键词 返回所有词对应的位置
        :param image: 图片
        :param words: 关键词
        :param threshold: 匹配阈值
        :return: {key_word: []}
        """
        all_match_result: dict = self.run_ocr(image, threshold)
        match_key = set()
        for k in all_match_result.keys():
            for w in words:
                if k.find(w) != -1:
                    match_key.add(k)
                    break

        return {key: all_match_result[key] for key in match_key if key in all_match_result}
