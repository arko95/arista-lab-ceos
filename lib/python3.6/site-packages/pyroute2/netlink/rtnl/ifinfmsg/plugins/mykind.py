from pyroute2.netlink import nla


class mykind(nla):
    prefix = 'IFLA_MYKIND_'
    nla_map = (('IFLA_MYKIND_UNSPEC', 'none'),
               ('IFLA_MYKIND_MYPORT', 'uint32'),
               ('IFLA_MYKIND_MYDEV', 'asciiz'))
