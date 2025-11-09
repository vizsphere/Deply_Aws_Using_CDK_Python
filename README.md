# Deply_Aws_Using_CDK_Python

# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
 * `cdk destroy`     CDK destroy
 
 
Enjoy!



### AWS Cloud Development Kit (AWS CDK)

```
npm install -g aws-cdk

cdk version 

cdk --help 

cdk --list

```


```
aws configure ---profile name aws_dev_1

```

### Links

https://docs.aws.amazon.com/cdk/v2/guide/home.html

https://pypi.org/project/aws-cdk.aws-s3/

https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html

-- configure profile name
https://iriscompanyio.medium.com/how-to-set-up-and-use-multiple-aws-profiles-using-aws-cli-00881cf93f4c


#### Construct Hub
https://constructs.dev/

https://github.com/cdklabs/construct-hub

Create Table 

Create Bucket 

Create Function 

(Laym fun => Dynamo Db => S3)