import subprocess
import os
import types
import re

class sql_connect():
        def __init__(self,ora_userid,ora_passwd,ora_sid,ora_proj,ora_role=None):
                self.ora_user=ora_userid
                self.ora_pwd=ora_passwd
                self.ora_sid=ora_sid
                self.ora_proj=ora_proj
                if type(ora_role) == types.TupleType:
                        self.role_name,self.role_pwd=ora_role
                else:
                        self.role_name = None

        def conn(self,ora_query):
                connt_sid = " %s/%s@%s "% (self.ora_user,self.ora_pwd,self.ora_sid)
                error = re.compile('(ORA-)\d+')
                sql_conn = subprocess.Popen(['sqlplus','-S',connt_sid], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                sql_conn.stdin.write(self.ora_proj)
                if self.role_name:
                        sql_conn.stdin.write('\n set role '+self.role_name+' identified by '+self.role_pwd+';')

                sql_conn.stdin.write('\n whenever sqlerror exit 2;')
                sql_conn.stdin.write('\n set feedback off;')
                sql_conn.stdin.write('\n set head off;')
                sql_conn.stdin.write('\n set pages 0;')
                sql_conn.stdin.write("\n set null '0';")
                sql_conn.stdin.write("\n set colsep '|';")
                sql_conn.stdin.write('\n set lines 1000;')
                sql_conn.stdin.write("\n select 'PYTHONSTRINGSEPSTARTSHERE' from dual;")
                sql_conn.stdin.write("\n "+ora_query+";")
                out,err=sql_conn.communicate('\n exit;')
                if sql_conn.returncode == 0 and not error.search(out):
                        return out.split("PYTHONSTRINGSEPSTARTSHERE")[-1]
                else:
                        return None
