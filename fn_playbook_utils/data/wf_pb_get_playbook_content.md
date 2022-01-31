<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-circuits codegen
-->

# PB: Get playbook content

## Function - PB: Get playbook content

### API Name
`pb_get_playbook_content`

### Output Name
`None`

### Message Destination
`fn_playbook_utils`

### Pre-Processing Script
```python
inputs.pb_id = row['workflow_id']
```

### Post-Processing Script
```python
if results.success:
  content = []
  for k in sorted(results.content.keys()):
    lizt = [v for v in results.content[k]]
    content.append("{}:<br>&nbsp;&nbsp;{}".format(k, "<br>&nbsp;&nbsp;".join(lizt)))
    
  row['workflow_content'] = helper.createRichText("<br><br>".join(content))
else:
  incident.addNote("PB: Get workflow content failed: {}".format(results.reason))

```

---
