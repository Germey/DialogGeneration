import time

from preprocess.iterator import BiTextIterator, TextIterator
from train import FLAGS
from tqdm import tqdm


def main():
    train_set = BiTextIterator(source='dataset/q1q2/request_1000.txt',
                               target='dataset/q1q2/response_1000.txt',
                               source_dict=FLAGS.source_vocabulary,
                               target_dict=FLAGS.target_vocabulary,
                               batch_size=128,
                               max_length=FLAGS.max_seq_length,
                               n_words_source=FLAGS.num_encoder_symbols,
                               n_words_target=FLAGS.num_decoder_symbols,
                               sort_by_length=FLAGS.sort_by_length
                               )
    with tqdm(total=train_set.length()) as pbar:
        train_set.reset()
        processed_length = 0
        for source, target in train_set.next():
            processed_length += len(source)
            print('Length', len(source), len(target), processed_length)
            time.sleep(5)
            pbar.update(processed_length)
    
    train_set.reset()
    
    print('Reset')
    
    for source, target in train_set.next():
        print('Length', len(source), len(target))


if __name__ == '__main__':
    main()
