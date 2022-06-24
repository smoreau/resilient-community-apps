<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Defender Find Machines by Internal IP Address

## Function - Defender Find Machines by Internal IP

### API Name
`defender_find_machines`

### Output Name
`None`

### Message Destination
`fn_microsoft_defender`

### Pre-Processing Script
```python
inputs.defender_indicator_value = artifact.value
inputs.defender_lookback_timeframe = rule.properties.defender_lookback_timeframe
```

### Post-Processing Script
```python
import java.util.Date as Date
now = Date().getTime()

"""
"value": [
    {
        "id": "04c99d46599f078f1c3da3783cf5b95f01ac61bb",
        "computerDnsName": "",
        "firstSeen": "2017-07-06T01:25:04.9480498Z",
        "osPlatform": "Windows10",
    }
]
"""
if results.success:
  if not results.content['value']:
    msg = u"Defender ATP Find machines by Internal IP Address unsuccessful.\nNothing found for {}".format(artifact.value)
    incident.addNote(helper.createPlainText(msg))
  else:
    for machine in results.content['value']:
        row = incident.addRow("defender_machines")
        row['report_date'] = now
        row['machine_link'] = "<a target='blank' href='https://security.microsoft.com/machines/{}/overview'>Machine</a>".format(machine['mdatpDeviceId'])
        row['machine_id'] = machine['id']
        row['machine_ip'] = machine['lastExternalIpAddress']
        row['machine_internal_ip'] = machine['lastIpAddress']
        row['machine_name'] = machine['computerDnsName']
        row['machine_platform'] = machine['osPlatform']
        row['machine_firstseen'] = machine['firstSeen_ts']
        row['machine_lastseen'] = machine['lastSeen_ts']
        row['machine_health_status'] = machine.get('healthStatus')
        row['machine_risk_score'] = machine.get('riskScore')
        row['machine_exposure_level'] = machine.get('exposureLevel')
        row['machine_tags'] = ', '.join(machine.get('machineTags', []))
else:
    msg = u"Defender Action unsuccessful.\nAction: Find machines by Internal IP Address\nReason: {}".format(results.reason)
    incident.addNote(helper.createPlainText(msg))
```

---
