<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-circuits codegen
-->

# Example: Kafka Send

## Function - Kafka Send

### API Name
`kafka_send`

### Output Name
`None`

### Message Destination
`fn_kafka`

### Pre-Processing Script
```python
inputs.kafka_topic = rule.properties.kafka_topic
inputs.kafka_message = rule.properties.kafka_message.content
inputs.kafka_broker_label = rule.properties.kafka_broker_label
inputs.kafka_key = rule.properties.kafka_key
```

### Post-Processing Script
```python
None
```

---
