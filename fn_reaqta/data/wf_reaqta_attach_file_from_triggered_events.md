<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# ReaQta: Attach File from Triggered Event

## Function - ReaQta: Attach File

### API Name
`reaqta_attach_file`

### Output Name
`None`

### Message Destination
`fn_reaqta`

### Pre-Processing Script
```python
inputs.reaqta_program_path = row['program_path']
inputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id
inputs.reaqta_incident_id = incident.id
inputs.reaqta_hive = incident.properties.reaqta_hive
```

### Post-Processing Script
```python
if results.success:
  incident.addNote(u"ReaQta Attach File created: {} from program path: {}".format(results.content['name'], results.inputs['reaqta_program_path']))
else:
  incident.addNote(u"ReaQta Attach File failed: {}".format(results.reason))
```

---
