import csv


def parse_file(src, tgt):
    with open(tgt, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['label', 'model', 'method', 'dimension', 'lr', 'ws', 'epoch', 'p', 'r', 'f1'])
#        return '{}-{}-t_precision-{}-t_recall-{}-t_f1-{}-d_precision-{}-d_recall-{}-d_f1-{}\n'.format(

        for line in open(src):
            dash_split = line.split('-')
            print(list(enumerate(dash_split)))
            # label = dash_split[0]
            # model = dash_split[1].split('/')[-1]
            # method = dash_split[2]
            # dimenson = int(dash_split[3])
            # lr = float(dash_split[4])
            # ws = int(dash_split[5])
            # epoch = int(dash_split[6].split('_')[0])
            # p, r, f1 = float(dash_split[8]), float(dash_split[10]), float(dash_split[12].strip())
            # writer.writerow([label, model, method, dimenson, lr, ws, epoch, p, r, f1])
