import itertools
import string

BATCH_SIZE = 2000
LETTERS = string.ascii_lowercase


def generate_domains():
    count = 0
    batch = 1
    buffer = []
    # 2位组合
    for combo in itertools.product(LETTERS, repeat=2):
        domain = ''.join(combo) + '.bio'
        buffer.append(domain)
        count += 1
        if count % BATCH_SIZE == 0:
            with open(f'domains_2_3_batch_{batch}.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(buffer) + '\n')
            buffer = []
            batch += 1
    # 3位组合
    for combo in itertools.product(LETTERS, repeat=3):
        domain = ''.join(combo) + '.bio'
        buffer.append(domain)
        count += 1
        if count % BATCH_SIZE == 0:
            with open(f'domains_2_3_batch_{batch}.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(buffer) + '\n')
            buffer = []
            batch += 1
    # 写入剩余的域名
    if buffer:
        with open(f'domains_2_3_batch_{batch}.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(buffer) + '\n')

if __name__ == '__main__':
    generate_domains() 
