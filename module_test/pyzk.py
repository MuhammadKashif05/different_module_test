import sys
from rest_framework.response import Response
from rest_framework.decorators import api_view
from zk import ZK, const
import os.path
sys.path.insert(1, os.path.abspath("./pyzk"))


@api_view(['GET'])
def machine123(request):
    if request.method == 'GET':
        pass
    conn = None
    zk = ZK('192.168.10.28', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
    try:
        conn = zk.connect()
        conn.disable_device()
        users = conn.get_users()
        print(users)
        print(zk.get_attendance())
        print(conn.get_attendance())
        print('Firmware Version: : {}'.format(conn.get_firmware_version()))
        # print '--- Get User ---'
        users = conn.get_users()
        print(conn.get_users())
        for user in users:
            privilege = 'User'
            if user.privilege == const.USER_ADMIN:
                privilege = 'Admin'
            print('+ UID #{}'.format(user.uid))
            print('  Name       : {}'.format(user.name))
            print('  Privilege  : {}'.format(privilege))
            print('  Password   : {}'.format(user.password))
            print('  Group ID   : {}'.format(user.group_id))
            print('  User  ID   : {}'.format(user.user_id))
        conn.test_voice()
        conn.enable_device()
    except Exception as e:
        print("Process terminate : {}".format(e))
    finally:
        if conn:
            conn.enable_device()
            conn.disconnect()
        return Response({"success": False})
