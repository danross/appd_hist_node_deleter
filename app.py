def download_selenium_packages():
    if os.name == "posix":
        print("Downloading selenium packages!")
        os.mkdir("/tmp/bin/")
        s3 = boto3.client('s3')

        filename = '/tmp/bin/chromedriver'
        if os.path.isfile(filename):
            with open(filename, 'wb+') as f:
                s3.download_fileobj('selenium-packages', 'chromedriver', f)

        filename = '/tmp/bin/headless-chromium'
        with open(filename, 'wb+') as f:
            s3.download_fileobj('selenium-packages', 'headless-chromium', f)


def lambda_handler(event, context):
	print("event = " + str(event))
