# check_mongodb - Get MongoDB Status for Zabbix

从 MongoDB db.serverStatus() 获取信息

[serverStatus](https://docs.mongodb.com/manual/reference/command/serverStatus/)

***

## Zabbix Items Key

* check.mongodb[asserts.regular]
* check.mongodb[asserts.rollovers]
* check.mongodb[asserts.user]
* check.mongodb[asserts.msg]
* check.mongodb[connections.available]
* check.mongodb[connections.current]
* check.mongodb[mem.bits]
* check.mongodb[mem.mapped]
* check.mongodb[mem.mappedWithJournal]
* check.mongodb[mem.resident]
* check.mongodb[mem.virtual]
* check.mongodb[network.bytesIn]
* check.mongodb[network.bytesOut]
* check.mongodb[opcounters.command]
* check.mongodb[opcounters.delete]
* check.mongodb[opcounters.getmore]
* check.mongodb[opcounters.insert]
* check.mongodb[opcounters.query]
* check.mongodb[opcounters.update]
* check.mongodb[extra_info.page_faults]
* check.mongodb[localTime]
* check.mongodb[process]
* check.mongodb[uptime]
* check.mongodb[version]

参数会被直接添加在 db.serverStatus() 之后以获取相关值，如 db.serverStatus().mem.bits
