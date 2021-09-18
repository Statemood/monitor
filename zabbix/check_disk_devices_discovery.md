#RAID info discovery


需要 root 通过 crontab 来更新 raid & disk 信息

> * * * * *     root    /usr/local/bin/megacli -PDList     –a0 -NoLog > /dev/shm/disk.info
> * * * * *     root    /usr/local/bin/megacli -adpallinfo -a0 -NoLog > /dev/shm/raid.info