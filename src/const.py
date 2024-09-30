import json

senttag2opinion = {'pos': 'great', 'neg': 'bad', 'neu': 'ok'}
sentword2opinion = {'positive': 'great', 'negative': 'bad', 'neutral': 'ok'}

rest_aspect_cate_list = [
    'location general', 'food prices', 'food quality', 'food general',
    'ambience general', 'service general', 'restaurant prices',
    'drinks prices', 'restaurant miscellaneous', 'drinks quality',
    'drinks style_options', 'restaurant general', 'food style_options'
]

with open("force_tokens.json", 'r') as f:
    force_tokens = json.load(f)

cate_list = {
    "rest16": rest_aspect_cate_list,
}

task_data_list = {
    "acos": ["rest16"]
}
force_words = {
    'acos': {
        "rest": rest_aspect_cate_list + list(sentword2opinion.values()) + ['[SSEP]'],
        "laptop": laptop_aspect_cate_list + list(sentword2opinion.values()) + ['[SSEP]'],
    }
}

optim_orders_all = {
            "acos": {
                "rest16": [  # ot null -> sp
                    '[A] [O] [S] [C]', '[A] [O] [C] [S]',
                    '[A] [S] [O] [C]', '[O] [A] [C] [S]',
                    '[O] [A] [S] [C]', '[O] [S] [C] [A]',
                    '[A] [C] [O] [S]', '[O] [C] [A] [S]',
                    '[O] [S] [A] [C]', '[A] [S] [C] [O]',
                    '[A] [C] [S] [O]', '[O] [C] [S] [A]',
                    '[C] [O] [A] [S]', '[C] [A] [O] [S]',
                    '[C] [S] [O] [A]', '[C] [O] [S] [A]',
                    '[S] [A] [O] [C]', '[C] [S] [A] [O]',
                    '[C] [A] [S] [O]', '[S] [O] [A] [C]',
                    '[S] [C] [O] [A]', '[S] [O] [C] [A]',
                    '[S] [C] [A] [O]', '[S] [A] [C] [O]'
                ]
            }
        }

heuristic_orders = {
    'acos': ['[A] [O] [C] [S]'],
}