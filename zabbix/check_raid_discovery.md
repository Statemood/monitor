#RAID info discovery

MegaCli 需要 root 权限才能获取相关数据，因此需要对sudo进行配置。  

/etc/sudoer settings:  
 
`Cmnd_Alias MEGACLIDISK = /usr/local/bin/megacli -PDList –a0` . 
`Cmnd_Alias MEGACLIRAID = /usr/local/bin/megacli -adpallinfo -a0` . 
`zabbix    ALL=(ALL)   NOPASSWD: MEGACLIDISK, MEGACLIRAID` . 
