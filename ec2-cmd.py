import boto3
import botocore
import argparse
import sys

PROFILE_NAME = "default"

region = "us-east-1"
machines = {
    "ec2-name-1": "ec2-instance-id-1",
    "ec2-name-2": "ec3-instance-id-2"
}

parser = argparse.ArgumentParser(description="Process EC2 Commands")
parser.add_argument("--cmd", dest="command", help="enter command start|stop")
parser.add_argument("--instance", dest="machine", help="enter machine name test-ec2")
results = parser.parse_args()


def init_session(reg=None):
    if reg is None:
        _reg = region
    _session = boto3.session.Session(region_name=reg, profile_name=PROFILE_NAME)
    return _session


if __name__ == "__main__":
    print("Running..")
    _ec2 = init_session().client("ec2")
    _machine = results.machine

    if _machine is not None:
        _machine_id = machines[_machine]

        if results.command == "start":
            try:
                _ec2.start_instances(InstanceIds=[_machine_id], DryRun=False)
                print("%s (%s) instance started." % (_machine, _machine_id))
            except botocore.exceptions.ClientError as e:
                print(e.response["Error"]["Machine"])
                sys.exit(404)

        elif results.command == "stop":
            try:
                _ec2.stop_instances(InstanceIds=[_machine_id], DryRun=False)
                print("%s (%s) instance stopped." % (_machine, _machine_id))
            except botocore.exceptions.ClientError as e:
                print(e.response["Error"]["Machine"])
                sys.exit(404)

    else:
        print("Instance not found")
        parser.print_usage()
        sys.exit(0)
