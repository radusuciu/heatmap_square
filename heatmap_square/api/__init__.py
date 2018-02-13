from heatmap_square.core.models import User, user_schema
from matplotlib.pyplot import cm
from io import StringIO, BytesIO
import matplotlib
import matplotlib.pyplot as plt
import pathlib
import csv

# matplotlib.use('Agg')
plt.switch_backend('agg')

def get_user_info(user_id):
    return user_schema.dump(User.query.get(user_id)).data

def heatmap(raw):
    data = [x for x in csv.reader(StringIO(raw.strip()), delimiter='\t')]

    # grab header
    x_labels = data[0]

    # consider using partition here
    y_labels = [x[0] for x in data[1:]]
    ratios = [x[1:] for x in data[1:]]
    ratios = [list(map(float, x)) for x in ratios]

    fig = matplotlib.pyplot.gcf()

    ax = plt.subplot(131)
    fig.set_size_inches(8, 8, forward=True)
    im = ax.imshow(ratios, interpolation='nearest', cmap=cm.Blues, aspect='auto', vmin=0, vmax=20)
    cbar = plt.colorbar(im, ax=ax, orientation='horizontal', pad=0.02, ticks=[0, 5, 10, 15, 20])

    cbar.ax.set_ylabel('R', rotation='horizontal', va='center')
    cbar.ax.get_yaxis().set_label_coords(-0.1, 0.35)

    ax.set_yticks(range(len(y_labels)))
    ax.set_yticklabels(y_labels, family='sans-serif', size=10)

    ax.get_xaxis().tick_top()
    plt.xticks(rotation=90)
    ax.set_xticks(range(len(x_labels)))
    ax.set_xticklabels(x_labels)

    plt.tight_layout()

    img_io = BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)


    return img_io
