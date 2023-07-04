from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import PPLInferencer
from opencompass.openicl.icl_evaluator import AccEvaluator
from opencompass.datasets import HFDataset

cmnli_reader_cfg = dict(
    input_columns=['sentence1', 'sentence2'],
    output_column='label',
    test_split='train')

cmnli_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template={
            'contradiction':
            '{sentence1}\nKeeping in mind the above text, consider: {sentence2}？\nIs this "always", "sometimes", or "never" correct? [MASK]never',
            'entailment':
            '{sentence1}\nKeeping in mind the above text, consider: {sentence2}？\nIs this "always", "sometimes", or "never" correct? [MASK]always',
            'neutral':
            '{sentence1}\nKeeping in mind the above text, consider: {sentence2}？\nIs this "always", "sometimes", or "never" correct? [MASK]sometimes'
        }),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=PPLInferencer))

cmnli_eval_cfg = dict(evaluator=dict(type=AccEvaluator))

cmnli_datasets = [
    dict(
        type=HFDataset,
        abbr='cmnli',
        path='json',
        split='train',
        data_files='./data/CLUE/cmnli/cmnli_public/dev.json',
        reader_cfg=cmnli_reader_cfg,
        infer_cfg=cmnli_infer_cfg,
        eval_cfg=cmnli_eval_cfg)
]
