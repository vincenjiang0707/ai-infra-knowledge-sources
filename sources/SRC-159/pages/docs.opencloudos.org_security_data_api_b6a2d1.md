source: https://docs.opencloudos.org/security_data_api

[
](https://gitee.com/opencloudos/Document/edit/master/docs/security_data_api.md)
[
](https://gitee.com/opencloudos/Document/raw/master/docs/security_data_api.md)
# OpenCloudOS安全中心API文档

## 1 安全公告列表接口

### 功能描述

### 调用方式

```
GET https://security.opencloudos.tech/api/v1/vms/public-info/advisories
```


### 请求参数说明

| 参数名称 |
类型 |
必填 |
描述 |
| page |
int |
否 |
当前页码，默认值为1。 |
| page_size |
int |
否 |
每页显示的数据条数，默认值为10。 |
| keywords |
string |
否 |
用于搜索公告ID或公告标题的关键词。 |
| severity |
string |
否 |
安全公告的严重程度，可多选，可选值为`critical` 、`important` 、`moderate` 、`low` 。 |
| date_start |
string |
否 |
查询起始日期，格式为`YYYY-MM-DD` 。 |
| date_end |
string |
否 |
查询结束日期，格式为`YYYY-MM-DD` 。 |

### 响应参数说明

HTTP status code为200成功，其他失败参照HTTP status codes

| 参数名称 |
类型 |
描述 |
| code |
int |
返回状态码，0表示成功。 |
| current_page |
int |
当前页码。 |
| data |
array |
公告信息数组，包含每个公告的详细信息。 |
| msg |
string |
返回消息，成功为`Success.` 。 |
| page_size |
int |
每页显示的数据条数。 |
| total |
int |
数据总数。 |
| total_page |
int |
总页数。 |

| 参数名称 |
类型 |
描述 |
| create_date |
string |
公告创建日期，格式为`YYYY-MM-DDTHH:MM:SS+08:00` （包含时区信息）。 |
| product_ids |
array |
相关产品ID数组。 |
| product_series |
string |
产品系列名称。 |
| publish_date |
string |
公告发布日期，格式为`YYYY-MM-DDTHH:MM:SS+08:00` （包含时区信息）。 |
| sa_id |
string |
安全公告ID。 |
| severity |
string |
公告严重程度。 |
| synopsis |
string |
公告概要内容。 |
| update_date |
string |
公告更新日期，格式为`YYYY-MM-DDTHH:MM:SS+08:00` （包含时区信息）。 |

### 请求例子

```
curl -X GET https://security.opencloudos.tech/api/v1/vms/public-info/advisories?page=1&page_size=20&keywords=2024&severity=critical&severity=important&severity=moderate&severity=low&date_start=2024-12-01&date_end=2024-12-31
{
"code": 0,
"current_page": 1,
"data": [
{
"create_date": "2024-12-13T00:11:33+08:00",
"product_ids": [
"OC8-8.10"
],
"product_series": "OC8",
"publish_date": "2024-12-12T18:01:14+08:00",
"sa_id": "OCSA-2024:1112",
"severity": "moderate",
"synopsis": "pcs security update",
"update_date": "2024-12-18T04:00:58+08:00"
},
...
],
"msg": "Success.",
"page_size": 20,
"total": 97,
"total_page": 5
}
```


## 2 安全公告详情接口

### 功能描述

### 调用方式

```
GET https://security.opencloudos.tech/api/v1/vms/public-info/csaf/<id>
```


### 请求参数说明

| 参数名称 |
类型 |
必填 |
描述 |
| id |
string |
是 |
安全公告id |

### 响应参数说明

HTTP status code为200成功，其他失败参照HTTP status codes

返回csaf v2 json schema https://docs.oasis-open.org/csaf/csaf/v2.0/csaf_json_schema.json https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html

### 请求例子

```
curl -X GET https://security.opencloudos.tech/api/v1/vms/public-info/csaf/OCSA-2024:1112
{
"document": {
"aggregate_severity": {
"text": "Moderate"
},
"category": "csaf_security_advisory",
"csaf_version": "2.0",
"distribution": {
"tlp": {
"label": "WHITE",
"url": "https://www.first.org/tlp/"
}
},
"lang": "en",
"notes": [
{
"category": "summary",
"text": "pcs security update",
"title": "Summary"
},
{
"category": "description",
"text": "Package updates are available for OpenCloudOS 8 that fix the following vulnerabilities:\n\nCVE-2024-21510:\nVersions of the package sinatra from 0.0.0 are vulnerable to Reliance on Untrusted Inputs in a Security Decision via the X-Forwarded-Host (XFH) header. When making a request to a method with redirect applied, it is possible to trigger an Open Redirect Attack by inserting an arbitrary address into this header. If used for caching purposes, such as with servers like Nginx, or as a reverse proxy, without handling the X-Forwarded-Host header, attackers can potentially exploit Cache Poisoning or Routing-based SSRF.",
"title": "Title"
}
],
"publisher": {
"category": "vendor",
"contact_details": "tencentos_secure@tencent.com",
"issuing_authority": "OpenCloudOS Security Incident Response Team is responsible for vulnerability handling across all OpenCloudOS offerings.",
"name": "OpenCloudOS Security Incident Response Team",
"namespace": "http://mirrors.tencent.com/tlinux/errata"
},
"title": "OpenCloudOS Security Advisory: pcs security update",
"tracking": {
"current_release_date": "2024-12-12T23:46:46+08:00",
"generator": {
"date": "2024-12-12T23:46:46+08:00",
"engine": {
"name": "OpenCloudOS-VMS",
"version": "1.0"
}
},
"id": "OCSA-2024:1112",
"initial_release_date": "2024-12-12T18:01:14+08:00",
"revision_history": [
{
"date": "2024-12-12T18:01:14+08:00",
"number": "1",
"summary": "Initial version"
},
{
"date": "2024-12-12T18:01:14+08:00",
"number": "2",
"summary": "Last updated version"
},
{
"date": "2024-12-12T23:46:46+08:00",
"number": "3",
"summary": "Last generated version"
}
],
"status": "final",
"version": "3"
}
},
"product_tree": {
"branches": [
{
"branches": [
{
"branches": [
{
"category": "product_name",
"name": "OpenCloudOS (v. 8.10)",
"product": {
"name": "OpenCloudOS (v. 8.10)",
"product_id": "OC8-8.10"
}
}
],
"category": "product_family",
"name": "OpenCloudOS"
},
{
"branches": [
{
"category": "product_version",
"name": "pcs-0.10.18-2.oc8.3.x86_64",
"product": {
"name": "pcs-0.10.18-2.oc8.3.x86_64",
"product_id": "pcs-0.10.18-2.oc8.3.x86_64"
}
},
{
"category": "product_version",
"name": "pcs-snmp-0.10.18-2.oc8.3.x86_64",
"product": {
"name": "pcs-snmp-0.10.18-2.oc8.3.x86_64",
"product_id": "pcs-snmp-0.10.18-2.oc8.3.x86_64"
}
}
],
"category": "architecture",
"name": "x86_64"
}
],
"category": "vendor",
"name": "Tencent"
}
],
"relationships": [
{
"category": "default_component_of",
"full_product_name": {
"name": "pcs-snmp-0.10.18-2.oc8.3.x86_64 as a component of OpenCloudOS (v. 8.10)",
"product_id": "OC8-8.10:pcs-snmp-0.10.18-2.oc8.3.x86_64"
},
"product_reference": "pcs-snmp-0.10.18-2.oc8.3.x86_64",
"relates_to_product_reference": "OC8-8.10"
}
]
},
"vulnerabilities": [
{
"cve": "CVE-2024-21510",
"cwe": {
"id": "CWE-807",
"name": "Reliance on Untrusted Inputs in a Security Decision"
},
"discovery_date": "2024-11-01T14:00:55+08:00",
"notes": [
{
"category": "description",
"text": "Versions of the package sinatra from 0.0.0 are vulnerable to Reliance on Untrusted Inputs in a Security Decision via the X-Forwarded-Host (XFH) header. When making a request to a method with redirect applied, it is possible to trigger an Open Redirect Attack by inserting an arbitrary address into this header. If used for caching purposes, such as with servers like Nginx, or as a reverse proxy, without handling the X-Forwarded-Host header, attackers can potentially exploit Cache Poisoning or Routing-based SSRF.",
"title": "Vulnerability description"
},
{
"category": "summary",
"text": "sinatra: Open Redirect Vulnerability in Sinatra via X-Forwarded-Host Header",
"title": "Vulnerability summary"
},
{
"category": "general",
"text": "The CVSS score(s) listed for this vulnerability do not reflect the associated product's status, and are included for informational purposes to better understand the severity of this vulnerability.",
"title": "CVSS score applicability"
}
],
"product_status": {
"fixed": [
"OC8-8.10:pcs-snmp-0.10.18-2.oc8.3.x86_64"
]
},
"references": [
{
"category": "external",
"summary": "MITRE CVE Database",
"url": "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21510"
},
{
"category": "external",
"summary": "OpenCloudOS CVE Database",
"url": "http://mirrors.tencent.com/tencentos/cve/#/detail/CVE-2024-21510"
}
],
"release_date": "2024-11-01T13:00:04+08:00",
"remediations": [
{
"category": "vendor_fix",
"details": "yum update --advisory OCSA-2024:1112",
"product_ids": [
"OC8-8.10:pcs-snmp-0.10.18-2.oc8.3.x86_64"
],
"url": "http://mirrors.tencent.com/tlinux/errata/OCSA-202410987.xml"
}
],
"scores": [
{
"cvss_v3": {
"attackComplexity": "LOW",
"attackVector": "NETWORK",
"availabilityImpact": "NONE",
"baseScore": 5.4,
"baseSeverity": "MEDIUM",
"confidentialityImpact": "LOW",
"integrityImpact": "LOW",
"privilegesRequired": "NONE",
"scope": "UNCHANGED",
"userInteraction": "REQUIRED",
"vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N",
"version": "3.1"
},
"products": [
"OC8-8.10:pcs-snmp-0.10.18-2.oc8.3.x86_64"
]
}
],
"threats": [
{
"category": "impact",
"details": "Medium"
}
],
"title": "sinatra: Open Redirect Vulnerability in Sinatra via X-Forwarded-Host Header"
}
]
}
```


## 3 漏洞库列表接口

### 功能描述

### 调用方式

```
GET https://security.opencloudos.tech/api/v1/vms/public-info/vulns
```


### 请求参数说明

| 参数名称 |
类型 |
必填 |
描述 |
| keywords |
string |
否 |
用于搜索CVE编号或软件包的关键词。 |
| severity |
string |
否 |
漏洞严重程度，可多选，可选值为`critical` 、`high` 、`medium` 、`low` 。 |
| status |
string |
否 |
漏洞状态，可多选，可选值为`under_investigation` 、`affected` 、`not_affected` 、`fixed` 、`wont_fix` 。 |
| create_date_start |
string |
否 |
漏洞创建日期起始范围，格式为`YYYY-MM-DD` 。 |
| create_date_end |
string |
否 |
漏洞创建日期结束范围，格式为`YYYY-MM-DD` 。 |
| update_date_start |
string |
否 |
漏洞更新日期起始范围，格式为`YYYY-MM-DD` 。 |
| update_date_end |
string |
否 |
漏洞更新日期结束范围，格式为`YYYY-MM-DD` 。 |
| page |
int |
否 |
当前页码，默认值为1。 |
| page_size |
int |
否 |
每页显示的数据条数，默认值为10。 |
| sort |
string |
否 |
排序字段，默认为`create_date` 入库时间。 |
| order |
string |
否 |
排序方式，可选值为`asc` （升序）或`desc` （降序），默认为`desc` （降序）。 |

### 响应参数说明

HTTP status code为200成功，其他失败参照HTTP status codes

| 参数名称 |
类型 |
描述 |
| code |
int |
返回状态码，0表示成功。 |
| current_page |
int |
当前页码。 |
| data |
array |
漏洞信息数组，包含每个漏洞的详细信息。 |
| msg |
string |
返回消息，成功为`Success.` 。 |
| page_size |
int |
每页显示的数据条数。 |
| total |
int |
数据总数。 |
| total_page |
int |
总页数。 |

| 参数名称 |
类型 |
描述 |
| create_date |
string |
漏洞创建日期，格式为`YYYY-MM-DDTHH:MM:SS+08:00` （包含时区信息）。 |
| cve_id |
string |
CVE（Common Vulnerabilities and Exposures）标识符。 |
| cwe_id |
string |
CWE（Common Weakness Enumeration）标识符。 |
| details |
string |
漏洞详细信息。 |
| severity |
string |
漏洞严重程度。 |
| status |
string |
漏洞状态。 |
| update_date |
string |
漏洞更新日期，格式为`YYYY-MM-DDTHH:MM:SS+08:00` （包含时区信息）。 |

### 请求例子

```
curl -X GET https://security.opencloudos.tech/api/v1/vms/public-info/vulns?keywords=http&severity=critical&severity=high&severity=medium&severity=low&status=under_investigation&status=affected&status=not_affected&status=fixed&status=wont_fix&create_date_start=2023-11-30&create_date_end=2024-12-31&update_date_start=2024-12-01&update_date_end=2024-12-31&page=1&page_size=20&sort=desc&order=create_date
{
"code": 0,
"current_page": 1,
"data": [
{
"create_date": "2024-12-07T10:00:31+08:00",
"cve_id": "CVE-2024-11148",
"cwe_id": "CWE-476",
"details": "In OpenBSD 7.4 before errata 006 and OpenBSD 7.3 before errata 020, httpd(8) is vulnerable to a NULL dereference when handling a malformed fastcgi request.",
"severity": "high",
"status": "not_affected",
"update_date": "2024-12-12T17:51:45+08:00"
},
...
],
"msg": "Success.",
"page_size": 20,
"total": 14,
"total_page": 1
}
```


## 4 CVE漏洞详情接口

### 功能描述

### 调用方式

```
GET https://security.opencloudos.tech/api/v1/vms/public-info/vulns/<id>
```


### 请求参数说明

| 参数名称 |
类型 |
必填 |
描述 |
| id |
string |
是 |
CVE编号 |

### 响应参数说明

HTTP status code为200成功，其他失败参照HTTP status codes

| 参数名称 |
类型 |
描述 |
| code |
int |
返回状态码，0表示成功 |
| data |
object |
安全漏洞信息列表 |
| msg |
string |
返回消息，成功为"Success." |

| 参数名称 |
类型 |
描述 |
| affects |
array |
影响的产品列表 |
| cve_id |
string |
CVE ID |
| cvss |
object |
CVSS 评分详情 |
| cve_date |
string |
发布日期，格式为ISO 8601 |
| cwe_id |
string |
CWE ID |
| details |
string |
漏洞详细描述 |
| publish_date |
string |
发布日期，格式为ISO 8601 |
| create_date |
string |
更新日期，格式为ISO 8601 |

### 请求例子

```
curl -X GET https://security.opencloudos.tech/api/v1/vms/public-info/vulns/CVE-2020-36309
{
"code": 0,
"data": {
"affects": [
{
"affect_details": "",
"affect_package_name": "openresty",
"product_id": "OC9-9.2",
"sa_id": "",
"sa_publish_date": "",
"status": "not_affected"
}
],
"create_date": "2024-12-14T22:54:14+08:00",
"cve_date": "2021-04-07T01:32:45+08:00",
"cve_id": "CVE-2020-36309",
"cvss": {
"attack_complexity": "Low(L)",
"attack_vector": "Network(N)",
"availability_impact": "None(N)",
"confidentiality_impact": "None(N)",
"integrity_impact": "Low(L)",
"privileges_required": "None(N)",
"scope": "Unchanged(U)",
"score": 5.3,
"user_interaction": "None(N)",
"vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N",
"version": "3.1"
},
"cwe_id": "",
"details": "ngx_http_lua_module (aka lua-nginx-module) before 0.10.16 in OpenResty allows unsafe characters in an argument when using the API to mutate a URI, or a request or response header.",
"publish_date": "",
"severity": "medium",
"status": "not_affected",
"update_date": "2024-12-16T15:05:21+08:00"
},
"msg": "Success."
}
```