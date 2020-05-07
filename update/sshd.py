import paramiko

#sshtest
def ssh_order(hostname,port,username,password,order):
# 创建SSH对象
    ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
    ssh.connect(hostname, port, username, password)
# 执行命令
    stdin, stdout, stderr = ssh.exec_command('{0}'.format(order))
# 获取命令结果
    result = stdout.read()
# 关闭连接
    ssh.close()


#sftp file download 
def sftp_download(hostname,port,username,password,remove_path,local_path):
    transport = paramiko.Transport((hostname,port))
    transport.connect(username=username,password=password)
 
    sftp = paramiko.SFTPClient.from_transport(transport)
# 将remove_path 下载到本地 local_path
    sftp.get(remove_path, local_path)


#拉取现网文件
def sftp_upload(hostname,port,username,password,remove_path,local_path):
    transport = paramiko.Transport((hostname,port))
    transport.connect(username=username,password=password)
 
    sftp = paramiko.SFTPClient.from_transport(transport)
# 将remove_path 上传至服务器 local_path
    sftp.put(remove_path, local_path)