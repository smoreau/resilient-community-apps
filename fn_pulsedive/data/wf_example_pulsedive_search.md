<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-circuits codegen
-->

# Example: Pulsedive Search

## Function - Pulsedive: Search

### API Name
`pulsedive_search`

### Output Name
``

### Message Destination
`fn_pulsedive`

### Pre-Processing Script
```python

inputs.incident_id = incident.id
inputs.attachment_name = rule.properties.attachment_name
inputs.pulsedive_attribute = rule.properties.pulsedive_attribute
inputs.pulsedive_indicator_type = rule.properties.pulsedive_indicator_type
inputs.pulsedive_category = rule.properties.pulsedive_category
inputs.pulsedive_feed = rule.properties.pulsedive_feed
inputs.pulsedive_limit = rule.properties.pulsedive_limit
inputs.pulsedive_lastseen = rule.properties.pulsedive_lastseen
inputs.pulsedive_pretty = rule.properties.pulsedive_pretty
inputs.pulsedive_property = rule.properties.pulsedive_property
inputs.pulsedive_risk = rule.properties.pulsedive_risk
inputs.pulsedive_search_type = rule.properties.pulsedive_search_type
inputs.pulsedive_search_value = rule.properties.pulsedive_search_value
inputs.pulsedive_splitrisk = rule.properties.pulsedive_splitrisk
inputs.pulsedive_threat = rule.properties.pulsedive_threat

```

### Post-Processing Script
```python
# get results and post summary to incident note
search_type = results.get("resp_json")["inputs"]["pulsedive_search_type"]["name"] if not None else "n/a"
return_limit = results.get("resp_json")["inputs"]["pulsedive_limit"]["name"] if not None else "n/a"
time_frame = results.get("resp_json")["inputs"]["pulsedive_lastseen"]["name"] if not None else "n/a"
risk_filter = [str(x["name"]) for x in results.get("resp_json")["inputs"]["pulsedive_risk"]]
categories = [str(x["name"]) for x in results.get("resp_json")["inputs"]["pulsedive_category"]]

count = len(results.get("resp_json")["content"]["results"])

# create text for summary results
note_text = u"<p>Pulsedive <b>{}</b> search results:</p> \
<p><b>time frame:</b> {}</p> \
<p><b>risk filter</b> {}</p> \
<p><b>categories</b> {}</p> \
<p><b>max # of returned data</b> {}</p> \
<p><b>Results count:</b> {}</p> \n \
<p>See attachment <b>'{}'</b> for full dataset</p> \n \
".format(str(search_type), str(time_frame), risk_filter, categories, str(return_limit), count, 
results.get("att_name")
)

# append link for exporting results to CSV (for Indicator search only)
if results["search_type"] == "Indicator":
  export_url = u"""<a href='{}{}' target='blank'>here</a>""".format(results["request_url"], "&export=1")
  note_text += "Click {} to export results to CSV".format(export_url)

# Create note text
note = helper.createRichText(note_text)

# Create incident note
incident.addNote(note)
```

---
