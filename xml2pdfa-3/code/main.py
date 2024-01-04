# importing necessary files
from latexcontent import *
from xmlparser import *
import subprocess
def main():
    # Creating objects for the class
    xml_parser = XMLParser()
    latex_generator = LatexGenerator()

    # XML and XSD Paths used for the files
    xml_file_path = r"C:\Users\soham\OneDrive\Desktop\new final folder\attachment.xml"
    xsd_file_path = r"C:\Users\soham\OneDrive\Desktop\new final folder\dcc.xsd"

    # Validation and XML parsing
    validation_result = xml_parser.validate_xml(xml_file_path, xsd_file_path)
    if validation_result:
        latex_content = latex_generator.generate_latex_content()
    # Write LaTeX content to a file or do further processing as needed
        with open("output.tex", "w") as file:
            file.write(latex_content)
    else:
        print("Validation failed. Cannot proceed further.")

    # Use current date and time for the pdf name
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_pdf = f'CSIR_{current_datetime}.pdf'
    subprocess.run(['pdflatex', '-jobname=' + output_pdf, "output.tex"])

if __name__ == "__main__":
    main()
