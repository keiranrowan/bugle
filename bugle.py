import pdfkit
import jinja2
import json
import argparse


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

    load = jinja2.FileSystemLoader(searchpath="./templates/")
    templateEnv = jinja2.Environment(loader=load)
    TEMPLATE = args.template + '.rpt'
    template = templateEnv.get_template(TEMPLATE)
    with open('data/' + args.data + '.json') as f:
        data = json.load(f)
        tempargs = {}
        for index in data:
            for param in index:
                tempargs[param] = index[param]
                if args.verbose:
                    print(index[param])
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
    
    
if __name__ == "__main__":
    main()
