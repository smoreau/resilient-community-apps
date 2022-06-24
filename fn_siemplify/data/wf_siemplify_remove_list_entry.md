<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Siemplify Remove Blocklist/Custom List Entity

## Function - Siemplify Remove List Entry

### API Name
`siemplify_remove_list_entry`

### Output Name
`None`

### Message Destination
`fn_siemplify`

### Pre-Processing Script
```python
inputs.siemplify_entity_id = row['entity_id']
inputs.siemplify_entity_list  = row['list_name']
inputs.siemplify_entity_value = row['entity']
inputs.siemplify_entity_type = row['entity_type']
inputs.siemplify_environments = row['environments']
```

### Post-Processing Script
```python
if results.success:
  incident.addNote("Siemplify Remove {} Entity '{}' successful".format(row['list_name'], row['entity']))
  row['entity'] = "{} (deleted)".format(row['entity'])
else:
  incident.addNote("Siemplify Remove {} Entity '{}' failed: {}".format(row['list_name'], row['entity'], results.reason))
```

---
