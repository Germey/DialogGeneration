import time

from preprocess.iterator import BiTextIterator, TextIterator
from train import FLAGS
from tqdm import tqdm


def main():
    train_set = TextIterator(source='dataset/q1q2/request_1000.txt',
                             source_dict=FLAGS.source_vocabulary,
                             batch_size=128,
                             max_length=FLAGS.max_seq_length,
                             n_words_source=FLAGS.num_encoder_symbols,
                             sort_by_length=FLAGS.sort_by_length
                             )
    train_set.reset()
    processed_length = 0
    for source in train_set.next():
        processed_length += len(source)
        print('Length', len(source), processed_length, source[0])
        time.sleep(1)
    
    train_set.reset()
    
    print('Reset')
    
    for source in train_set.next():
        print('Length', len(source))


if __name__ == '__main__':
    main()
