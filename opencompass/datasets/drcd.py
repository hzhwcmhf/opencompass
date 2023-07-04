import json

from datasets import Dataset

from opencompass.registry import LOAD_DATASET

from .base import BaseDataset


@LOAD_DATASET.register_module()
class DRCDDataset(BaseDataset):

    @staticmethod
    def load(path: str):
        with open(path) as f:
            data = json.load(f)
        # 将原始数据转换为所需的格式
        rows = []
        for index, paragraphs in enumerate(data['data']):
            for paragraph in paragraphs['paragraphs']:

                context = paragraph['context']

                for question in paragraph['qas']:
                    answers = question['answers']
                    unique_answers = list(set([a['text'] for a in answers]))
                    rows.append({
                        'context': context,
                        'question': question['question'],
                        'answers': unique_answers
                    })

        # 创建 Dataset
        dataset = Dataset.from_dict({
            'context': [row['context'] for row in rows],
            'question': [row['question'] for row in rows],
            'answers': [row['answers'] for row in rows]
        })

        return dataset
