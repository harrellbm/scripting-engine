import argparse
import requests
import requests
from requests.exceptions import HTTPError

#TODO: add command to start up DKron server
#TODO: add subfunctions to add update job, delete job, get job status, and get server status.
#TODO: use click to build the commandline user interface

def main():
    args = process_arguments_argparse()
    print("These are our arguments", args)
    

    # Define Job for Dkron API
    url = "https://example.com/createOrUpdateJob"
    query_params = {"runoncreate": True}
    request_body = {
        "name": "job1",
        "displayname": "Job 1",
        "schedule": "@daily",
        "timezone": "UTC",
        "owner": "John Doe",
        "owner_email": "john@example.com",
        "disabled": False,
        "tags": {"team": "dev", "project": "xyz"},
        "metadata": {"description": "Daily job for data processing"},
        "retries": 3,
        "parent_job": None,
        "processors": {},
        "concurrency": "allow",
        "executor": "shell",
        "executor_config": {"command": "echo 'Hello World'"},
    }

    try:
        # Making the API call
        response = post_to_API(url, query_params, request_body)
    
        # Handling successful response
        if response.status_code == 201:
            print("Job created or updated successfully!")
            print("Job details:")
            print(response.json())
        else:
            print(f"Unexpected status code: {response.status_code}")
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")


def process_arguments_argparse():
    """
    Process command line arguments using argparse.

    Args:
        None

    Returns:
        Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description='Command line tool')
    parser.add_argument('action', choices=['action1', 'action2'], help='Specify the action to perform')
    parser.add_argument('argument', type=int, help='Specify an argument')
    args = parser.parse_args()
    return args


def create_or_update_job(job_data, run_on_create=False):
    """
    Send a POST request to the API endpoint to create or update a job.

    Args:
        job_data (dict): A dictionary containing the job data.
        run_on_create (bool, optional): If True, the job will be run immediately after creation/update.

    Returns:
        dict: The response data from the API.
    """
    url = "https://api.example.com/jobs"
    params = {"runoncreate": run_on_create}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=job_data, params=params, headers=headers)

    return response.json()


def send_http_request(url, method="POST", headers=None, query_params=None, json_content=None):

    if method.upper() not in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS']:
        raise ValueError("Invalid HTTP method")

    response = None
    if method.upper() == 'GET':
        response = requests.get(url, params=query_params, headers=headers)
    elif method.upper() == 'POST':
        response = requests.post(url, json=json_content, params=query_params, headers=headers)
    elif method.upper() == 'PUT':
        response = requests.put(url, json=json_content, params=query_params, headers=headers)
    elif method.upper() == 'DELETE':
        response = requests.delete(url, params=query_params, headers=headers)
    elif method.upper() == 'PATCH':
        response = requests.patch(url, json=json_content, params=query_params, headers=headers)
    elif method.upper() == 'HEAD':
        response = requests.head(url, params=query_params,headers=headers)
    elif method.upper() == 'OPTIONS':
        response = requests.options(url, params=query_params, headers=headers)

    response.raise_for_status()  # Raise an exception for non-2xx status codes
    
    if response:
        return response.json()
    else:
        return None

# Example usage:
# Replace the URL with the API endpoint you want to test
url = 'https://api.example.com/resource'
response = send_http_request('GET', url)
print(response)

# You can also specify data and headers if required:
# data = {'key': 'value'}
# headers = {'Authorization': 'Bearer <token>'}
# response = send_http_request('POST', url, data=data, headers=headers)


# Execute the main function if this script is executed directly
if __name__ == "__main__":
    main()