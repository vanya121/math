from lib import Graph


def split_word(stroka):
    words = stroka["text"].lower().split()
    for word in words:
        yield {'doc_id': stroka['doc_id'], 'text': word}


def count_word(stroks):
    yield {'count': len(stroks), 'text': stroks[0]['text']}


if __name__ == "__main__":
    gwc = Graph.Graph()
    gwc.add_name('docs')
    gwc.add_map(mapper=split_word)
    gwc.add_sort(key=('text', 'doc_id'))
    gwc.add_reduce(key=('text',), reducer=count_word)
    gwc.add_sort(key=('count',))
    import json
    result = gwc.run(docs=list(json.loads(line)
                               for line in open("/home/ggg/krutov_i/compgraph/resource/text_corpus.txt", 'r')))
    json.dump(result, open("/home/ggg/krutov_i/compgraph/example/word_count_on_text_corpus.txt", 'w'))
