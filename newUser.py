#!/usr/bin/python3

def getUserByName(Users,Name):
    for user in Users:
        if user["name"] == Name:
            return user
    return None


if __name__ == '__main__':
    import argparse
    from config import pri as pri
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True)
    parser.add_argument("-e", "--email", required=True)
    parser.add_argument("-p", "--pin", required=True)
    parser.add_argument("-y", "--yubikey_id", required=False)
    parser.add_argument("-f", "--force", required=False,action='store_true',help="Recreate the user in case it already exists")
    args = parser.parse_args()

    # Ping host
    if pri.ping():

        # View all orgs
        x = pri.organization.get()

        #print(pri.user.get(org_id=x[0]['id']))
        #exit(0)
        user = getUserByName(pri.user.get(org_id=x[0]['id']),args.name)
        if user is not None and args.force is True:
            pri.user.delete(org_id=x[0]['id'], usr_id=user['id'])
            user = None
        
        if user is None:
            #POST payload
            payload={
                'name': args.name,
                'email': args.email,
                'pin': args.pin,
                'groups': []
            }
            if args.yubikey_id is not None:
                #Add yubikey settings to payload
                payload["auth_type"]="yubico"
                payload["yubico_id"]=args.yubikey_id[:12]

            # Add users to org[0]
            pri.user.post(org_id=x[0]['id'], data=payload)

        # View users id
        q = pri.user.get(org_id=x[0]['id']) 

        # Delete users
        #pri.user.delete(org_id=x[0]['id'], user_id=q[1]['id'])

        # Get user key download link
        print(pri.key.get(org_id=x[0]['id'], usr_id=getUserByName(q,args.name)['id']).content.decode('utf-8'))

