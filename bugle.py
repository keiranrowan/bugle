import pdfkit
import jinja2
import json
import argparse
import matplotlib.pyplot as plt


def main():
    # Initialize STDIN Args
    parser = argparse.ArgumentParser(description='Generate Custom Reports from Templates')
    parser.add_argument('template', help='Report template to render')
    parser.add_argument('data', help='Report data to parse')
    parser.add_argument('output', help='Name of generated report')
    parser.add_argument('-v', '--verbose', action='store_true', help='Output additional data at runtime')
    args = parser.parse_args()

    if args.verbose:
        print(args.template)
        print(args.data)

    # Generate Assets
    with open('data/' + args.data + '.json') as f:
        data = json.load(f)[0]
        assets = []
        i = 0
        if 'graphs' in data:
            for graph in data['graphs']:
                print(list(graph)[0])
                createGraph(data['graphs'][graph], graph)
                assets.append(graph)
                i += 1

    # Compile Template
    load = jinja2.FileSystemLoader(searchpath="./templates/")
    templateEnv = jinja2.Environment(loader=load)
    TEMPLATE = args.template + '.rpt'
    template = templateEnv.get_template(TEMPLATE)
    with open('data/' + args.data + '.json') as f:
        data = json.load(f)[0]
        tempargs = {}
        tempargs['assets'] = './assets'

        # Load Asset Variables
        for item in assets:
            tempargs[item] = item
            if args.verbose:
                print(item)

        # Load Variables
        for index in data:
            tempargs[index] = data[index]
            if args.verbose:
                print(data[index])
        output = template.render(tempargs)
        outputHTML(args, output)
    f.close()

    outputPDF(args)


def outputHTML(args, output):
    html_file = open('reports/html/' + args.output + '.html', 'w')
    html_file.write(output)
    html_file.close()


def outputPDF(args):
    pdfkit.from_file('reports/html/' + args.output + '.html', 'reports/pdf/' + args.output + '.pdf')


def createGraph(data, name):
    if data['type'] == 'bar':
        title = data['title']
        xindex = data['x']
        yindex = data['y']
        xlabel = data['x-label']
        ylabel = data['y-label']

        chart = plt.figure()
        axis = chart.add_axes([0, 0, 1, 1])
        x = data[xindex]
        y = data[yindex]
        axis.bar(x, y)
        axis.set_title(title)
        axis.set_xlabel(xlabel)
        axis.set_ylabel(ylabel)
        chart.savefig('./reports/html/assets/' + name + '.png', dpi=600, bbox_inches='tight')
    elif data['type'] == 'line':
        title = data['title']
        lines = []
        labels = []
        for line in data['lines']:
            labels.append(line)
            lines.append(data[data['lines'][line]])

        print(lines)
        print(labels)
        xindex = data['x']
        xlabel = data['x-label']
        ylabel = data['y-label']

        chart = plt.figure()
        axis = chart.add_axes([0, 0, 1, 1])
        x = data[xindex]
        i = 0

        for line in lines:
            axis.plot(x, lines[i], label=labels[i])
            i += 1
        axis.set_title(title)
        axis.set_xlabel(xlabel)
        axis.set_ylabel(ylabel)
        chart.savefig('./reports/html/assets/' + name + '.png', dpi=600, bbox_inches='tight')
  #  elif data['type'] == 'histogram':

    
if __name__ == "__main__":
    main()
