from xmlparser import XMLParser
xml_parser = XMLParser()
data = xml_parser.parse_xml("attachment.xml")
first_dictionary = data[0]

measuring_result = first_dictionary['measuring_result']
measuring_value_probe = first_dictionary['measuring_value_probe']
measuring_result_error = first_dictionary['measuring_result_error']
next_recalibration_date = first_dictionary['next_recalibration_date']
certificate_number = first_dictionary['certificate_number']
head_cft = first_dictionary['head_cft']
calibrated_by = first_dictionary['calibrated_by']
checked_by = first_dictionary['checked_by']
scientist_incharge = first_dictionary['scientist_incharge']
customer_name = first_dictionary['customer_name']
customer_street = first_dictionary['customer_street']
customer_city = first_dictionary['customer_city']
customer_postal_code = first_dictionary['customer_postal_code']
customer_reference = first_dictionary['customer_reference']
item_name = first_dictionary['item_name']
model_no = first_dictionary['model_no']
serial_no = first_dictionary['serial_no']
temperature = first_dictionary['temperature']
humidity_final = first_dictionary['humidity_final']
equipment_type = first_dictionary['equipment_type']
associated_uncertainity = first_dictionary['associated_uncertainity']
coverage_factor = first_dictionary['coverage_factor']
coverage_probablity = first_dictionary['coverage_probablity']
distribution_type = first_dictionary['distribution_type']
begin_calibration_date = first_dictionary['begin_calibration_date']
end_calibration_date = first_dictionary['end_calibration_date']

