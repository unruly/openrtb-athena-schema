# openrtb-athena-schema

A project to derive OpenRTB schemas to plug into AWS Athena.

## Generating the schemas

Requires: *Python* 

```
$ python generate-schemas.py

*** Generating schema for [bid-request-2.0.json]
*** Generating schema for [bid-response-2.0.json]

$ ls *.schema

bid-request-2.0.schema	bid-response-2.0.schema
```

## Using in Athena

Below is a shortened schema of a Bid Responses table (with most of the bid_response field truncated for readability)

```sql
CREATE EXTERNAL TABLE bid_responses (
    `bid_response` struct<cur:string,customdata:string[...] 
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
LOCATION 's3://my-open-rtb-data.s3.amazonaws.com/path-to-bid-responses/';
```

## Supported Formats

* JSON

This project may work on OpenRTB logs formatted as Avro or Thrist but they are not officially supported.