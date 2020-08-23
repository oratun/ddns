# coding: utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109.DescribeSubDomainRecordsRequest import DescribeSubDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest

import datetime
import json
import urllib.request


client = AcsClient('',  # AccessKeyId
                   '',  # AccessKeySecret
                   'cn-hangzhou'  # region
                   )

ip_source = 'https://jsonip.com'  # 用于获取本机公网ip的第三方接口
# ip_source = 'http://www.3322.org/dyndns/getip'


def get_internet_ip(ip_source):
    with urllib.request.urlopen(ip_source) as r:
        ip = json.loads(r.read()).get('ip')
    return ip


def update_domain(domain, current_ip):
    request = DescribeSubDomainRecordsRequest()
    sub_domain = domain['RR'] + '.' + domain['DomainName']
    print(sub_domain)
    request.set_SubDomain(sub_domain)
    response = client.do_action_with_exception(request)
    r = json.loads(response)
    print(datetime.datetime.now(), r)

    records = r['DomainRecords']['Record']
    if records:
        # 存在记录
        record = records[0]
        if record['Value'] != current_ip:
            update_request = UpdateDomainRecordRequest()
            # 主机记录
            update_request.set_RR(domain['RR'])
            # 记录ID
            update_request.set_RecordId(record['RecordId'])
            # 主机记录值设为当前主机IP
            update_request.set_Value(current_ip)
            # 解析记录类型
            update_request.set_Type(domain['Type'])
            update_response = client.do_action_with_exception(update_request)
            print(json.loads(update_response))


if __name__ == '__main__':
    # 当前公网ip
    ip = get_internet_ip(ip_source)
    # 多个域名
    domain_list = [
        {'RR': 't', 'DomainName': 'oratun.top', 'Type': 'A'},
    ]
    for domain in domain_list:
        update_domain(domain, ip)
