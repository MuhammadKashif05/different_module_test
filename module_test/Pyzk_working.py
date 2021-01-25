import sys
import traceback
import argparse
import time
import datetime
import codecs
from builtins import input
import os
from zk import ZK, const
from rest_framework.response import Response
from rest_framework.decorators import api_view
from zk import ZK, const
from zk.user import User
from zk.finger import Finger
from zk.attendance import Attendance
from zk.exception import ZKErrorResponse, ZKNetworkError
sys.path.insert(1, os.path.abspath("./pyzk"))


@api_view(['GET'])
def create_user123(request):
    zk = ZK('192.168.10.77', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
    try:
        conn = zk.connect()
        try:
            conn.disable_device()
            print(zk.set_user(32, 'AsadBro', 0, '', '1', '32'))
            # zk.enroll_user('26')
            conn.enable_device()
        except Exception as e:
            print("Process terminate : {}".format(e))

        conn.disable_device()
        return Response({"success": True})
    except Exception as e:
        print(e)
        return Response({"success": True})
