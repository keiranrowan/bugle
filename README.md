# Bugle

Bugle is a simple report generator which leverages Jinja2 and Matplotlib to allow you to create fully featured custom reports
including graphics and other assets. The use of JSON for designing data sets allows for many programs to interface data to 
generate reports. Reports are written in standard HTML and CSS and are populated using Jinja's templating system. Bugle is
capable of generating both a dynamic web page report and a printable PDF report. 

### Dependencies

```bash
python 3.0 or later
pdfkit
jinja2
matplotlib
```

### Creating a Simple Report

To create a report you must have data, and that data must have structure. The ```data``` folder is where all JSON data sets are stored. These data sets contain key : value pairs which define variables which will be used in the template. Because JSON can represent many different sets of data, this gives you a lot of freedom when it comes to structuring your data. Below is a sample JSON data file:

##### data/names.json
```json
[
    {
        "title": "Generic Report",
        "rows": {
            "row1": "John",
            "row2": "Jane ",
            "row3": "Joe",
            "row4": "Smith"
        }
    }
]
```

```title```,```header```,```footer```, and ```rows```, are are variables which can be accessed via the template. Each one of these variables can contain a single value, or an array of values, or even more key : value pairs.

Next, we have to create the template. A template is simply an HTML document with templating syntax. Below is a sample template using the variables we defined above:

Note: reports use .rpt as a file extension in order to differentiate them from .html output files.

##### templates/simpleReport.rpt

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{title}}</title>
</head>
<body>
    <h1>{{title}}</h1>

    <ul id="values">
        {% for row in rows %}
            <li><p>{{ rows[row] }}</p></li>
        {% endfor %}
    </ul>
</body>
</html>
```

As you can see, ```{{title}}``` is the variable that we defined eariler which will get replaced on compile time with  ```Generic Report```. To create a list item for all of the rows defined without having to call each one by name, we use the loop structure. In this case, it iterates through each row in rows, and sets the list item value to the value of that row.

### Compiling a Report

Below is the general usage for Bugle. Simply pass it the names (without extension) of the template and data to build and it will generate an HTML file under ```reports/HTML``` and a PDF file under ```reports/PDF```

##### Usage
```
usage: bugle.py [-h] [-v] template data output

Generate Custom Reports from Templates

positional arguments:
  template       Report template to render
  data           Report data to parse
  output         Name of generated report

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Output additional data at runtime
```

### More Examples:


Template | Data | HTML Output | PDF Output
--- | --- | --- | ---
[Chart Report](templates/chartReport.rpt) | [Data](data/stats.json) | [HTML](reports/HTML/chartReport.html) | [PDF](reports/PDF/chartReport.pdf)
[Formatted Report](templates/formattedReport.rpt) | [Data](data/employeeData.json) | [HTML](reports/HTML/formattedReport.html) | [PDF](reports/PDF/formattedReport.pdf)
[Simple Report](templates/simpleReport.rpt) | [Data](data/names.json) | [HTML](reports/HTML/simpleReport.html) | [PDF](reports/PDF/simpleReport.pdf)
