import requests

# SonarQube server URL and API endpoint
sonarqube_url = 'https://sonarqube.iwobble.com'
api_endpoint = '/api'

# API authentication token or username/password
api_token = 'your-api-token'

# Function to make API requests
def make_api_request(endpoint, params=None):
    headers = {'Authorization': f'Bearer {api_token}'} if api_token else None
    response = requests.get(f'{sonarqube_url}{api_endpoint}{endpoint}', params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error {response.status_code}: {response.text}')
        return None

# Get a list of projects
def get_projects():
    projects_endpoint = '/projects/search'
    params = {'format': 'json'}
    return make_api_request(projects_endpoint, params)

# Get project permissions
def get_project_permissions(project_key):
    permissions_endpoint = f'/permissions/search_project_permissions'
    params = {'projectKey': project_key, 'format': 'json'}
    return make_api_request(permissions_endpoint, params)

# Example usage
if __name__ == '__main__':
    # Get and print projects
    projects = get_projects()
    if projects:
        print('Projects:')
        for project in projects['components']:
            print(f'- {project["key"]}')

        # Get and print permissions for the first project (change as needed)
        if projects['components']:
            first_project_key = projects['components'][0]['key']
            permissions = get_project_permissions(first_project_key)
            if permissions:
                print(f'\nPermissions for project {first_project_key}:')
                for permission in permissions['permissions']:
                    print(f'- {permission}')