class LatexGenerator:
    def __init__(self):
        pass
    # Split the string by spaces
    def change(self, string):
        split_values = string.split()
        processed_values = []
        current = ""

        for val in split_values:
            if val.startswith('\\'):
                current += f" {val}"
            else:
                if current:
                    processed_values.append(current.strip())
                    current = ""
                processed_values.append(val)

        if current:
            processed_values.append(current.strip())

        return processed_values

    def generate_latex_table_with_headline(self, lists):
        num_columns = len(lists)
        num_rows = max(len(lst) for lst in lists)

        headline = ["Nominal Value (in V)", "Measured Value(in V)", "Error(in V)"]

        table = "\\begin{tabular}{|" + "|".join(["c"] * num_columns) + "|}\n"
        table += "\\hline\n"
        
        # Add headline
        table += " & ".join(headline) + " \\\\\n"
        table += "\\hline\n"

        for i in range(num_rows):
            row = [lst[i] if i < len(lst) else '' for lst in lists]
            table += " & ".join(row) + " \\\\\n"
            table += "\\hline\n"

        table += "\\end{tabular}"
        return table


    def generate_latex_content(self):
        measuring_result_list = self.change(measuring_result)
        measuring_value_probe_list = self.change(measuring_value_probe)
        measuring_result_error_list = self.change(measuring_result_error)
        latex_table = self.generate_latex_table_with_headline([measuring_result_list, measuring_value_probe_list, measuring_result_error_list])
            # Accessing XML data and creating LaTeX content...
        latex_content = f'''
        \\documentclass[a4paper]{{article}}

        % Load necessary packages for using Arial-like font
        \\usepackage[a-3u]{{pdfx}}
        \\usepackage{{attachfile}}
        \\usepackage{{geometry}}
        \\usepackage{{fancyhdr}}
        \\usepackage{{graphicx}}
        \\usepackage{{color}}
        \\usepackage{{helvet}}  % Helvetica clone
        \\usepackage{{embedfile}}
        \\usepackage{{tabularx}} % For the tabularx environment
        \\usepackage{{siunitx}}
        \\usepackage{{lastpage}} % For typesetting units
        % Set Arial-like font as the default sans-serif font
        \\renewcommand{{\\familydefault}}{{\\sfdefault}}

        \\fancyhf{{}}
        \\fancyhead[L]{{\\includegraphics[width=0.18\\textwidth,height=25.0mm]{{logo.png}} \\\\[3pt]}}
        \\fancyhead[R]{{
            Date: {{\\today}} \\\\
            Next Calibration Date: {next_recalibration_date} \\\\
            {{Page \\thepage}} \\\\
            Certificate Number: {certificate_number} \\\\[2pt]
        }}
        \\fancyfoot[L]{{
            \\setlength{{\\tabcolsep}}{{1pt}} % Adjusting column separation
                \\begin{{tabularx}}{{\\textwidth}}{{@{{\\extracolsep{{0.001pt}}}} p{{0.1\\textwidth}} X X X X X X X X}}  % Adjusting column widths
                    Head CFT: & & Calibrated By: & & Checked By: & & Scientist incharge: & \\\\
                    & ({head_cft}) & & ({calibrated_by}) & & ({checked_by}) & & ({scientist_incharge}) \\\\
                \\end{{tabularx}}
                \\vspace{{0.1 cm}}
        }} 

        \\setlength{{\\headheight}}{{25mm}}
        \\pagestyle{{fancy}}
        \\renewcommand{{\\headrulewidth}}{{0.8pt}}
        \\renewcommand{{\\footrulewidth}}{{0.8pt}}
        \\renewcommand{{\\familydefault}}{{\\sfdefault}}
        \\newcommand{{\\embedmyfile}}[1]{{\\embedfile{{#1}}}}

        \\begin{{document}}
            \\embedfile{{attachment.xml}}
            \\begin{{center}}
                {{\\fontfamily{{phv}}\\fontsize{{18pt}}{{20pt}}\\selectfont\\textbf{{\\textcolor{{black}}{{\\\\[3pt]Calibration Certificate : {item_name}}}}}}}
            \\end{{center}}
            
            \\vspace{{2cm}}  % Adding some vertical space
            
            \\renewcommand{{\\arraystretch}}{{1.5}} % Increasing row height
            
            \\begin{{center}}
                \\setlength{{\\tabcolsep}}{{12pt}} % Adjusting column separation
                \\begin{{tabularx}}{{\\textwidth}}{{@{{\\extracolsep{{8pt}}}} p{{0.4\\textwidth}} X}}  % Adjusting column widths
                    1. Calibrated for: & {customer_name} \\\\
                    & {customer_street} \\\\
                    & {customer_city} \\\\
                    & {customer_postal_code} \\\\
                    & {customer_reference} \\\\
                    &  \\\\
                    2. Description and Identification of instrument: & {item_name} \\\\
                    & {model_no} \\\\
                    & {serial_no} \\\\
                    & \\\\
                    3. Environmental Conditions:
                    & Temperature: {{{temperature}}} \\\\
                    & Humidity: ({{{humidity_final}}})\\% \\\\ 
                    & \\\\
                    4. Standard(s) Used: & {equipment_type} \\\\
                    Associated Uncertainity: & {associated_uncertainity} \\\\
                    & \\\\
                    5. Traceability of standard(s) used: & {equipment_type} (Primary Standard)\\\\
                    & \\\\
                    6. Principle/ Methodology of Calibration: & The {item_name} has been calibrated by comarison method with {equipment_type} as per calibration procedure no. \\\\
                \\end{{tabularx}}
            \\end{{center}}

            \\pagebreak
            7. Measurements:   \\\\
            \\begin{{center}}
                {latex_table} \\\\
            \\vspace{{0.5 cm}}  
            \\end{{center}}
            The report expanded uncertainity is at a coverage factor k + {coverage_factor} which corresponds approximaltely {coverage_probablity}\% for a {distribution_type} distribution. \\\\
            \\\\

            \\begin{{flushleft}}
                \\setlength{{\\tabcolsep}}{{1pt}} % Adjusting column separation
                \\begin{{tabularx}}{{\\textwidth}}{{@{{\\extracolsep{{8pt}}}} p{{0.4\\textwidth}} X}}  % Adjusting column widths
                    8. Dates of Calibration: & {begin_calibration_date} to {end_calibration_date} \\\\
                    & \\\\
                    9. Remarks: & (i) The {item_name} has been calibrated \\\\
                    & (ii) The noise of the {item_name} is inclusive 
                \\end{{tabularx}}
                \\vspace{{2 cm}}
            \\end{{flushleft}}
        \\end{{document}}
        '''

        return latex_content
