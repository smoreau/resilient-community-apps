<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Example: LDAP Utilities: Add User(s) to Group(s)

## Function - LDAP Utilities: Add to Group(s)

### API Name
`ldap_utilities_add_to_groups`

### Output Name
``

### Message Destination
`fn_ldap_utilities`

### Pre-Processing Script
```python
# Both inputs must be a string representation of a List

## Example of multiple entries
# inputs.ldap_multiple_user_dn = "['dn=user1,dc=example,dc=com', 'dn=user2,dc=example,dc=com']"
# inputs.ldap_multiple_group_dn = "['dn=Accounts Group,dc=example,dc=com', 'dn=IT Group,dc=example,dc=com']"

# Both inputs must be a string representation of a List
inputs.ldap_multiple_user_dn = rule.properties.ldap_multiple_user_dn
inputs.ldap_multiple_group_dn = rule.properties.ldap_multiple_group_dn

# If the incident field ldap_domain_name contains a value then set ldap_domain_name to that value
if incident.properties.ldap_domain_name:
  inputs.ldap_domain_name = incident.properties.ldap_domain_name
# If a value is given in the rule ldap_domain_name field then set ldap_domain_name to that value
if rule.properties.ldap_domain_name:
  inputs.ldap_domain_name = rule.properties.ldap_domain_name
```

### Post-Processing Script
```python
# If the function is successful in adding the users to said groups,
# a note is added to the incident

if (results.success):
  noteText = """<br><i style="color: #979ca3"> LDAP Utilities: Add User(s) to Group(s) <u>complete</u>:</i>
                    <b>User(s):</b> {}
                    <b>Group(s):</b> {}""".format(results.inputs.ldap_multiple_user_dn, results.inputs.ldap_multiple_group_dn)

  incident.addNote(helper.createRichText(noteText))
```

---
