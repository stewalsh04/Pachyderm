'''
Example of how to upload a file to Pachyderm, using the Python plugin.
Note the file must be read in using a binary format, i.e with the 'rb' flag
'''

import python_pachyderm

client = python_pachyderm.Client()
client.create_repo("urls")

with client.commit('urls', "master") as c:
    with open('/home/intern/urls.txt', "rb") as f:
        client.put_file_bytes(c, 'urls', f)
