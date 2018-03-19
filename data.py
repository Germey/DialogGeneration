from preprocess.iterator import BiTextIterator, TextIterator
from train import FLAGS


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
    train_set.reset()
    
    for source, target in train_set.next():
        print('Length', len(source), len(target))
    
    train_set.reset()
    
    print('Reset')
    
    for source, target in train_set.next():
        print('Length', len(source), len(target))


if __name__ == '__main__':
    main()
