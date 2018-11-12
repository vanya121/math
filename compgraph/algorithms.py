from lib import Graph


def split_word(stroka):
    import re
    words = re.sub("[^\w]", " ", stroka["text"]).lower().split()
    for word in words:
        yield {'doc_id': stroka['doc_id'], 'text': word}


def count_word(stroks):
    yield {'count': len(stroks), 'text': stroks[0]['text']}


def sum_docs_folder(state, stroka):
    state['docs_count'] += 1
    return state


def unic_word(strocs):
    yield strocs[0]


def reducer_idf(strocs):
    import math
    yield {'text': strocs[0]['text'], 'idf': math.log10(strocs[0]['docs_count'] / len(strocs))}


def reducer_tf(records):
    from collections import Counter
    word_count = Counter()
    total = 0
    for r in records:
        word_count[r['text']] += 1
        total += 1
    for w, count in word_count.items():
        yield {
            'doc_id': r['doc_id'],
            'text': w,
            'tf': count / total
        }


def top_three_tf_idf_word_reducer(strocs):
    top_three_idf = []
    min = 0
    for item in strocs:
        if item['tf']*item['idf'] > min:
            if len(top_three_idf) == 3:
                top_three_idf.pop()
            top_three_idf.append({'text': item['text'], 'doc_id': item['doc_id'], 'tf_idf': item['tf']*item['idf']})
            from operator import itemgetter
            top_three_idf.sort(key=itemgetter('tf_idf'), reverse=True)
    yield from top_three_idf



def build_word_count_graph(input_stream, text_column='text', count_column='count'):
    gwc = Graph.Graph()
    gwc.add_name(input_stream)
    gwc.add_map(mapper=split_word)
    gwc.add_sort(key=('text', 'doc_id'))
    gwc.add_reduce(key=('text',), reducer=count_word)
    gwc.add_sort(key=('count',))
    return gwc


def build_inverted_index_graph(input_stream, doc_column='doc_id', text_column='text'):
    split_word_g = Graph.Graph()
    split_word_g.add_name(input_stream)
    split_word_g.add_map(split_word)
    count_docs = Graph.Graph()
    count_docs.add_name(input_stream)
    count_docs.add_fold(state={'docs_count': 0}, folder=sum_docs_folder)
    count_idf = Graph.Graph()
    count_idf.add_name(input_stream, split_word_g, count_docs)
    count_idf.add_sort(key=('doc_id', 'text'))
    count_idf.add_reduce(key=('doc_id', 'text'), reducer=unic_word)
    count_idf.add_join(key=(), joined_g=count_docs, type='outer')
    count_idf.add_sort(key=('text',))
    count_idf.add_reduce(key=('text',), reducer=reducer_idf)
    calc_index = Graph.Graph()
    calc_index.add_name(input_stream, split_word_g, count_idf)
    calc_index.add_sort(key=('doc_id',))
    calc_index.add_reduce(key=('doc_id',), reducer=reducer_tf)
    calc_index.add_join(key=('text', 'text'), joined_g=count_idf, type='left')
    calc_index.add_sort(key=('text',))
    calc_index.add_reduce(key=('text',), reducer=top_three_tf_idf_word_reducer)
    return calc_index


def build_pmi_graph(input_stream, doc_column='doc_id', text_column='text'):
    pass


def build_yandex_maps_graph(input_stream, input_stream_length):
    pass
