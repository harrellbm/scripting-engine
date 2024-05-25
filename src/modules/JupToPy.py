import sys
import jupytext
import nbformat

def convert(path, name):
    print('Converting Notebook to pure Python')
    
    # Read the Jupyter notebook into a Python object
    flpath = path + '/' + name
    with open(f'{flpath}.ipynb') as f:
        nb = nbformat.read(f, as_version=4)

    # Create a new function
    new_cells = []
    new_cells.append(nbformat.v4.new_code_cell(f'def run(data):'))

    # Copy the code from each code cell into the function
    for cell in nb.cells:
        if cell.cell_type == 'code':
            code = cell.source
            code = code.replace('\n', '\n    ')
            new_cells.append(nbformat.v4.new_code_cell(f'    {code}'))

    # Add the final return statement to the function
    new_cells.append(nbformat.v4.new_code_cell('    return result'))

    # Replace the original cells with the new cells in the function
    nb.cells = new_cells
    
    # Write the Jupyter notebook to a Python script
    jupytext.write(nb, f"{flpath}.py")
    print("Convertion complete!") 

if __name__ == "__main__":
    name = sys.argv[1]
    path = sys.argv[2]
    convert(path, name)