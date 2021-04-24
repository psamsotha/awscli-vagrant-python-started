# awscli-vagrant

Vagrant setup to use [aws-cli][cli] version 2 on Ubuntu 18.04 LTS 64-bit box

### Install

```
vagrant up
```

### Enter machine

```
vagrant ssh
```

After entering the Vagrant box, you will have a new Pythong virtual environment installed and activated. The virtual environment is named `venv-vm`. You should see `(venv-vm)` at the beginning of your terminal prompt. This is an environment just for the Vagrant box. You will need to install an activate a different virtual environment on your development machine. The reason is that your development machine will not be able to use the same Python interpreter in your development environment as your Vagrant box. PyCharm has this feature in its Pro edition, but many developers will be using the community edition which does not have this feature. To install a virtual environment on your development machine, run the following commands

```
python3 -m pip venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

### Run aws-cli (in Vagrant box)

```bash
aws --version
aws configure
```

With the `aws configue` command, you will need to specify your AWS:
* access key
* secret key
* region (e.g. us-east-1)
* output format (e.g. json)

### ec2-cmd.py

In this starter project, there is a simple program to start and stop an EC2 instnce. The Python file is `ec2-cmd.py`. The program requires that you have already run the `aws configure` command. It will get your credentials and configuration from the created `~/.aws/(config|credentials)` files. The program uses the AWS API Python SDK ([Boto3][boto]). You need to configure your EC2 machines in the `machines` property

```python
machines = {
  "ec2-name-1": "ec2-instance-id-1",
  "ec2-name-2": "ec3-instance-id-2"
}
```

You can run the program with `python ec2-cmd.py --cmd (start|stop) --instance ec2-name-1` to start or stop and instance.

### Shared Folder

The default shared folder for your Vagrant box is `. -> /vagrant`. In this project, the shared folder used is `. -> /home/vagrant`. This means that the home directory in your Vagrant box is where your project files will be. A lot of home folder generated files will be added to your project. Some of these files and folders are added to the `.gitignore`. If you want to change this shared folder behavior, then edit the `Vagrantfile: congfig.vm.synced_folder`



[cli]: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html
[boto]: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

