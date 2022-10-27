# Pritunl API client for Python 3

This is a simple api client written in Python 3. View example in
example.py.
Python 2 is not supported. You need to refer Pritunl api doc to get the
idea on how to use this.

Basically this api client use almost same command like in the doc.
For example:

## Examples

* Example 1

  [(in doc)](https://pritunl.com/api.html) `GET /server`

  (this) `api.server.get()`

* Example 2

  [(in doc)](https://pritunl.com/api.html) `PUT /server/:server_id/organization/:organization_id`

  (this) `api.server.put(srv_id='', org_id='')`

* Example 3

  [(in doc)](https://pritunl.com/api.html) `DELETE /user/:organization_id/:user_id`

  (this) `api.user.delete(org_id='', usr_id='')`

* Example 4

  [(in doc)](https://pritunl.com/api.html) `POST /server**`

  (this) `api.server.post(data={
   'name': 'new server name'})`

   \* _If there is data available, you must pass it through data parameter._

   \* _Command above works well because there are template available for
   creating a new server._

* Example 5

  [(in doc)](https://pritunl.com/api.html) `PUT /user/:organization_id/:user_id`

  (this) `api.user.put(org_id='', usr_id='', data={
   'name': 'modified org name',
   'disabled': True})`


## Installation

```sh
export GITHUB_HANDLER = "<maintainer username>"
pip install git+https://github.com/${GITHUB_HANDLER}/pritunl-api-python.git@master#egg=pritunl-api

```
### TODO 
To be replaced with simple `pip install pritunl-api` if the the main author published it to PyPi.

***
This api client is not fully complete. There are some features missing,
feel free to fork and pull request to add new features.

Tested working on **Pritunl 1.26.1188.41**.
