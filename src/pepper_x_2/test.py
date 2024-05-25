import subprocess

# Open a subprocess and capture its output
process = subprocess.Popen(['dir'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)

# Read the output of the command in real-time
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip(), flush=True)

# Wait for the subprocess to complete and get its return code
rc = process.poll()

# Read any remaining output
while True:
    output = process.stdout.readline()
    if output == '':
        break
    print(output.strip(), flush=True)

# Close the subprocess
process.stdout.close()
process.stderr.close()