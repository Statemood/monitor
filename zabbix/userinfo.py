#! /usr/bin/env python2

# --------------------------------------------------
# Project monitor
#       https://github.com/Statemood/monitor
#
# A part of the project AMC
#       https://github.com/Statemood/amc
# --------------------------------------------------

import sys
import ldap

LDAP_HOST       = 'auth.abc.com'
LDAP_PORT       = 389
LDAP_BASE_DN    = 'dc=auth,dc=abc,dc=com'

class LDAPSearch:
    def __init__(self):
        self.ldapconn = ldap.open(LDAP_HOST)
        self.ldapconn.simple_bind()
        self.ldap_base_dn = LDAP_BASE_DN

    def usr_search(self, filter=None, attrib=None):
        s = self.ldapconn.search_s(self.ldap_base_dn, ldap.SCOPE_SUBTREE, filter, attrib)

        return s
