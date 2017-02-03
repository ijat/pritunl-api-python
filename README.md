# Pritunl API client for Python 3

This is a simple api client written in Python 3. View example in
example.py.
Python 2 is not supported. You need to refer Pritunl api doc to get the
idea on how to use this.

Basically this api client use almost same command like in the doc.
For example:

1. **(in doc) GET /server**

   **(this) api.server.get()**

2. **(in doc) PUT /server/:server_id/organization/:organization_id**

   **(this) api.server.put(srv_id='', org_id='')**

3. **(in doc) DELETE /user/:organization_id/:user_id**

   **(this) api.user.delete(org_id='', usr_id='')**

4. **(in doc) POST /server**

   **(this) api.server.post(data={
   'name': 'new server name'})**

   \* _If there is data available, you must pass it through data parameter._

   \* _Command above works well because there are template available for
   creating a new server._

5. **(in doc) PUT /user/:organization_id/:user_id**

   **(this) api.user.put(org_id='', usr_id='', data={
   'name': 'modified org name',
   'disabled': True})**


This api client is not fully completed. There are some features missing,
feel free to fork and pull request to add new features.

Tested working on Pritunl 1.26.1188.41.

### License

This api client is under GPLv3. please view LICENSE file for more info.
